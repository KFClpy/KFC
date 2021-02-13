import numpy
def judgeDuplicated_NUM(num_list):
    count=0
    Duplicated_NUM=0
    while count<len(num_list[1])-1:
        if num_list[1][count]==num_list[1][count+1]:
            Duplicated_NUM+=1
        count+=1
    return Duplicated_NUM
def judgeThree(num_list):
    count=0
    Duplicated_NUM=0
    while count<len(num_list[1])-2:
        if num_list[1][count]==num_list[1][count+1] and num_list[1][count+1]==num_list[1][count+2]:
            return True
        else:
            count+=1
    return False
def judgeThree_r(num_list):
    count=0
    while count<len(num_list[1])-2:
        if num_list[1][count]==num_list[1][count+1] and num_list[1][count+1]==num_list[1][count+2]:
            return num_list[1][count]
        count+=1
    else:
        return 0
def judgeDoubleandThree(num_list):
    count=0
    while count<len(num_list[1])-1:
        if num_list[1][count]==judgeThree_r(num_list):
            count+=1
            continue
        if num_list[1][count]==num_list[1][count+1]:
            return True
        count+=1
    else:
        return False
def judgeDoubleandThree_max(num_list):
    count=0
    max=num_list[1][0]
    while count<len(num_list[1])-2:
        if num_list[1][count] == num_list[1][count + 1] and num_list[1][count + 1] == num_list[1][count + 2]:
            max=num_list[1][count]
        count+=1
    count=0
    while count<len(num_list[1])-1:
        if num_list[1][count]==judgeThree_r(num_list):
            break
        if num_list[1][count]==num_list[1][count+1]:
            max=num_list[1][count]
        count+=1
    return max
def judge_num_connect(num_list):
    count=0
    while count<len(num_list[1])-4:
        if num_list[1][count]==num_list[1][count+1]+1 and num_list[1][count+1]==num_list[1][count+2]+1 and num_list[1][count+2]==num_list[1][count+3]+1 and num_list[1][count+3]==num_list[1][count+4]+1 :
            return True
        count+=1
    else :
        return False
def judge_num_connect_max(num_list):
    count=0
    max=num_list[1][0]
    while count<len(num_list[1])-4:
        if num_list[1][count] == num_list[1][count + 1] + 1 and num_list[1][count + 1] == num_list[1][count + 2] + 1 and num_list[1][count + 2] == num_list[1][count + 3] + 1 and num_list[1][count + 3] == num_list[1][count + 4] + 1:
            max=num_list[1][count]
        count+=1
    return max
def judgepoke_colorsame(num_list):
    count=0
    num1_list=num_list.T[numpy.lexsort(num_list[::-1,:])].T
    while count<len(num1_list[1])-4:
        if num1_list[0][count]==num1_list[0][count+1] and num1_list[0][count+1]==num1_list[0][count+2] and num1_list[0][count+2]==num1_list[0][count+3] and num1_list[0][count+3]==num1_list[0][count+4]:
            return True
        count+=1
    else :
        return False
def judgepoke_colorsame_max(num_list):
    count=0
    num1_list = num_list.T[numpy.lexsort(num_list[::-1, :])].T
    max=num_list[1][0]
    while count < len(num_list[1]) - 4:
        if num1_list[0][count] == num1_list[0][count + 1] and num1_list[0][count + 1] == num1_list[0][count + 2] and num1_list[0][count + 2] == num1_list[0][count + 3] and num1_list[0][count + 3] == num1_list[0][count + 4]:
           max=num_list[1][count]
           count1=count
           while count1<=count+4:
               if num1_list[1][count1]>max:
                   max=num1_list[1][count1]
               count1+=1

        count+=1
    return max
def judge_Four(num_list):
    count=0
    while count<len(num_list[1])-3:
        if num_list[1][count]==num_list[1][count+1] and num_list[1][count+1]==num_list[1][count+2] and num_list[1][count+2]==num_list[1][count+3]:
            return True
        count+=1
    else:
        return False

def poke_compare(num_list,poke_max):
    num_list=num_list.T[numpy.lexsort(-num_list)].T
    poke=1
    max=num_list[1][0]
    poke_max[0][0]=num_list[1][0]
    if judgeDuplicated_NUM(num_list)==1:
        poke=2
    if judgeDuplicated_NUM(num_list)==2:
        poke=3
    if judgeThree(num_list):
        poke=4
    if judge_num_connect(num_list):
        poke=5
        max=judge_num_connect_max(num_list)
    if judgepoke_colorsame(num_list):
        poke=6
        max=judgepoke_colorsame_max(num_list)
    if judgeThree(num_list):
        if judgeDoubleandThree(num_list):
            poke=7
            max=judgeDoubleandThree_max(num_list)
    if judge_Four(num_list):
        poke=8
    if judge_num_connect(num_list) and judgepoke_colorsame(num_list):
        poke=9
        max = judge_num_connect_max(num_list)
    poke_max[0][0]=max
    return poke
def player_poke_compare(player1,player2,max1,max2):
    if player1>player2:
        return 1
    if player2>player1:
        return -1
    if player1==player2:
        if max1>max2:
            return 1
        if max1<max2:
            return -1
        if max1==max2:
            return 0
#方片1 梅花2 红桃3 黑桃4
if __name__=='__main__':
    num_list=numpy.zeros((2,7))
    poke_max=numpy.zeros((1,1))
    num_list1=numpy.zeros((2,7))
    poke_max1=numpy.zeros((1,1))
    for i in range(2):
        for j in range(7):
            num_list[i][j]=int(input())
    for i in range(2):
        for j in range(7):
            num_list[i][j]=int(input())
    poke=poke_compare(num_list,poke_max)
    max=poke_max[0][0]
    poke1=poke_compare(num_list1,poke_max1)
    max1=poke_max1[0][0]
    flag=player_poke_compare(poke,poke1,max,max1)
    print(flag)





















