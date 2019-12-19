% Hello World
% Xinyi Li
% 2019-12-19

---

### Sine Plot

![](./temp/figure_0.pdf)

### Sine Table

|   x |   sin(x) |   cos(x) |   sin^2^(x)+cos^2^(x) |
|-----|----------|----------|-----------------------|
| 6.6 |     0.31 |     0.95 |                     1 |
| 5.6 |    -0.63 |     0.78 |                     1 |
| 7.3 |     0.85 |     0.53 |                     1 |
| 5.9 |    -0.37 |     0.93 |                     1 |
| 4.7 |    -1    |    -0.01 |                     1 |

### Sine Function

```{.python}
def sin_2x_and_cos_2x(x):
    y = np.sin(x) * np.sin(x) + np.cos(x) *  np.cos(x)
    return y

```
