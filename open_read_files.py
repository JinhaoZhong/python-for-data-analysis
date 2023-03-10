##data frame is like dictionary

## read txt file
with open("C:/Users/ZJH_8/Desktop/tmp.txt","r") as f1:
    file=f1.read()
print(f1.closed)
print(file)
print("type:", type(file))

## open as data frame
import panda as pd
path="C:/Users/ZJH_8/Desktop/tmp.csv"
df=pd.to_csv(path)  #pd.read_csv  read csv file
# pd.to_json(path) pd.read_json  read json file
# pd.to_excel(path) pd.read_excel  read excel file
# pd.to_sql(path) pd.read_sql  read sql file

print("#########################seperate#########################")
## read lines, print out as list
with open("C:/Users/ZJH_8/Desktop/tmp.txt","r") as f2:
    file2 = f2.readlines()
print(f2.closed)
print(file2)
print("type:",type(file2))

print("##################### read word by word ########################")
## print out num-1 words
with open("C:/Users/ZJH_8/Desktop/tmp.txt","r") as f3:
    tmp = f3.readline(16)
print(tmp)

print("##################### read line by line ########################")
import linecache
path="C:/Users/ZJH_8/Desktop/tmp.txt"
num=2
def get_line(path,num):
    return linecache.getline(path,num).strip()
print(get_line(path,num))

print("##################### rewrite file ########################")
## 如果有相同的就跳过，直接write没有的，如果原本有文字就全部删除只写新的，write没内容就全部删除
with open("C:/Users/ZJH_8/Desktop/tmp.txt","w") as f4:
    f4.write("this is line 1\n")
    f4.write("this is line 2\n")
    f4.write("this is line 3\n")
    f4.write("this is tmp file\n")
    f4.write("blablablablabla")


print("##################### use panda to read multiple files types ########################")

##  data frame count start as [0,0]
import pip
pip.main(["install", "openpyxl"])
import pandas as pd
xlsx_path = 'C:/Users/ZJH_8/Desktop/CarSalesByModelEnd.xlsx'
df = pd.read_excel(xlsx_path)
df.head
print(df)
print(df["Dealer ID"].unique())
print("######################list num row and num col#################################")

## looks like num of col = num of []
date = df[["Year", "Month"]]
print(date)

##  print specific col
year=df["Year"]
print(year)

## first row first col
df.ix[0,0]


