#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# AC!
def same_row(i,j): return (i//5 == j//5) #看是否為同列
def same_col(i,j): return (i-j) % 5 == 0 #看是否為同行
def same_area(i,j): return (b.index(i)//5 == b.index(j)//5) #看定義的區域是否有重複的數字

def solveSudoku(board):
    ans = []
    idx = board.index(0) if 0 in board else -1 # board哪裡有空格存在idx
    if idx == -1: #解完了就結束
        return board
    # 把前三個定義的條件拿來找同行、同列、同區的 set ，可自動找到還可以填哪個數字
    exclude = {board[j] for j in range(25) if same_row(idx,j) or same_col(idx,j) or same_area(idx,j)}
    for m in set('12345')-exclude:
        ans += solveSudoku(board[:idx]+[m]+board[idx+1:]) #遞迴
    return ans 


# 定義區塊
a1 = [x.split(',') for x in input().split( )]
a2 = [x.split(',') for x in input().split( )]
a3 = [x.split(',') for x in input().split( )]
a4 = [x.split(',') for x in input().split( )]
a5 = [x.split(',') for x in input().split( )]

#轉成數字
for k in (a1,a2,a3,a4,a5):   
    for i in range(5):
        for j in range(2):
            k[i][j] = int(k[i][j])
            
# 將區塊座標轉換為 25 elements 的 list
b = []
for x in (a1,a2,a3,a4,a5):
    for i in range(5):
        b.append(x[i][0]*5+x[i][1])

# 創空白 list
space = [0]*25
# 放入題目
while True:
    try: 
        n = [x.split(',') for x in input().split( )]
        n1 = list(map(int, n[0]))
        space[n1[0]*5+n1[1]] = n[1][0]
    except:
        break

# 解題
Ans = solveSudoku(space)
# 列印
if len(Ans) == 25:
    for i in range(5):
        pr = []
        for j in range(5):
            pr.append(Ans[5*i+j])
        print(*pr, sep = ' ')   
else:
    print('no solution!')

