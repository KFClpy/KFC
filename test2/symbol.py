def symbol(pokelist,pokeboard):
    i=0
    pokeNow1=""
    if pokelist[0][0] == 0:
        pokeNow1 = pokeNow1 + "黑桃"
    elif pokelist[0][0] == 1:
        pokeNow1 = pokeNow1 + "梅花"
    elif pokelist[0][0] == 2:
        pokeNow1 = pokeNow1 + "红桃"
    elif pokelist[0][0] == 3:
        pokeNow1 = pokeNow1 + "方片"
    if pokelist[1][0] == 0:
        pokeNow1 = pokeNow1 + "2"
    elif pokelist[1][0] == 1:
        pokeNow1 = pokeNow1 + "3"
    elif pokelist[1][0] == 2:
        pokeNow1 = pokeNow1 + "4"
    elif pokelist[1][0] == 3:
        pokeNow1 = pokeNow1 + "5"
    elif pokelist[1][0] == 4:
        pokeNow1 = pokeNow1 + "6"
    elif pokelist[1][0] == 5:
        pokeNow1 = pokeNow1 + "7"
    elif pokelist[1][0] == 6:
        pokeNow1 = pokeNow1 + "8"
    elif pokelist[1][0] == 7:
        pokeNow1 = pokeNow1 + "9"
    elif pokelist[1][0] == 8:
        pokeNow1 = pokeNow1 + "10"
    elif pokelist[1][0] == 9:
        pokeNow1 = pokeNow1 + "J"
    elif pokelist[1][0] == 10:
        pokeNow1 = pokeNow1 + "Q"
    elif pokelist[1][0] == 11:
        pokeNow1 = pokeNow1 + "K"
    elif pokelist[1][0] == 12:
        pokeNow1 = pokeNow1 + "A"
    pokeNow1 = pokeNow1 + " "
    if pokelist[0][1] == 0:
        pokeNow1 = pokeNow1 + "黑桃"
    elif pokelist[0][1] == 1:
        pokeNow1 = pokeNow1 + "梅花"
    elif pokelist[0][1] == 2:
        pokeNow1 = pokeNow1 + "红桃"
    elif pokelist[0][1] == 3:
        pokeNow1 = pokeNow1 + "方片"
    if pokelist[1][1] == 0:
        pokeNow1 = pokeNow1 + "2"
    elif pokelist[1][1] == 1:
        pokeNow1 = pokeNow1 + "3"
    elif pokelist[1][1] == 2:
        pokeNow1 = pokeNow1 + "4"
    elif pokelist[1][1] == 3:
        pokeNow1 = pokeNow1 + "5"
    elif pokelist[1][1] == 4:
        pokeNow1 = pokeNow1 + "6"
    elif pokelist[1][1] == 5:
        pokeNow1 = pokeNow1 + "7"
    elif pokelist[1][1] == 6:
        pokeNow1 = pokeNow1 + "8"
    elif pokelist[1][1] == 7:
        pokeNow1 = pokeNow1 + "9"
    elif pokelist[1][1] == 8:
        pokeNow1 = pokeNow1 + "10"
    elif pokelist[1][1] == 9:
        pokeNow1 = pokeNow1 + "J"
    elif pokelist[1][1] == 10:
        pokeNow1 = pokeNow1 + "Q"
    elif pokelist[1][1] == 11:
        pokeNow1 = pokeNow1 + "K"
    elif pokelist[1][1] == 12:
        pokeNow1 = pokeNow1 + "A"
    pokeNow1 = pokeNow1 + " "
    while i<5:
        if pokeboard[0][i]==0:
            pokeNow1=pokeNow1+"黑桃"
        elif pokeboard[0][i]==1:
            pokeNow1=pokeNow1+"梅花"
        elif pokeboard[0][i]==2:
            pokeNow1=pokeNow1+"红桃"
        elif pokeboard[0][i]==3:
            pokeNow1=pokeNow1+"方片"
        if pokeboard[1][i]==0:
            pokeNow1=pokeNow1+"2"
        elif pokeboard[1][i]==1:
            pokeNow1=pokeNow1+"3"
        elif pokeboard[1][i]==2:
            pokeNow1=pokeNow1+"4"
        elif pokeboard[1][i]==3:
            pokeNow1=pokeNow1+"5"
        elif pokeboard[1][i]==4:
            pokeNow1=pokeNow1+"6"
        elif pokeboard[1][i]==5:
            pokeNow1=pokeNow1+"7"
        elif pokeboard[1][i]==6:
            pokeNow1=pokeNow1+"8"
        elif pokeboard[1][i]==7:
            pokeNow1=pokeNow1+"9"
        elif pokeboard[1][i]==8:
            pokeNow1=pokeNow1+"10"
        elif pokeboard[1][i]==9:
            pokeNow1=pokeNow1+"J"
        elif pokeboard[1][i]==10:
            pokeNow1=pokeNow1+"Q"
        elif pokeboard[1][i]==11:
            pokeNow1=pokeNow1+"K"
        elif pokeboard[1][i]==12:
            pokeNow1=pokeNow1+"A"
        pokeNow1=pokeNow1+" "
        i=i+1
    print(pokeNow1)






