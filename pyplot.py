import matplotlib.pyplot as plt
import pandas_datareader.data as web

plt.plot([1, 2, 3, 4])
# plt.show()

x = range(0, 100)
y = [v*v for v in x]
plt.plot(x, y, 'ro')
# plt.show()

lg = web.DataReader("066570.KS", "yahoo")
samsung = web.DataReader("005930.KS", "yahoo")

plt.plot(lg.index, lg['Adj Close'], label='LG Electronics')
plt.plot(samsung.index, samsung['Adj Close'], label='Samsung Electronics')

plt.legend(loc='upper left')
# plt.show()

"""
상단 주가 + 하단 거래량 그리기
"""
sk_hynix = web.DataReader("000660.KS", "yahoo")

fig = plt.figure(figsize=(12, 8))

top_axes = plt.subplot2grid((4,4), (0,0), rowspan=3, colspan=4)
bottom_axes = plt.subplot2grid((4,4), (3,0), rowspan=1, colspan=4)
bottom_axes.get_yaxis().get_major_formatter().set_scientific(False)

top_axes.plot(sk_hynix.index, sk_hynix['Adj Close'], label='Adjusted Close')
bottom_axes.plot(sk_hynix.index, sk_hynix['Volume'])

plt.tight_layout()
plt.show()