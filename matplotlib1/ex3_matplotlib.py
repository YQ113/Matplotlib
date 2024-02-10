#歷年觀光
#https://www.learncodewithmike.com/2021/03/pandas-and-matplotlib.html
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

df = pd.read_csv('matplotlib1\歷年國內主要觀光遊憩據點遊客人數月別統計.csv', encoding='utf-8')

rows = (df['年別'] == 2019) & (df['縣市別'] == '臺北市')
columns = ['細分', '1月', '2月', '3月']
result = df.loc[rows, columns].head(10) #Pandas套件的loc[rows, columns]選擇資料集
result.set_index('細分', inplace=True) #set_index()將索引值(index)更改為'細分'增加可讀性,inplace=True取代原索引值

chart = result.plot(figsize=(8, 5)) #圖表大小

font = FontProperties(fname=r'matplotlib1\NotoSansTC-Thin.otf')

for label in chart.get_xticklabels():
    label.set_fontproperties(font)  # 設定x軸每一個細分(景點名稱)字型
 
    plt.title('2019年臺北市各景點旅客人數', fontproperties=font)  #圖表標題
    plt.xlabel('細分(景點名稱)', fontproperties=font)  #x軸說明文字
    plt.ylabel('人數', fontproperties=font)  #y軸說明文字
    plt.legend(prop=font)  #圖例
                   
plt.show()


