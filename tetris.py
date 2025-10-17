# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 09:33:51 2025

@author: rehma
"""
import random

score = 0

grid = [[".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."]]

def get_shape(index):
    shape_1 = [[".",".",".",".","X",".",".",".",".","."],
               [".",".",".",".","X",".",".",".",".","."],
               [".",".",".",".","X",".",".",".",".","."],
               [".",".",".",".","X",".",".",".",".","."]]
    shape_2 = [[".",".",".",".",".",".",".",".",".","."],
               [".",".",".",".",".",".",".",".",".","."],
               [".",".",".",".","X","X",".",".",".","."],
               [".",".",".",".","X","X",".",".",".","."]]
    shape_3 = [[".",".",".",".",".",".",".",".",".","."],
               [".",".",".",".","X",".",".",".",".","."],
               [".",".",".",".","X","X",".",".",".","."],
               [".",".",".",".",".","X",".",".",".","."]]
    shape_4 = [[".",".",".",".",".",".",".",".",".","."],
               [".",".",".",".",".",".",".",".",".","."],
               [".",".",".",".",".",".",".",".",".","."],
               [".",".",".",".","X",".",".",".",".","."]]
    shape_5 = [[".",".",".",".",".",".",".",".",".","."],
               [".",".",".",".",".",".",".",".",".","."],
               [".",".",".",".",".",".",".",".",".","."],
               [".",".",".","X","X","X","X",".",".","."]]
    shape_6 = [[".",".",".",".",".",".",".",".",".","."],
               [".",".",".",".",".",".",".",".",".","."],
               [".",".",".",".",".","X","X",".",".","."],
               [".",".",".",".","X","X",".",".",".","."]]
    shape_7 = [[".",".",".",".",".",".",".",".",".","."],
               [".",".",".",".",".","X",".",".",".","."],
               [".",".",".",".","X","X",".",".",".","."],
               [".",".",".",".","X",".",".",".",".","."]]
    shape_8 = [[".",".",".",".",".",".",".",".",".","."],
               [".",".",".",".",".",".",".",".",".","."],
               [".",".",".","X","X",".",".",".",".","."],
               [".",".",".",".","X","X",".",".",".","."]]
    
    if index == 1:
        return (shape_1,1, [3,4])
    elif index == 2:
        return (shape_2,2, [3,5])
    elif index == 3:
        return (shape_3,3, [3,5])
    elif index == 4:
        return (shape_4,4, [3,4])
    elif index == 5:
        return (shape_5,5, [3,6])
    elif index == 6:
        return (shape_6,6, [3,5])
    elif index == 7:
        return (shape_7,7, [3,4])
    elif index == 8:
        return (shape_8,8, [3,5])
    
   



while True:
    random_num = random.randint(1,8)
    shape = get_shape(random_num)[0]
    shape_case = get_shape(random_num)[1]
    cord = get_shape(random_num)[2]
        
    for i in range(len(shape)):
        grid[i] = shape[i]
    
    
    def update_cord(user_input, case):
        if case == 1:
            if user_input == "a":
                if cord[1] >= 1:
                    cord[0] += 1
                    cord[1] -= 1
                else:
                    cord[0] += 1
                
            elif user_input == "d":
                if cord[1] <= 8:
                    cord[0] += 1
                    cord[1] += 1
                else:
                    cord[0] +=1
            else:
                cord[0] += 1
                   
        elif case == 2:
            if user_input == "a":
                if cord[1] > 1:
                    cord[0] += 1
                    cord[1] -= 1
                else:
                    cord[0] += 1
                
            elif user_input == "d":
                if cord[1] <= 8:
                    cord[0] += 1
                    cord[1] += 1
                else:
                    cord[0] +=1
            else:
                cord[0] += 1
        
        elif case == 3:
            if user_input == "a":
                if cord[1] > 1:
                    cord[0] += 1
                    cord[1] -= 1
                else:
                    cord[0] += 1
                
            elif user_input == "d":
                if cord[1] <= 8:
                    cord[0] += 1
                    cord[1] += 1
                else:
                    cord[0] +=1
            else:
                cord[0] += 1
                
        elif case == 4:
            if user_input == "a":
                if cord[1] >= 1:
                    cord[0] += 1
                    cord[1] -= 1
                else:
                    cord[0] += 1
                
            elif user_input == "d":
                if cord[1] <= 8:
                    cord[0] += 1
                    cord[1] += 1
                else:
                    cord[0] +=1
            else:
                cord[0] += 1
        
        elif case == 5:
            if user_input == "a":
                if cord[1] >= 4:
                    cord[0] += 1
                    cord[1] -= 1
                else:
                    cord[0] += 1
                
            elif user_input == "d":
                if cord[1] <= 8:
                    cord[0] += 1
                    cord[1] += 1
                else:
                    cord[0] +=1
            else:
                cord[0] += 1
                
        elif case == 6:
            if user_input == "a":
                if cord[1] >= 2:
                    cord[0] += 1
                    cord[1] -= 1
                else:
                    cord[0] += 1
                
            elif user_input == "d":
                if cord[1] < 8:
                    cord[0] += 1
                    cord[1] += 1
                else:
                    cord[0] +=1
            else:
                cord[0] += 1
                
        elif case == 7:
            if user_input == "a":
                if cord[1] > 0:
                    cord[0] += 1
                    cord[1] -= 1
                else:
                    cord[0] += 1
                
            elif user_input == "d":
                if cord[1] < 8:
                    cord[0] += 1
                    cord[1] += 1
                else:
                    cord[0] +=1
            else:
                cord[0] += 1
                
        elif case == 8:
            if user_input == "a":
                if cord[1] >= 3:
                    cord[0] += 1
                    cord[1] -= 1
                else:
                    cord[0] += 1
                
            elif user_input == "d":
                if cord[1] < 9:
                    cord[0] += 1
                    cord[1] += 1
                else:
                    cord[0] +=1
            else:
                cord[0] += 1

    def move_shape(case, user_input, cord):
        if case == 1:
            if user_input == "a":
                if grid[cord[0]][0] != "X":
                    for i in range(4):
                        grid[cord[0]-i].remove(grid[cord[0]-i][cord[1]-1])
                        grid[cord[0]-i].insert(cord[1]+1,".")
            if user_input == "d":
                if grid[cord[0]][9] != "X":
                    for i in range(4):
                        if cord[1] < 9:
                            grid[cord[0]-i].pop(cord[1]+1)
                            grid[cord[0]-i].insert(cord[1],".")
    
        
        elif case == 2:
            if user_input == "a":
                if grid[cord[0]][0] != "X":
                    for i in range(2):
                        grid[cord[0]-i].remove(grid[cord[0]-i][cord[1]-2])
                        grid[cord[0]-i].insert(cord[1]+1,".")
            if user_input == "d":
                if grid[cord[0]][9] != "X":
                    for i in range(2):
                        grid[cord[0]-i].pop(cord[1]+1)
                        grid[cord[0]-i].insert(cord[1]-1,".")
        elif case == 3:
            if user_input == "a":
                if grid[(cord[0]-1)][0] != "X":
                    for i in range(3):
                        grid[cord[0]-i].remove(grid[cord[0]-i][cord[1]-2])
                        grid[cord[0]-i].insert(cord[1]+1,".")
            if user_input == "d":
                if grid[cord[0]][9] != "X":
                    for i in range(3):
                        grid[cord[0]-i].pop(cord[1]+1)
                        grid[cord[0]-i].insert(cord[1]-1,".")
                        
        elif case == 4:
            if user_input == "a":
                if grid[cord[0]][0] != "X":
                    for i in range(1):
                        grid[cord[0]-i].remove(grid[cord[0]-i][cord[1]-1])
                        grid[cord[0]-i].insert(cord[1]+1,".")
            if user_input == "d":
                if grid[cord[0]][9] != "X":
                    for i in range(1):
                        grid[cord[0]-i].pop(cord[1]+1)
                        grid[cord[0]-i].insert(cord[1],".")
            
        elif case == 5:
            if user_input == "a":
                if grid[cord[0]][0] != "X":
                    for i in range(1):
                        grid[cord[0]-i].remove(grid[cord[0]-i][cord[1]-4])
                        grid[cord[0]-i].insert(cord[1]+1,".")
            if user_input == "d":
                if grid[cord[0]][9] != "X":
                    for i in range(1):
                        grid[cord[0]-i].pop(cord[1]+1)
                        grid[cord[0]-i].insert(cord[1]-3,".")
                        
        elif case == 6:
             if user_input == "a":
                 if grid[cord[0]][0] != "X":
                     for i in range(2):
                         grid[cord[0]-i].remove(grid[cord[0]-i][cord[1]-2])
                         grid[cord[0]-i].insert(cord[1]+1,".")
             if user_input == "d":
                 if grid[(cord[0]-1)][9] != "X":
                     for i in range(2):
                         if i != 1:
                             grid[cord[0]-i].pop(cord[1]+1)
                             grid[cord[0]-i].insert(cord[1]-1,".")
                        
                         else:
                             grid[cord[0]-i].pop(cord[1]+2)
                             grid[cord[0]-i].insert(cord[1]-1,".")
                            
        
        elif case == 7:
             if user_input == "a":
                 if grid[cord[0]][0] != "X":
                     for i in range(3):
                         grid[cord[0]-i].remove(grid[cord[0]-i][cord[1]-1])
                         grid[cord[0]-i].insert(cord[1]+2,".")
             if user_input == "d":
                 if grid[(cord[0]-1)][9] != "X":
                     for i in range(3):
                         grid[cord[0]-i].pop(cord[1]+2)
                         grid[cord[0]-i].insert(cord[1],".")
        
        elif case == 8:
             if user_input == "a":
                 if grid[(cord[0]-1)][0] != "X":
                     for i in range(3):
                         grid[cord[0]-i].remove(grid[cord[0]-i][cord[1]-3])
                         grid[cord[0]-i].insert(cord[1]+1,".")
             if user_input == "d":
                 if grid[(cord[0])][9] != "X":
                     for i in range(3):
                         grid[cord[0]-i].pop(cord[1]+1)
                         grid[cord[0]-i].insert(cord[1]-2,".")
                
    def rotate_shape():
        pass
    
    def next_frame(case, cord):
        if case == 1:
            if cord[0] == 14:
                return True
            for i in range(5):
                if i != 4:   
                    grid[(cord[0])-i][cord[1]] = grid[cord[0]-1-i][cord[1]]
                else:
                    grid[cord[0]-i][cord[1]] = "."
        
        elif case == 2:
            if cord[0] == 14:
                return True
            for i in range(3):
                if i != 2:   
                    grid[(cord[0])-i][cord[1]-1] = grid[cord[0]-1-i][cord[1]-1]
                    grid[(cord[0])-i][cord[1]] = grid[cord[0]-1-i][cord[1]]
                    
                else:
                    grid[cord[0]-i][cord[1]-1] = "."
                    grid[cord[0]-i][cord[1]] = "."
    
        elif case == 3:
            if cord[0] == 14:
                return True
            for i in range(4):
                if i != 3:   
                    grid[(cord[0]-1)-i][cord[1]-1] = grid[cord[0]-2-i][cord[1]-1]
                    grid[(cord[0])-i][cord[1]] = grid[cord[0]-1-i][cord[1]]
                    
                else:
                    grid[cord[0]-i][cord[1]-1] = "."
                    grid[cord[0]-i+1][cord[1]] = "."
        
        elif case == 4:
            if cord[0] == 14:
                return True
            for i in range(2):
                if i != 3:   
                    grid[(cord[0]-1)-i][cord[1]-1] = grid[cord[0]-2-i][cord[1]-1]
                    grid[(cord[0])-i][cord[1]] = grid[cord[0]-1-i][cord[1]]
                    
                else:
                    grid[cord[0]-i][cord[1]-1] = "."
                    grid[cord[0]-i+1][cord[1]] = "."
                    
        elif case == 5:
            if cord[0] == 14:
                return True
            for i in range(2):
                if i != 2:   
                    grid[(cord[0])-i][cord[1]-3] = grid[cord[0]-1-i][cord[1]-3]
                    grid[(cord[0])-i][cord[1]-2] = grid[cord[0]-1-i][cord[1]-2]
                    grid[(cord[0])-i][cord[1]-1] = grid[cord[0]-1-i][cord[1]-1]
                    grid[(cord[0])-i][cord[1]] = grid[cord[0]-1-i][cord[1]]
                    
                else:
                    grid[cord[0]-i][cord[1]-1] = "."
                    grid[cord[0]-i][cord[1]] = "."
                    
        elif case == 6:
            if cord[0] == 14:
                return True
            for i in range(3):
                if i != 2:   
                   
                    
                    grid[(cord[0])-i][cord[1]-1] = grid[cord[0]-1-i][cord[1]-1]
                    grid[(cord[0])-i][cord[1]] = grid[cord[0]-1-i][cord[1]]
                    grid[(cord[0])-1-i][cord[1]+1] = grid[cord[0]-2-i][cord[1]+1]
                    
                else:
                    grid[cord[0]-i][cord[1]-1] = "."
                    grid[cord[0]-i][cord[1]] = "."
                    grid[cord[0]-i][cord[1]+1] = "."
        
        elif case == 7:
            if cord[0] == 14:
                return True
            for i in range(4):
                if i != 3:   
                    grid[(cord[0]-1)-i][cord[1]+1] = grid[cord[0]-2-i][cord[1]+1]
                    grid[(cord[0])-i][cord[1]] = grid[cord[0]-1-i][cord[1]]
                    
                else:
                    grid[cord[0]-i][cord[1]+1] = "."
                    grid[cord[0]-i+1][cord[1]] = "."
                    
        elif case == 8:
            if cord[0] == 14:
                return True
            for i in range(3):
                if i != 2:   
                   
                    
                    grid[(cord[0])-i][cord[1]-1] = grid[cord[0]-1-i][cord[1]-1]
                    grid[(cord[0])-i][cord[1]] = grid[cord[0]-1-i][cord[1]]
                    grid[(cord[0])-1-i][cord[1]-2] = grid[cord[0]-2-i][cord[1]-2]
                    
                else:
                    
                    grid[cord[0]-i][cord[1]-1] = "."
                    grid[cord[0]-i][cord[1]] = "."
                    grid[cord[0]-i][cord[1]-2] = "."
                    
    def check_score():
        for i in range(len(grid)):
            if "." not in grid[i]:
                for j in range(i,0,-1):
                    grid[j] = grid[j-1]
                global score
                score += 1
        
            
    def print_frame():   
        for i in range(13):
                print("_"*23)
                print("|"," "*6, "TETRIS", " "*5, "|")
                print("|"," "*5, f"Score:{score}", " "*5, "|")
                print("|","_"*19, "|")
                
                print("|"," ".join(grid[0]),"|")
                print("|"," ".join(grid[1]),"|")
                print("|"," ".join(grid[2]),"|")
                print("|"," ".join(grid[3]),"|")
                
                print("|"," ".join(grid[4]),"|")
                print("|"," ".join(grid[5]),"|")
                print("|"," ".join(grid[6]),"|")
                print("|"," ".join(grid[7]),"|")
                print("|"," ".join(grid[8]),"|")
                print("|"," ".join(grid[9]),"|")
                print("|"," ".join(grid[10]),"|")
                print("|"," ".join(grid[11]),"|")
                print("|"," ".join(grid[12]),"|")
                print("|"," ".join(grid[13]),"|")
                print("|", "_"*19, "|")
                print(cord)
                print(shape_case)
                
                
                
                
                
                user_input = input()
                move_shape(shape_case, user_input, cord)
                update_cord(user_input, shape_case)
                if next_frame(shape_case, cord):
                    break
    check_score()
    if score == 9:
        for i in range(len(grid)):
            grid[i] = [".",".",".",".",".",".",".",".",".","."]
        grid[5] =  [".",".",".","G","A","M","E",".",".","."] 
        grid[6] =  [".","C","O","M","P","L","E","T","E","."] 
        print("_"*23)
        print("|"," "*6, "TETRIS", " "*5, "|")
        print("|"," "*5, f"Score:{score}", " "*5, "|")
        print("|","_"*19, "|")
        
        print("|"," ".join(grid[0]),"|")
        print("|"," ".join(grid[1]),"|")
        print("|"," ".join(grid[2]),"|")
        print("|"," ".join(grid[3]),"|")
        
        print("|"," ".join(grid[4]),"|")
        print("|"," ".join(grid[5]),"|")
        print("|"," ".join(grid[6]),"|")
        print("|"," ".join(grid[7]),"|")
        print("|"," ".join(grid[8]),"|")
        print("|"," ".join(grid[9]),"|")
        print("|"," ".join(grid[10]),"|")
        print("|"," ".join(grid[11]),"|")
        print("|"," ".join(grid[12]),"|")
        print("|"," ".join(grid[13]),"|")
        print("|", "_"*19, "|")
        break
                
    print_frame()

