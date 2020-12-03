from pandas import Series, DataFrame
import datetime

kakao = Series([92600, 92400, 92100, 94300, 92300], index=['2016-02-19',
                                                            '2016-02-18',
                                                            '2016-02-17',
                                                            '2016-02-16',
                                                            '2016-02-15'])

print(kakao)

for date in kakao.index:
    print(date)

for ending_price in kakao.values:
    print(ending_price)

mine   = Series([10, 20, 30], index=['naver', 'sk', 'kt'])
friend = Series([10, 30, 20], index=['kt', 'naver', 'sk'])

merge = mine + friend
print(merge)

raw_data = {'col0': [1, 2, 3, 4],
            'col1': [10, 20, 30, 40],
            'col2': [100, 200, 300, 400]}

data = DataFrame(raw_data)
print(data)

daeshin = {'open':  [11650, 11100, 11200, 11100, 11000],
           'high':  [12100, 11800, 11200, 11100, 11150],
           'low' :  [11600, 11050, 10900, 10950, 10900],
           'close': [11900, 11600, 11000, 11100, 11050]}

date = ['16.02.29', '16.02.26', '16.02.25', '16.02.24', '16.02.23']
daeshin_day = DataFrame(daeshin, columns=['open', 'high', 'low', 'close'], index=date)
print(daeshin_day)

day_data = daeshin_day.loc['16.02.24']
print(day_data)
print(type(day_data))
print(daeshin_day.columns)
print(daeshin_day.index)


start = datetime.datetime(2016, 2, 19)
end = datetime.datetime(2016, 3, 4)

import pandas_datareader.data as web
gs = web.DataReader("078930.KS", "yahoo", start, end)
gs = web.DataReader("078930.KS", "yahoo", "2014-01-01", "2016-03-06")

import matplotlib.pyplot as plt
plt.plot(gs.index, gs['Adj Close'])


new_gs = gs[gs['Volume'] != 0]
ma5 = new_gs['Adj Close'].rolling(window=5).mean()

print(type(new_gs))

new_gs.insert(len(new_gs.columns), 'MA5', ma5)
new_gs.tail(5)

plt.plot(new_gs.index, new_gs['Adj Close'], label="Adj Close")
plt.plot(new_gs.index, new_gs['MA5'], label="MA5")
plt.legend(loc='best')
plt.grid()