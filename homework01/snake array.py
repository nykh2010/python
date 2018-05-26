# 编写一个函数，输入参数：正整数n，如果n=4，得到下面的输出。
# 10 11 12 1
#  9 16 13 2
#  8 15 14 3
#  7  6  5 4
move = (0,0)
left = (0,-1)
right = (0,1)
down = (1,0)
up = (-1,0)
pos = [0,0]
moves = [left,right,down,up]

def put(i, array,max):
    global pos
    global move
    array[pos[0]][pos[1]] = i
    # print(array)
    if move == down:
        if pos[0]+1 >= max or array[pos[0]+1][pos[1]] != 0:
            move = left
    elif move == left:
        if pos[1]-1 < 0 or array[pos[0]][pos[1]-1] != 0:
            move = up
    elif move == up:
        if  pos[0]-1 < 0 or array[pos[0]-1][pos[1]] != 0:
            move = right
    elif move == right:
        if  pos[1]+1 >= max or array[pos[0]][pos[1]+1] != 0:
            move = down
    else:
        return
    pos[0] = pos[0] + move[0]
    pos[1] = pos[1] + move[1]
    # print(pos)
    # print(move)


def fun(n):
    array = [[0 for i in range(n)] for j in range(n)]       
    print(array)
    global pos 
    global move
    pos = [0,n-1]
    move = down
    for i in range(n*n):
        put(i+1,array,n)
    print(array)


if __name__ == '__main__':
    fun(4)