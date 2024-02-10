# pandas數據分析基礎練習
import pandas as pd


#讀取資料
data = pd.read_csv('googleplaystore.csv') #把CSV格式的檔案讀取成一個 DataFrame

#觀察資料
# print("Quantity",data.shape[0])
# print("Filed",data.columns)
# print("==================================================")

# condition = data["Rating"]<=5 #取小於等於5的資料
# print(data[condition])

# #分析資料:評分的各種統計數據
# print("平均數:", data["Rating"].mean())
# print("中位數:", data["Rating"].median())
# print("取得前一百個應用程式的平均:", data["Rating"].nlargest(100).mean())

#分析資料: 安裝數量的各種統計數據
#把字串型態轉化成數字型態,並且將Installs資料中的,+ Free轉化為空字串
#因為程式中有兩個replace,第一個replace沒有打regex = True的話 第二個也不會執行，所以必須先打在第一個replace後才能正常運作

# data["Installs"] = pd.to_numeric(data["Installs"].str.replace("[,+]","",regex=True).replace("Free","")) 
# print("平均數",data["Installs"].mean())
# condition = data["Installs"]>100000
# print("安裝數量大於100000 的應用程式有幾個",data[condition].shape[0])

#基於資料的應用:關鍵字搜尋應用程式名稱
# keyword = input("請輸入關鍵字:")
# condition = data["App"].str.contains(keyword, case=False) #應用程式名稱的字串是否包含使用者輸入的關鍵字,case=False忽略大小寫
# print("包含關鍵字的應用程式數量",data[condition].shape[0])

