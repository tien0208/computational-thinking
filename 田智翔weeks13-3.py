for i in range (1,6,1):
  print('Hello')
Hello
Hello
Hello
Hello
Hello
for i in range (100,89,-3):
  print(i)
100
97
94
91
sum = 0
for i in range (3,13,3):
  sum = sum + i
print(sum)
30
start = int(input())
end = int(input())
step = int(input())
for i in range (start,end,step):
  print(i)
100
88
-3
100
97
94
91
start = int(input())
end = int(input())
step = int(input())
sum = 0
for i in range (start,end,step):
  sum = sum + i**2
print(sum)
1
6
1
55
for i in range(1,10,1):
  for j in range(1,10,1):
    print(i, '*', j, '=', i*j, '\t', end=' ')
  print()
1 * 1 = 1    1 * 2 = 2   1 * 3 = 3   1 * 4 = 4   1 * 5 = 5   1 * 6 = 6   1 * 7 = 7   1 * 8 = 8   1 * 9 = 9   
2 * 1 = 2    2 * 2 = 4   2 * 3 = 6   2 * 4 = 8   2 * 5 = 10      2 * 6 = 12      2 * 7 = 14      2 * 8 = 16      2 * 9 = 18      
3 * 1 = 3    3 * 2 = 6   3 * 3 = 9   3 * 4 = 12      3 * 5 = 15      3 * 6 = 18      3 * 7 = 21      3 * 8 = 24      3 * 9 = 27      
4 * 1 = 4    4 * 2 = 8   4 * 3 = 12      4 * 4 = 16      4 * 5 = 20      4 * 6 = 24      4 * 7 = 28      4 * 8 = 32      4 * 9 = 36      
5 * 1 = 5    5 * 2 = 10      5 * 3 = 15      5 * 4 = 20      5 * 5 = 25      5 * 6 = 30      5 * 7 = 35      5 * 8 = 40      5 * 9 = 45      
6 * 1 = 6    6 * 2 = 12      6 * 3 = 18      6 * 4 = 24      6 * 5 = 30      6 * 6 = 36      6 * 7 = 42      6 * 8 = 48      6 * 9 = 54      
7 * 1 = 7    7 * 2 = 14      7 * 3 = 21      7 * 4 = 28      7 * 5 = 35      7 * 6 = 42      7 * 7 = 49      7 * 8 = 56      7 * 9 = 63      
8 * 1 = 8    8 * 2 = 16      8 * 3 = 24      8 * 4 = 32      8 * 5 = 40      8 * 6 = 48      8 * 7 = 56      8 * 8 = 64      8 * 9 = 72      
9 * 1 = 9    9 * 2 = 18      9 * 3 = 27      9 * 4 = 36      9 * 5 = 45      9 * 6 = 54      9 * 7 = 63      9 * 8 = 72      9 * 9 = 81      
people = ["Mario", "Peach", "Luigi", "Daisy", "Toad", "Yoshi"]
desserts = ["Star Pudding", "Peach Pie", "Popsicles", "Honey Cake", "Cookies", "Jelly Beans"]
for index in range(len(people)):
  name = people[index]
  dessert = desserts[index] 
  print(f'Hi,my name is', name, '.My favorite dessert is', dessert, '.')
Hi,my name is Mario .My favorite dessert is Star Pudding .
Hi,my name is Peach .My favorite dessert is Peach Pie .
Hi,my name is Luigi .My favorite dessert is Popsicles .
Hi,my name is Daisy .My favorite dessert is Honey Cake .
Hi,my name is Toad .My favorite dessert is Cookies .
Hi,my name is Yoshi .My favorite dessert is Jelly Beans .
sum = 0
price = [100, 150, 120, 90, 145]
for i in price:
  sum = sum + i
print('總金額為', sum)
aver = sum / 5
print('平均金額為', aver)
總金額為 605
平均金額為 121.0
sign = ['*', '**', '***', '****', '******']
for i in sign:
  print(i)
*
**
***
****
******
for i in range(5): 
  print(" "*(4-i), end=' ')
  print("* "*(2*i+1))
     * 
    * * * 
   * * * * * 
  * * * * * * * 
 * * * * * * * * * 
for i in range(4):
  print(' '*(3-i), end=' ')
  print('* '*(3*i+1))
    * 
   * * * * 
  * * * * * * * 
 * * * * * * * * * * 
for i in range(1,6):
  for j in range(1,6):
    print(i, '*', j, '=', i*j, '\t', end='')
  print()
1 * 1 = 1   1 * 2 = 2   1 * 3 = 3   1 * 4 = 4   1 * 5 = 5   
2 * 1 = 2   2 * 2 = 4   2 * 3 = 6   2 * 4 = 8   2 * 5 = 10  
3 * 1 = 3   3 * 2 = 6   3 * 3 = 9   3 * 4 = 12  3 * 5 = 15  
4 * 1 = 4   4 * 2 = 8   4 * 3 = 12  4 * 4 = 16  4 * 5 = 20  
5 * 1 = 5   5 * 2 = 10  5 * 3 = 15  5 * 4 = 20  5 * 5 = 25  
Got it, thanks!Thanks, I'll check them out.What is this?