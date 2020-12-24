# for迴圈示範碼
## 方法(一) : for迴圈 + range()函數
for i in range(0, 5):
  print(i)
## 方法(二) : for迴圈 + 資料容器(數字串列)
for i in [0,1,2,3,4]:
  print(i)
0
1
2
3
4
0
1
2
3
4
## 1. 文字資料的例子
cars = ['Toyota', 'Honda']
 #把cars清單中的東西一個一個拿出來
for i in cars: #每次拿出來的東西暫時叫它i
  print(i) #清單中的每個東西都拿完就結束
Toyota
Honda
## 2. 英文串列的例子
names = ['Austin', 'Bryant', 'James', 'Jordan'] 
##計數迴圈:把names串列中的東西一個一個拿出來
for i in names: #每次拿出來的東西暫時叫它i
  print('Welcome to Class!', i) #清單中的每個東西都拿完就結束
Welcome to Class! Austin
Welcome to Class! Bryant
Welcome to Class! James
Welcome to Class! Jordan
## 3. 中文串列的例子
sheet = ['起司', '牛奶', '義大利麵', '披薩']
for i in range(0, len(sheet)): #位置索引從0開始[0,1,2]
  print(i, sheet[i]) #i是索引值，sheet[i]才是項目
0 起司
1 牛奶
2 義大利麵
3 披薩
## 4. 數字資料的例子
numbers = [117, 177, 777]
for i in numbers:
  print(i) #印拿出來的東西
for i in range(0, len(numbers)):
  print(i, numbers[i]) #索引和項目
117
177
777
0 117
1 177
2 777
# 作業 ###未完成
people = ["Mario", "Peach", "Luigi", "Toad", "Yoshi"]
dessert = ["Star Pudding", "Peach Pie", "Popsicles", "Honey Cake", "Cookies", "Jelly Beans"]
for i in people:
  print('Hi,my name is', i, '.')
for j in dessert:
  print('My favorite dessert is', j, '.')
Hi,my name is Mario .
Hi,my name is Peach .
Hi,my name is Luigi .
Hi,my name is Toad .
Hi,my name is Yoshi .
My favorite dessert is Star Pudding .
My favorite dessert is Peach Pie .
My favorite dessert is Popsicles .
My favorite dessert is Honey Cake .
My favorite dessert is Cookies .
My favorite dessert is Jelly Beans .
# 雙迴圈，for巢狀迴圈
for i in range(1,10): #控制輸出多少行
  for j in range(1,10): #每行輸出多少個
  #依序將「變數i* 變數j = 變數i 與j 相乘結果」顯示在螢幕
  #串接tab，設定sep與end為空字串
    print(i, '*', j, '=', i*j, '\t', sep='', end='')
  print() #每行輸出後換行
1*1=1   1*2=2   1*3=3   1*4=4   1*5=5   1*6=6   1*7=7   1*8=8   1*9=9   
2*1=2   2*2=4   2*3=6   2*4=8   2*5=10  2*6=12  2*7=14  2*8=16  2*9=18  
3*1=3   3*2=6   3*3=9   3*4=12  3*5=15  3*6=18  3*7=21  3*8=24  3*9=27  
4*1=4   4*2=8   4*3=12  4*4=16  4*5=20  4*6=24  4*7=28  4*8=32  4*9=36  
5*1=5   5*2=10  5*3=15  5*4=20  5*5=25  5*6=30  5*7=35  5*8=40  5*9=45  
6*1=6   6*2=12  6*3=18  6*4=24  6*5=30  6*6=36  6*7=42  6*8=48  6*9=54  
7*1=7   7*2=14  7*3=21  7*4=28  7*5=35  7*6=42  7*7=49  7*8=56  7*9=63  
8*1=8   8*2=16  8*3=24  8*4=32  8*5=40  8*6=48  8*7=56  8*8=64  8*9=72  
9*1=9   9*2=18  9*3=27  9*4=36  9*5=45  9*6=54  9*7=63  9*8=72  9*9=81  
