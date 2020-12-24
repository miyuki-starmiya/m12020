
import codecs
import shutil
import pandas as pd
import time
import datetime
import pytz
from matplotlib import pyplot as plt
from matplotlib import dates as mdates
from matplotlib.dates import date2num
from matplotlib.dates import DateFormatter
from matplotlib import rcParams

rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']

keyword_list = ['インディアンス','東京ホテイソン','ニューヨーク','見取り図','おいでやすこが','マヂカルラブリー','オズワルド','アキナ','錦鯉','ウエストランド']

# str -> datetime

def typechange(x):
    st = time.strptime(x, '%a %b %d %H:%M:%S +0000 %Y')
    utc_time = datetime.datetime(st.tm_year, st.tm_mon,st.tm_mday, st.tm_hour,st.tm_min,st.tm_sec, tzinfo=datetime.timezone.utc)
    jst_time = utc_time.astimezone(pytz.timezone('Asia/Tokyo'))
    # str_time = jst_time.strftime('%a %b %d %H:%M:%S +0900 %Y')
    return jst_time
    # return datetime.datetime.strptime(x, '%a %b %d %H:%M:%S +0000 %Y')

def make_df_re(keyword):
    df = pd.read_csv('data/m12020_'+keyword+'.csv', encoding='utf-16', sep='\t', header=0)
    df['count'] = 1

    df['datetime'] = df['created_at'].map(typechange)

    # 分ごとにresampleしたdetaの取得
    df_date = pd.concat([df['datetime'], df['count']], axis=1)

    df_re = df_date.reset_index().set_index('datetime').resample('T').sum()
    # df_re.to_csv('data/re_'+keyword+'.csv', encoding='utf-16', sep='\t')
    df_re = df_re.reset_index()
    return df_re

df_list = []
for keyword in keyword_list:
    df_re = make_df_re(keyword)
    df_list.append(df_re)

# グラフ作成
with plt.style.context('seaborn-darkgrid', after_reset=True):
    plt.rcParams['font.family'] = 'Noto Sans CJK JP'
    figure = plt.figure(1, figsize=(8,4))
    axes = figure.add_subplot(111)

    x0 = df_list[0]['datetime']
    x1 = df_list[1]['datetime']
    x2 = df_list[2]['datetime']
    x3 = df_list[3]['datetime']
    x4 = df_list[4]['datetime']
    x5 = df_list[5]['datetime']
    x6 = df_list[6]['datetime']
    x7 = df_list[7]['datetime']
    x8 = df_list[8]['datetime']
    x9 = df_list[9]['datetime']
    y0 = df_list[0]['count']
    y1 = df_list[1]['count']
    y2 = df_list[2]['count']
    y3 = df_list[3]['count']
    y4 = df_list[4]['count']
    y5 = df_list[5]['count']
    y6 = df_list[6]['count']
    y7 = df_list[7]['count']
    y8 = df_list[8]['count']
    y9 = df_list[9]['count']
    start_time = datetime.datetime(2020, 12, 20, 10, 0)
    end_time = datetime.datetime(2020, 12, 20, 13, 0)

    axes.plot(x0, y0, color='#d52f25')
    axes.plot(x1, y1, color='#691c0d')
    axes.plot(x2, y2, color='#fff000')
    axes.plot(x3, y3, color='#f0821e')
    axes.plot(x4, y4, color='#00a0dc')
    axes.plot(x5, y5, color='#ff2599')
    axes.plot(x6, y6, color='#ffcc00')
    axes.plot(x7, y7, color='#193278')
    axes.plot(x8, y8, color='#9944cc')
    axes.plot(x9, y9, color='#d3c1af')
    axes.set_xlim(
        date2num([
            start_time,
            x9.max()])
    )
    axes.set_ylabel('ツイート数 / 分')
    xticks = [datetime.datetime(2020, 12, 20, 10, 0), datetime.datetime(2020, 12, 20, 10, 30), datetime.datetime(2020, 12, 20, 11, 00), datetime.datetime(2020, 12, 20, 11, 30), datetime.datetime(2020, 12, 20, 12, 00), datetime.datetime(2020, 12, 20, 12, 30), datetime.datetime(2020, 12, 20, 13, 00)]
    xaxis = axes.xaxis
    xaxis.set_ticklabels(['19:00', '19:30', '20:00', '20:30', '21:00', '21:30', '22:00'])
    plt.legend(('インディアンス','東京ホテイソン','ニューヨーク','見取り図','おいでやすこが','マヂカルラブリー','オズワルド','アキナ','錦鯉','ウエストランド'),
    bbox_to_anchor=(1, 1), loc='upper left', borderaxespad=0, fontsize=10)
    # axes.xaxis.set_major_formatter(DateFormatter('%H:%M'))
    plt.savefig('data/fig.png')
    plt.show()


