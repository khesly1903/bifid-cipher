import array 
import random

def printTable(table):
    for i in range(len(table)):
        print(f"{table[i]}")
        
def get_char(text:str) -> array.array:
    charArr = []
    for i in range(len(text)):
        charArr.append(text[i].upper())
    return charArr


def text_to_positions(text:str, table:array.array) -> array.array:
    text = get_char(text)
    positions = []
    for i in range(len(text)):
        if text[i].isalnum():
            for j in range(len(table)):           
                if text[i] in table[j]:
                    positions.append([j , table[j].index(text[i])])
                     
    return positions



def positions_to_text(text:str, positions:array.array, table:array.array) -> str:
    text_arr = []
    for i in range(len(positions)):
        text_arr.append(table[positions[i][0]][positions[i][1]])

    for i in range(len(text)):
        if not text[i].isalnum():
            text_arr.insert(i,text[i])
            
    return "".join(text_arr)
        


def bifid_encrypt(ptext:str, table:array.array) -> str:
    positions = text_to_positions(ptext, table)
    
    enc_part1 = [] #straight version
    enc_part2 = [] #diagraph version
    
    for i in range(2):
        for j in range(len(positions)):
            enc_part1.append(positions[j][i])
     
    for i in range(0,len(positions)*2,2):
        enc_part2.append([enc_part1[i],enc_part1[i+1]])
    
    return positions_to_text(ptext, enc_part2,table)
    

def bifid_decrypt(ctext:str, table:array.array) -> str:
    positions = text_to_positions(ctext, table)
    
    ij_positions = [] # positions with straight array, eg i0,i1,...,i6,j0,j1,...,j6
    for i in range(len(positions)):
        ij_positions.append(positions[i][0])
        ij_positions.append(positions[i][1])

    ptext_positions = [] # positions with digraph, eg [i0,j0],[i1,j1],...,[i6,j6]
    for i in range(len(positions)):
        ptext_positions.append([ij_positions[i],ij_positions[i+len(positions)]])
    
    return positions_to_text(ctext,ptext_positions,table)

classical_table = [
    ["A" , "B" , "C" , "D" , "E" , "F"],
    ["G" , "H" , "I" , "J" , "K" , "L"],
    ["M" , "N" , "O" , "P" , "Q" , "R"],
    ["S" , "T" , "U" , "V" , "W" , "X"],
    ["Y" , "Z" , "0" , "1" , "2" , "3"],
    ["4" , "5" , "6" , "7" , "8" , "9"]
]
 
def shuffle_table(table:array.array) -> array.array:
    shuffled_alphabet = []
    shuffled_table = []
    
    for i in range(len(table)):
        for j in range(len(table[i])):
            shuffled_alphabet.append(table[i][j])
    
    random.shuffle(shuffled_alphabet)
    
    for i in range(len(table)):
        row = []
        for j in range(len(table[i])):
            row.append(shuffled_alphabet[6*i+j]) #0,..,5 then 6,..,11 ...
        shuffled_table.append(row)
    
    
    return shuffled_table



