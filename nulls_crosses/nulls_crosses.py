# Создайте программу для игры в ""Крестики-нолики"".
import streamlit as st
import os.path
filename = 'val.csv'
def ReadValues(file):
    values = []
    fle = open(file, 'r')
    for i in fle:
        if  i != '\n':
            values.append(i.split(','))
    fle.close()
    return values
def new_game():
    fle = open('x.txt', "w")
    fle.write("")
    fle.close()
    fle = open('0.txt', "w")
    fle.write("")
    fle.close()
    fle = open('val.csv', "w")
    fle.write("")
    fle.close()

def WriteValues(file, values):
    fle = open(file, 'a')
    for i in values:
        if i.strip("\n") != '':
            fle.write(i)
            fle.write('\n')
    fle.close()


def row(): return ["|   ", "|   |", "   |"]
def init_empty(filename):

    matrix = [row(), row(), row()]
    # print(matrix)
    str = ''
    listVal = ''
    listStr = []
    fle = open(filename, 'w')
    fle.write('')
    fle.close()
    i, j = [0, 0]
    while i < len(matrix):
        j = 0
        str = ''
        listVal = ''
        while j < len(matrix[i]):
            str += matrix[i][j]
            if j == 0:
                listVal += matrix[i][j]
            else:
                listVal += ',' + matrix[i][j]
            j += 1

        listStr.append(listVal)
        #st.text(str)
        #st.text("-------------")
        i += 1
    WriteValues(filename, listStr)

    return matrix
def parse_coord(filename):
    coords = []
    fle = open(filename,'r')
    j=0
    for i in fle:
        if j == 0:
            coords = [[k.split(',')[0], k.split(',')[1]] for k in i.strip('|').split('|')]
        j+=1
        break
    fle.close()
    print(coords)
    return coords

def CheckWin(coord, player):
    if player == True:
        player = 1
    else:
        player = 2
    
    comb1 = [['0', '0'], ['0', '1'], ['0', '2']]
    comb2 = [['0', '0'], ['1', '1'], ['2', '2']]
    comb3 = [['0', '0'], ['1', '0'], ['2', '0']]
    comb4 = [['2', '0'], ['1', '1'], ['0', '2']]
    k = 0
    while k < 3:
        j = 0
        for i in coord:
            if i in map(lambda x: [str(int(x[0])+k), x[1]], comb1):
                j += 1
        if j == 3:
            return player
        j = 0
        for i in coord:
            if i in comb2:
                j += 1
        if j == 3:
            return player
        j = 0
        for i in coord:
            if i in comb4:
                j += 1
        if j == 3:
            return player
        j = 0
        for i in coord:
            if i in map(lambda x: [x[0], str(int(x[1])+k)], comb3):
                j += 1
        if j == 3:
            return player
        k += 1
    return 0


def InitField(x, y, value, matrix=[]):
    str = ''
    listVal = ''
    listStr=[]
    #st.text(listStr)
    if value == 'x':
        player = True
    else:
        player = False
    matrix = ReadValues(filename)
    #st.text(matrix)
    coord_x = open('x.txt', 'a')
    coord_null = open('0.txt','a')
    fle = open(filename, 'w')
    fle.write('')
    fle.close()
    if value == 'x':
        coord_x.write(f"{x},{y}|")
        coord_x.close()
    else:
        coord_null.write(f"{x},{y}|")
        coord_null.close()
    if y == '0':
        matrix[int(x)][int(y)] = f'| {value} '
    elif y == '1':
        matrix[int(x)][int(y)] = f'| {value} |'
    elif y == '2':
        matrix[int(x)][int(y)] = f' {value} |'
    i, j = [0, 0]
    while i < len(matrix):
        j = 0
        str = ''
        listVal = ''
        while j < len(matrix[i]):
            str += matrix[i][j]
            if j == 0:
                listVal += matrix[i][j]
            else:
                listVal += ',' + matrix[i][j]
            j += 1
        
        listStr.append(listVal.strip("\n"))
        #st.text(str)
        #st.text("-------------")
        i += 1
    
    #st.text(listStr)
    WriteValues(filename, listStr)
    if CheckWin(parse_coord(value+'.txt'),player) == 1:
        return "win x"
    elif  CheckWin(parse_coord(value+'.txt'),player) == 2:
        return "win 0"
    # WriteValues('val.csv',listVal)
    return matrix
