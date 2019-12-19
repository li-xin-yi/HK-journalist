% Report template 
% Author
% 2019-12-19

### Cover_type

Cover_Type

1    2160

2    2160

3    2160

4    2160

5    2160

6    2160

7    2160

dtype: int64

### shape

(15120, 55)

### dtypes

Elevation                             int64

Aspect                                int64

Slope                                 int64

Horizontal_Distance_To_Hydrology      int64

Vertical_Distance_To_Hydrology        int64

Horizontal_Distance_To_Roadways       int64

Hillshade_9am                         int64

Hillshade_Noon                        int64

Hillshade_3pm                         int64

Horizontal_Distance_To_Fire_Points    int64

dtype: object

### skew

Elevation                             0.075640

Aspect                                0.450935

Slope                                 0.523658

Horizontal_Distance_To_Hydrology      1.488052

Vertical_Distance_To_Hydrology        1.537776

Horizontal_Distance_To_Roadways       1.247811

Hillshade_9am                        -1.093681

Hillshade_Noon                       -0.953232

Hillshade_3pm                        -0.340827

Horizontal_Distance_To_Fire_Points    1.617099

dtype: float64

### description

|       |   Elevation |   Aspect |    Slope |   Horizontal_Distance_To_Hydrology |   Vertical_Distance_To_Hydrology |   Horizontal_Distance_To_Roadways |   Hillshade_9am |   Hillshade_Noon |   Hillshade_3pm |   Horizontal_Distance_To_Fire_Points |
|-------|-------------|----------|----------|------------------------------------|----------------------------------|-----------------------------------|-----------------|------------------|-----------------|--------------------------------------|
| count |    15120    | 15120    | 15120    |                           15120    |                         15120    |                          15120    |        15120    |         15120    |        15120    |                             15120    |
| mean  |     2749.32 |   156.68 |    16.5  |                             227.2  |                            51.08 |                           1714.02 |          212.7  |           218.97 |          135.09 |                              1511.15 |
| std   |      417.68 |   110.09 |     8.45 |                             210.08 |                            61.24 |                           1325.07 |           30.56 |            22.8  |           45.9  |                              1099.94 |
| min   |     1863    |     0    |     0    |                               0    |                          -146    |                              0    |            0    |            99    |            0    |                                 0    |
| 25%   |     2376    |    65    |    10    |                              67    |                             5    |                            764    |          196    |           207    |          106    |                               730    |
| 50%   |     2752    |   126    |    15    |                             180    |                            32    |                           1316    |          220    |           223    |          138    |                              1256    |
| 75%   |     3104    |   261    |    22    |                             330    |                            79    |                           2270    |          235    |           235    |          167    |                              1988.25 |
| max   |     3849    |   360    |    52    |                            1343    |                           554    |                           6890    |          254    |           254    |          248    |                              6993    |

### Corr

![](./temp/figure_0.pdf)

### select_method{.fragile}

```{.python}
def drop_by_cor(feature_df, threshold=0.9):
    corr_matrix = feature_df.corr().abs()
    upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool))
    to_drop = [column for column in upper.columns if any(upper[column] > threshold)]
    return to_drop

```

### features_remain_with_thres_as_70

9 Hillshade_9am, Aspect, Horizontal_Distance_To_Roadways, Vertical_Distance_To_Hydrology, Horizontal_Distance_To_Hydrology, Hillshade_Noon, Elevation, Slope, Horizontal_Distance_To_Fire_Points

