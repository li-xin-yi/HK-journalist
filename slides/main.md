---
title: HKJournalist Module
subtitle: A Custom Automatic Report Generator for Python Programs
author: Xinyi Li
date: \today{}
aspectratio: 169
---

## Basic Idea

**Template**

- Write a `.md` report with `{var_name}` placeholders instead of real values in some critical places

**Python Runtime**

- Maintain a global `dict` variable `config` to fetch mappings in time

```{.python}
config = {'var_name': value}
```

- Read `.md` template and fill in real value bound with `var_name`

```{.python}
report_template_text = open('template.md','r').read()
Path('raw_report.md').write_text(report_template_text.format(**config))
```

- Call `pandoc` to convert `md` report to `pdf` slides

```
pandoc -t beamer raw_report.md -o report.pdf
```

## Wrap Python runtime tasks into a module {.fragile}

```{.python}
from hkjournalist import Journalist

config = dict(...)

reporter = Journalist(template_file='template.md')
reporter.hear(config)
reporter.report(output_file='output.pdf',beamer=True)
```

## Display support for special types

`pandas.DataFrame`

: $\to$ 3-line table (if numeric, round to `{.2f}`)

`matplotlib.axes.SubplotBase`

: $\to$

    1. save into a `pdf` standalone file in temp directory
    2. use `![]({var_name})` in template for referring
    3. runtime change as `![](../tmp/xxx.pdf)`
    4. **Note:** before assigning it to `dict`, use
  ```{.python}
  plt.tight_layout()
  ```
  for better performance.

`function`

: print its definition

`list(str)`

: concatenate into a sentance, following its length (e.g. show features list)

## Install

**Pre-requirements**

Pandoc

: https://pandoc.org/installing.html

pdfLaTeX

: integrated in [TeXLive](https://www.tug.org/texlive/) (and [MacTeX](http://www.tug.org/mactex/) for MacOS users).

**Make sure your environment variables set properly.**

- Install from [PyPI](https://pypi.org/project/hkjournalist/):
```
pip install hkjournalist
```
**For `Jupyter Notebook` users with Chrome**

- cannot open `.pdf` on file browser. Download [Firefox](https://www.mozilla.org/en-US/firefox/new/).

## Example
\framesubtitle{template.md}

:::::::::::::: {.columns}
::: {.column width="50%"}

````{.markdown}
% Hello World
% Xinyi Li
% 2019-12-19

---

### sine plot

![]({sin_plot})

### sine table

{sin_table}
````
:::

::: {.column width="50%"}

````{.markdown .numberLines startFrom="14"}

### sine function

```{{.python}}
{sin_func}
```
````
**Note**

: use `{{}}` to escape `{}`
:::
::::::::::::::

## Example {.allowframebreaks}
\framesubtitle{demo.py (leave out headers)}

```{.python}
config = {}
def sin_2x_and_cos_2x(x):
    y = np.sin(x) * np.sin(x) + np.cos(x) *  np.cos(x)
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
# sin_2x_and_cos_2x as sin_func
config['sin_func'] = sin_2x_and_cos_2x

# HK journalist runs faster than everyone! hear variables and make a big report
reporter = Journalist(template_file='template.md')
reporter.hear(config)
reporter.report(output_file='big_news.pdf', beamer=True, overwrite=True)
```

## Example
\framesubtitle{big\_news.pdf}
![](figures/big_news.pdf){ height=100% }

## Features

### Snapshot

```{.python}
Journalist.report(overwrite=False)
```

- it is why use `.pdf` instead of `.html` or raw `.md`
- add a timestamp at the end of output filename, such as `1_prophet_report_2019-12-18_22:06:18.pdf`

### Generate Template

```{.python}
Journalist.generate_template()
```

- after `hear` method
- generate template with **each** variable on subsection/slide page according its type:
  - `var_name` as *title*, `value` as *page content*
- slight modification for usage

## References

GitHub

: https://github.com/li-xin-yi/HK-journalist

Documents

: https://hk-journalist.readthedocs.io/en/latest/

Introduction

: https://zhuanlan.zhihu.com/p/98708920 (Chinese)

Write Guide

: https://pandoc.org/MANUAL.html
