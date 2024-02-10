import pandas as pd #載入模組

data = pd.Series([20,10,15]) #建立Series,顯示列表

print(data) #印出Series

print("------------------------------------------")

#建立DataFrame,
data = pd.DataFrame({
    "name": ["小琪","bella","cindy"],
    "age": [20,10,15]
}) 
print(data) #印出DataFrame,顯示字典
print(data["name"])#取得特地的欄位
print(data.iloc[0])#取得特定的列