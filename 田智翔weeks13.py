for i in range(5):
  print('Hello')
Hello
Hello
Hello
Hello
Hello
for i in range(0,5,1):
  print(i)
0
1
2
3
4
for i in range(2,9,2):
  print(i)
2
4
6
8
for i in range(2,6):
  print(i)
2
3
4
5
for i in range(100,90,-3):
  print(i)
100
97
94
91
# 數字1到10之和。
## 1+2+3+4+5+6+7+8+9+10=? 
sum = 0 # 起始值
for i in range(1,11): # 加總運算，變更條件
  sum = sum + i # 加總運算，變更條件
print('Total is', sum)
Total is 55
# 數字1到10奇數之和。
## 1+3+5+7+9=?
sum = 0 # 起始值
for i in range(1,10,2): # 數字串列 [1,3,5,7,9]
  sum = sum + i # 加總運算，變更條件
print('Total is', sum)
Total is 25
# 隨堂練習1.
# 數字1到10偶數之和。
## 2+4+6+8+10=?
sum = 0
for i in range(2,11,2):
  sum = sum + i
print('Total is', sum)
Total is 30
# 隨堂練習2.
sum = 0
for i in range(3,13,3):
  sum = sum + i
print('Total is', sum)
Total is 30
#  加分練習
start = int(input('請輸入加總起始值'))
end = int(input('請輸入加總最終值')) # 取前一個數字
step = int(input('請輸入遞增減值'))

sum = 0
for i in range(start, end, step):
  sum = sum + i
print('Total is', sum)
請輸入加總起始值2
請輸入加總最終值9
請輸入遞增減值2
Total is 20
# 作業
sum = 0
n = int(input('Please enter a positive number'))
for i in range(0, n+1):
  sum = sum + i**2
print('When i is', i, ', total is', sum, '.')
