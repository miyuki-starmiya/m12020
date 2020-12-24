
import pandas as pd
import time
import datetime
import pytz
from matplotlib import pyplot as plt
from matplotlib import rcParams
import matplotlib.ticker as ticker

rcParams['font.family'] = 'Noto Sans CJK JP'
rcParams['font.sans-serif'] = 'Noto Sans CJK JP'
keyword_list = ['インディアンス','東京ホテイソン','ニューヨーク','見取り図','おいでやすこが','マヂカルラブリー','オズワルド','アキナ','錦鯉','ウエストランド']

def typechange(x):
    st = datetime.datetime.strptime(x, '%a %b %d %H:%M:%S +0000 %Y')
    # utc_time = datetime.datetime(st.tm_year, st.tm_mon,st.tm_mday, st.tm_hour,st.tm_min,st.tm_sec, tzinfo=datetime.timezone.utc)
    # jst_time = utc_time.astimezone(pytz.timezone('Asia/Tokyo'))
    # str_time = jst_time.strftime('%a %b %d %H:%M:%S +0900 %Y')
    return st

def replace(x):
    y = x.replace(tzinfo=None)
    return y

sum_list = []
rate_list = []
for keyword in keyword_list:
    # def make_df_re(keyword):
    df = pd.read_csv('data/m12020_'+keyword+'.csv', encoding='utf-16', sep='\t', header=0)
    df['count'] = 1
    df['datetime'] = df['created_at'].map(typechange)
    # print(df.info())

    from_dt = datetime.datetime(2020, 12, 20, 10, 20)
    to_dt = datetime.datetime(2020, 12, 20, 12, 40)

    df = df[from_dt <= df['datetime']]
    df = df[df['datetime'] <= to_dt]
    df_cut = pd.concat([df['datetime'], df['text'], df['count']], axis=1)

    # df_cut.to_csv('data/cut_'+keyword+'.csv', encoding='utf-16', sep='\t')

    df_result = df[df_cut.text.str.contains('面白かった|おもしろかった|おもろかった|良かった|よかった|笑った|好き|すき')]
    sum = len(df_result)
    print('sum :', keyword, len(df_result))
    rate = round(len(df_result)/(len(df_cut)), 2)
    print('rate', keyword, rate)
    sum_list.append(sum)
    rate_list.append(rate)

# グラフ作成
with plt.style.context('seaborn-darkgrid', after_reset=True):
    plt.rcParams['font.family'] = 'Noto Sans CJK JP'
    figure = plt.figure(1, figsize=(8,4))
    axes1 = figure.add_subplot(111)

    s0 = 1
    s1 = 2
    s2 = 3
    s3 = 4
    s4 = 5
    s5 = 6
    s6 = 7
    s7 = 8
    s8 = 9
    s9 = 10
    axes1.bar(s0, width=0.5, height=sum_list[0], color='#d52f25')
    axes1.bar(s1, width=0.5, height=sum_list[1], color='#691c0d')
    axes1.bar(s2, width=0.5, height=sum_list[2], color='#fff000')
    axes1.bar(s3, width=0.5, height=sum_list[3], color='#f0821e')
    axes1.bar(s4, width=0.5, height=sum_list[4], color='#00a0dc')
    axes1.bar(s5, width=0.5, height=sum_list[5], color='#ff2599')
    axes1.bar(s6, width=0.5, height=sum_list[6], color='#ffcc00')
    axes1.bar(s7, width=0.5, height=sum_list[7], color='#193278')
    axes1.bar(s8, width=0.5, height=sum_list[8], color='#9944cc')
    axes1.bar(s9, width=0.5, height=sum_list[9], color='#d3c1af')

    axes2 = axes1.twinx()
    r0 = rate_list[0]
    r1 = rate_list[1]
    r2 = rate_list[2]
    r3 = rate_list[3]
    r4 = rate_list[4]
    r5 = rate_list[5]
    r6 = rate_list[6]
    r7 = rate_list[7]
    r8 = rate_list[8]
    r9 = rate_list[9]
    # axes2.axis('off')
    axes2.plot(s0, r0, 's', ms=7, color='#7acbe1')
    axes2.plot(s1, r1, 's', ms=7, color='#7acbe1')
    axes2.plot(s2, r2, 's', ms=7, color='#7acbe1')
    axes2.plot(s3, r3, 's', ms=7, color='#7acbe1')
    axes2.plot(s4, r4, 's', ms=7, color='#7acbe1')
    axes2.plot(s5, r5, 's', ms=7, color='#7acbe1')
    axes2.plot(s6, r6, 's', ms=7, color='#7acbe1')
    axes2.plot(s7, r7, 's', ms=7, color='#7acbe1')
    axes2.plot(s8, r8, 's', ms=7, color='#7acbe1')
    axes2.plot(s9, r9, 's', ms=7, color='#7acbe1')

    axes1.set_ylabel('ツイート数合計')
    axes2.set_ylabel('ポジティブ比率')
    axes1.set_axisbelow(True)
    axes2.set_axisbelow(True)
    xticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    xaxis = axes1.xaxis
    xaxis.set_major_locator(ticker.FixedLocator(xticks))
    xaxis.set_ticklabels(['インディアンス','東京ホテイソン','ニューヨーク','見取り図','おいでやすこが','マヂカルラブリー','オズワルド','アキナ','錦鯉','ウエストランド'], rotation=45)
    # xaxis.set_ticklabels(['インディアンス','東京ホテイソン','ニューヨーク','見取り図','おいでやすこが','マヂカルラブリー','オズワルド','アキナ','錦鯉','ウエストランド'], rotation=45)
    # axes1.legend(('インディアンス','東京ホテイソン','ニューヨーク','見取り図','おいでやすこが','マヂカルラブリー','オズワルド','アキナ','錦鯉','ウエストランド'),
    # bbox_to_anchor=(1, 1), loc='upper left', borderaxespad=0, fontsize=10)
    # plt.savefig('data/fig.png')
    plt.show()



