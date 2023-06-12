```python
import pandas as pd
df1 = pd.read_excel("/Users/haneul/Desktop/실습/E15EXAMPLE.xlsx", sheet_name=0)
df2 = pd.read_excel("/Users/haneul/Desktop/실습/E15EXAMPLE.xlsx", sheet_name=1)
df3 = pd.read_excel("/Users/haneul/Desktop/실습/E15EXAMPLE.xlsx", sheet_name=2)

```

# 1. 불리언 인덱싱을 먼저 해준다.
## 연차를 1씩 올려주고,
## 은퇴선수에 해당하는 인원을 isin함수로 제거해준다.


```python
df1["연차"] = df1["연차"] +1
```


```python
cond1 = df1["이름"].isin(df3["이름"])
df1 = df1.loc[~cond1]
```

# 2. 불리언인덱싱으로 롯데만 필터링한다.


```python
cond2 = df2["지명팀"] == "롯데"
df2 = df2.loc[cond2]
```

# 3. df1과 df2를 df1형식으로 합친다.


```python
pd.concat([df1,df2.reindex(columns = df1.columns, fill_value = 1)])

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>이름</th>
      <th>포지션</th>
      <th>비고</th>
      <th>연차</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>강은탁</td>
      <td>투수</td>
      <td>우투우타</td>
      <td>17</td>
    </tr>
    <tr>
      <th>1</th>
      <td>방대한</td>
      <td>외야수</td>
      <td>좌투좌타</td>
      <td>17</td>
    </tr>
    <tr>
      <th>2</th>
      <td>김모범</td>
      <td>포수</td>
      <td>좌투우타</td>
      <td>15</td>
    </tr>
    <tr>
      <th>3</th>
      <td>김래원</td>
      <td>투수</td>
      <td>좌투좌타</td>
      <td>15</td>
    </tr>
    <tr>
      <th>4</th>
      <td>류수영</td>
      <td>외야수</td>
      <td>우투우타</td>
      <td>15</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>21</th>
      <td>김동욱</td>
      <td>외야수</td>
      <td>우투우타</td>
      <td>1</td>
    </tr>
    <tr>
      <th>39</th>
      <td>변우종</td>
      <td>포수</td>
      <td>좌투좌타</td>
      <td>1</td>
    </tr>
    <tr>
      <th>43</th>
      <td>권오현</td>
      <td>포수</td>
      <td>우투좌타</td>
      <td>1</td>
    </tr>
    <tr>
      <th>56</th>
      <td>고태진</td>
      <td>외야수</td>
      <td>우투양타</td>
      <td>1</td>
    </tr>
    <tr>
      <th>60</th>
      <td>서병철</td>
      <td>투수</td>
      <td>우투우타</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>97 rows × 4 columns</p>
</div>


