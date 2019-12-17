% Simple Model Test
% Author
% 2019-12-18

### Data Plot

![](./temp/figure_0.pdf){ width=100% }

### Train set

- **train end date** 20131231
- **seasonality**

|                | monthly   | quarter   | yearly   | weekly   |
|----------------|-----------|-----------|----------|----------|
| condition_name |           |           |          |          |
| fourier_order  | 12        | 10        | 10       | 3        |
| mode           | additive  | additive  | additive | additive |
| period         | 30.5      | 91.125    | 365.25   | 7        |
| prior_scale    | 10.0      | 5.0       | 10.0     | 10.0     |

### Prediction Result

![](./temp/figure_1.pdf){ width=100% }

### Error analysis

```{.python}
def kpi_mape(df, y_true, y_pred):
    ### mape group by yearmonth
    df[y_pred] = df[y_pred].clip(0, None)
    df['diff'] = abs(df[y_true] - df[y_pred])
    mape_df = df.groupby(['year', 'month']).agg({'diff': 'sum', y_true: 'sum'
                                                }).reset_index()
    mape_df['mape'] = mape_df['diff'] / mape_df[y_true]
    return mape_df.pivot(index='month', columns='year', values='mape')

```

### Error analysis (plot)

![](./temp/figure_2.pdf){ height=90% }

### Note

no holidays added
