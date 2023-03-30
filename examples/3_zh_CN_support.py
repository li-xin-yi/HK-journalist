import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from hkjournalist import Journalist


config = {}


def sin_2x_and_cos_2x(x):
    y = np.sin(x) * np.sin(x) + np.cos(x) * np.cos(x)
    return y


x = np.arange(0, 4 * np.pi, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

df = pd.DataFrame({'x': x, 'sin(x)': y1, 'cos(x)': y2})
df['sin^2^(x)+cos^2^(x)'] = sin_2x_and_cos_2x(df['x']).values
df = df.set_index('x')

# plot sine curve as sin_plot
ax = df.plot()
plt.tight_layout()
config['sin_plot'] = ax

# random select 5 point (x,y) as sin_table
config['sin_table'] = df.sample(5)

config['sin_func'] = sin_2x_and_cos_2x

reporter = Journalist(template_file='./reports/3_zh_cn_template.md', zh=True)
reporter.hear(config)
reporter.report(output_file='./reports/3_zh_report.pdf', beamer=True, overwrite=True)
