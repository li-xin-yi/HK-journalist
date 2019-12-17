import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
from hkjournalist.journalist import Journalist
from fbprophet import Prophet

sns.set(style="darkgrid")
config = {}

df = pd.read_csv('./data/example_wp_log_peyton_manning.csv')
df['ds'] = pd.to_datetime(df['ds'])

ax = df.set_index('ds').plot(figsize=(20, 10))
config['data_plot'] = ax

train_end_date = '20131231'
config['train_end_date'] = train_end_date
train_df = df[df['ds'] <= train_end_date]
test_df = df[df['ds'] > train_end_date]

test_df['year'] = test_df['ds'].dt.year
test_df['month'] = test_df['ds'].dt.month

model = Prophet(weekly_seasonality=True, yearly_seasonality=True)
model.add_seasonality('monthly', period=30.5, fourier_order=12, prior_scale=10)
model.add_seasonality('quarter', period=364.5 / 4, fourier_order=10, prior_scale=5)

model.fit(train_df)
config['seasonality'] = pd.DataFrame(model.seasonalities)
test_df['y_pred'] = model.predict(test_df[['ds']])['yhat'].values
config['pred_plot'] = test_df[['ds','y','y_pred']].set_index('ds').plot(figsize=(20,10))
print(test_df[['ds','y','y_pred']])


def kpi_mape(df, y_true, y_pred):
    ### mape group by yearmonth
    df[y_pred] = df[y_pred].clip(0, None)
    df['diff'] = abs(df[y_true] - df[y_pred])
    mape_df = df.groupby(['year', 'month']).agg({'diff': 'sum', y_true: 'sum'
                                                }).reset_index()
    mape_df['mape'] = mape_df['diff'] / mape_df[y_true]
    return mape_df.pivot(index='month', columns='year', values='mape')


config['metric_func'] = kpi_mape

kpi_df = kpi_mape(test_df, 'y', 'y_pred')
plt.figure(figsize=(8, 6))
ax = sns.heatmap(kpi_df, annot=True, cmap='YlGn')
#plt.savefig('./tmp/temp.pdf')
config['error_plot'] = ax

config['note'] = """no holidays added"""

report_journalist = Journalist(template_file='./reports/simple_model_report_template.md')
report_journalist.hear(config)
report_journalist.report(final_report_file='./reports/simple_model_report',format='.pdf')
