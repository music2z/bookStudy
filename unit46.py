import requests  # 웹 페이지의 HTML을 가져오는 모듈
from bs4 import BeautifulSoup  # HTML을 파싱하는 모듈

# 웹 페이지를 가져온 뒤 BeautifulSoup 객체로 만듦
response = requests.get('https://pythondojang.bitbucket.io/weather/observation/currentweather.html')
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table', {'class': 'table_develop3'})  # <table class="table_develop3">을 찾음
data = []  # 데이터를 저장할 리스트 생성
for tr in table.find_all('tr'):  # 모든 <tr> 태그를 찾아서 반복(각 지점의 데이터를 가져옴)
    tds = list(tr.find_all('td'))  # 모든 <td> 태그를 찾아서 리스트로 만듦
    # (각 날씨 값을 리스트로 만듦)
    for td in tds:  # <td> 태그 리스트 반복(각 날씨 값을 가져옴)
        if td.find('a'):  # <td> 안에 <a> 태그가 있으면(지점인지 확인)
            point = td.find('a').text  # <a> 태그 안에서 지점을 가져옴
            temperature = tds[5].text  # <td> 태그 리스트의 여섯 번째(인덱스 5)에서 기온을 가져옴
            humidity = tds[9].text  # <td> 태그 리스트의 열 번째(인덱스 9)에서 습도를 가져옴
            data.append([point, temperature, humidity])  # data 리스트에 지점, 기온, 습도를 추가

print(data)  # data 표시. 주피터 노트북에서는 print를 사용하지 않아도 변수의 값이 표시됨

with open('weather.csv', 'w') as file:
    file.write('point,temperature,humidity\n')
    for i in data:
        file.write('{},{},{}\n'.format(i[0], i[1], i[2]))

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

df = pd.read_csv('weather.csv', index_col='point', encoding='euc-kr')

city_df = df.loc[['서울', '인천', '대전', '대구', '광주', '부산', '울산']]

# Windows 한글 폰트 설정
font_name = mpl.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

# 차트 종류, 제목, 차트 크기, 범례, 폰트 크기 설정
ax = city_df.plot(kind='bar', title='날씨', figsize=(12, 4), legend=True, fontsize=12)
ax.set_xlabel('도시', fontsize=12)  # x축 정보 표시
ax.set_ylabel('기온/습도', fontsize=12)  # y축 정보 표시
ax.legend(['기온', '습도'], fontsize=12)  # 범례 지정
plt.show()

print(city_df.loc[city_df.temperature.argmax()])
print(city_df.loc[city_df.temperature.argmin()])