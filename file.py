# 儲存檔案 ("w"寫入(儲存)檔案,"r"讀取檔案,"r+"讀寫檔案)
file=open("data_1.txt",mode="w")               # 開啟
file.write("Hello File\nSecond line")          # 寫入
file.close()                                   # 關閉
# 最佳實務寫法(不須寫close)
with open("data_2.txt",mode="w",encoding="utf-8") as file:  # utf-8編碼可寫入英文以外文字
    file.write("測試中文\n第二行")
# 讀取檔案
with open("data_2.txt",mode="r",encoding="utf-8") as file:
    data=file.read()
print(data)
# 把檔案中的資料,一行一行讀取出來,並計算總合
with open("data_3.txt",mode="w",encoding="utf-8") as file:
    file.write("5\n3")
sum=0
with open("data_3.txt",mode="r",encoding="utf-8") as file:
    for line in file:   # 一行一行的讀取
        sum+=int(line)
print(sum)
# 使用json格式讀取、複寫檔案
import json
with open("config.json",mode="r") as file:
    data=json.load(file)
print(data)             # data是一個字典
print("name:",data["name"])
print("version",data["version"])
data["name"]="New Name" # 修改變數中的資料
# 把最新的資料複寫回檔案中
with open("config.json",mode="w") as file:
    json.dump(data,file)