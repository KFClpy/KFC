import numpy
import main
import random
poke_times=numpy.zeros((4,4,13,13))
poke_score=numpy.zeros((4,4,13,13))
poke_bilv=numpy.zeros((4,4,13,13))
poke1=numpy.zeros((2,2))


poke2=numpy.zeros((2,2))
poke_board=numpy.zeros((2,5))
i=0
numpy.random.seed()
while i<=100:
    poke1[0][0] = numpy.random.randint(0, 4)
    poke1[1][0] = numpy.random.randint(0, 13)

    while 1:
        poke1[0][1] = numpy.random.randint(0, 4)
        poke1[1][1] = numpy.random.randint(0, 13)
        if poke1[0][1] == poke1[0][0] and poke1[1][1] == poke1[1][0]:
            continue
        else:
            break
    while 1:
        poke2[0][0] = numpy.random.randint(0, 4)
        poke2[1][0] = numpy.random.randint(0, 13)
        if poke1[0][1] == poke2[0][0] and poke1[1][1] == poke2[1][0]:
            continue
        if poke1[0][0] == poke2[0][0] and poke1[1][0] == poke2[1][0]:
            continue
        else:
            break
    while 1:
        poke2[0][1] = numpy.random.randint(0, 4)
        poke2[1][1] = numpy.random.randint(0, 13)
        if poke2[0][1] == poke2[0][0] and poke2[1][1] == poke2[1][0]:
            continue
        if poke1[0][1]==poke2[0][1] and poke1[1][1]==poke2[1][1]:
            continue
        if poke1[0][0] == poke2[0][1] and poke1[1][0] == poke2[1][1]:
            continue
        else:
            break
    while 1:
        poke_board[0][0] = numpy.random.randint(0, 4)
        poke_board[1][0] = numpy.random.randint(0, 13)
        if (poke_board[0][0] == poke1[0][0] and poke_board[1][0] == poke1[1][0]) or (
                poke_board[0][0] == poke1[0][1] and poke_board[1][0] == poke1[1][1]) or (
                poke_board[0][0] == poke2[0][0] and poke_board[1][0] == poke2[1][0]) or (
                poke_board[0][0] == poke2[0][1] and poke_board[1][0] == poke2[1][1]):
            continue
        else:
            break
    while 1:
        poke_board[0][1] = numpy.random.randint(0, 4)
        poke_board[1][1] = numpy.random.randint(0, 13)
        if (poke_board[0][1] == poke1[0][0] and poke_board[1][1] == poke1[1][0]) or (
                poke_board[0][1] == poke1[0][1] and poke_board[1][1] == poke1[1][1]) or (
                poke_board[0][1] == poke2[0][0] and poke_board[1][1] == poke2[1][0]) or (
                poke_board[0][1] == poke2[0][1] and poke_board[1][1] == poke2[1][1]) or (
                poke_board[0][1] == poke_board[0][0] and poke_board[1][1] == poke_board[1][0]):
            continue
        else:
            break
    while 1:
        poke_board[0][2] = numpy.random.randint(0, 4)
        poke_board[1][2] = numpy.random.randint(0, 13)
        if (poke_board[0][2] == poke1[0][0] and poke_board[1][2] == poke1[1][0]) or (
                poke_board[0][2] == poke1[0][1] and poke_board[1][2] == poke1[1][1]) or (
                poke_board[0][2] == poke2[0][0] and poke_board[1][2] == poke2[1][0]) or (
                poke_board[0][2] == poke2[0][1] and poke_board[1][2] == poke2[1][1]) or (
                poke_board[0][2] == poke_board[0][0] and poke_board[1][2] == poke_board[1][0]) or (
                poke_board[0][2] == poke_board[0][1] and poke_board[1][2] == poke_board[1][1]):
            continue
        else:
            break
    while 1:
        poke_board[0][3] = numpy.random.randint(0, 4)
        poke_board[1][3] = numpy.random.randint(0, 13)
        if (poke_board[0][3] == poke1[0][0] and poke_board[1][3] == poke1[1][0]) or (
                poke_board[0][3] == poke1[0][1] and poke_board[1][3] == poke1[1][1]) or (
                poke_board[0][3] == poke2[0][0] and poke_board[1][3] == poke2[1][0]) or (
                poke_board[0][3] == poke2[0][1] and poke_board[1][3] == poke2[1][1]) or (
                poke_board[0][3] == poke_board[0][0] and poke_board[1][3] == poke_board[1][0]) or (
                poke_board[0][3] == poke_board[0][1] and poke_board[1][3] == poke_board[1][1]) or (
                poke_board[0][3] == poke_board[0][2] and poke_board[1][3] == poke_board[1][2]):
            continue
        else:
            break
    while 1:
        poke_board[0][4] = numpy.random.randint(0, 4)
        poke_board[1][4] = numpy.random.randint(0, 13)
        if (poke_board[0][4] == poke1[0][0] and poke_board[1][4] == poke1[1][0]) or (
                poke_board[0][4] == poke1[0][1] and poke_board[1][4] == poke1[1][1]) or (
                poke_board[0][4] == poke2[0][0] and poke_board[1][4] == poke2[1][0]) or (
                poke_board[0][4] == poke2[0][1] and poke_board[1][4] == poke2[1][1]) or (
                poke_board[0][4] == poke_board[0][0] and poke_board[1][4] == poke_board[1][0]) or (
                poke_board[0][4] == poke_board[0][1] and poke_board[1][4] == poke_board[1][1]) or (
                poke_board[0][4] == poke_board[0][2] and poke_board[1][4] == poke_board[1][2]) or (
                poke_board[0][4] == poke_board[0][3] and poke_board[1][4] == poke_board[1][3]):
            continue
        else:
            break
    poke_times[int(poke1[0][0])][int(poke1[0][1])][int(poke1[1][0])][int(poke1[1][1])] += 1
    poke_times[int(poke2[0][0])][int(poke2[0][1])][int(poke2[1][0])][int(poke2[1][1])] += 1
    all_poke = poke1.T
    all_poke = numpy.concatenate((all_poke, poke_board.T))
    all_poke = all_poke.T
    print(all_poke)
    op_poke = poke2.T
    op_poke = numpy.concatenate((op_poke, poke_board.T))
    op_poke = op_poke.T
    print(op_poke)
    print(i)
    poke_max = numpy.zeros((1, 1))
    poke_max1 = numpy.zeros((1, 1))
    poke_ = main.poke_compare(all_poke, poke_max)
    max = poke_max[0][0]
    poke__ = main.poke_compare(op_poke, poke_max1)
    max1 = poke_max1[0][0]
    flag = main.player_poke_compare(poke_, poke__, max, max1)
    print(flag)
    if flag == 1:
        poke_score[int(poke1[0][0])][int(poke1[0][1])][int(poke1[1][0])][int(poke1[1][1])] += 1
    elif flag == -1:
        poke_score[int(poke2[0][0])][int(poke2[0][1])][int(poke2[1][0])][int(poke2[1][1])] += 1
    elif flag == 0:
        poke_score[int(poke1[0][0])][int(poke1[0][1])][int(poke1[1][0])][int(poke1[1][1])] += 0.5
        poke_score[int(poke2[0][0])][int(poke2[0][1])][int(poke2[1][0])][int(poke2[1][1])] += 0.5
    i+=1
file_handl=open('test.txt', mode ='w')
print("循环结束")
for i1 in range(4):
    for i2 in range(4):
        for i3 in range(13):
            for i4 in range(13):
                poke_bilv[i1][i2][i3][i4]=poke_score[i1][i2][i3][i4]/poke_times[i1][i2][i3][i4]
                file_handl.write('%s %s %s %s %s %s %s\n'%(i1,i2,i3,i4,poke_score[i1][i2][i3][i4],poke_times[i1][i2][i3][i4],poke_bilv[i1][i2][i3][i4]))


























