import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from hkjournalist import Journalist

sns.set(style="darkgrid")

config = {}

for i in range(1, 4):
    uniform_data = np.random.rand(10, 12)
    plt.figure(figsize=(10, 8))
    ax = sns.heatmap(uniform_data, cmap='Blues', annot=True)
    plt.tight_layout()
    config[f'plot_{i}'] = ax

reporter = Journalist(fig_height='80%')
reporter.hear(config)
reporter.generate_template('auto_generate_template.md')
reporter.report(output_file='auto_report.pdf', beamer=True, overwrite=True)
