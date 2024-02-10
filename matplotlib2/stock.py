#電子投票占股東會出席比例
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

df = pd.read_csv('matplotlib2\電子投票占股東會出席比例.csv', encoding='big5hkscs')

rows = (df['年度'] == 112)
columns = ['證券名稱', '一般股東電子投票權數', '保管銀行電子投票權數', '保管銀行電子投票權數','其他專業機構法人電子投票權數']
result = df.loc[rows, columns].head(10)
result.set_index('證券名稱', inplace=True)

chart = result.plot(figsize=(8, 5)) #圖表大小

font = FontProperties(fname=r'matplotlib1\NotoSansTC-Thin.otf')

for label in chart.get_xticklabels():
    label.set_fontproperties(font)  # 設定x軸每一個細分(景點名稱)字型
 
    plt.title('112年電子投票占股東會投票權數', fontproperties=font)  #圖表標題
    plt.xlabel('證券名稱', fontproperties=font)  #x軸說明文字
    plt.ylabel('權重比數(%)', fontproperties=font)  #y軸說明文字
    plt.legend(prop=font)  #圖例
                   
plt.show()


