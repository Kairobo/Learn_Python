#command
#python read_argv.py [[1,2],[3,4],[5,6],[7,8]]
import sys
from copy import deepcopy

#Effect: change list of string way to int number (less than 10) list
#only fix to 4
def string_list(list_str):
    points = []
    xys = 0
    ki = 0
    tmp_point = [0,0]
    tmp_num_str =
    for i in range(1,len(list_str)):
        if list_str[i] == '[':
            xys = 1
        elif list_str[i] == ']':
            xys = 0
        else:
            if xys == 1:
                tmp_point[ki] = list_str[i]
                ki = 1
            else:
                tmp_point[ki] = list_str[i]
                ki = 0
        if
        if xys == 1:
            tmp[ki] =
        try:
            num_tmp = int(list_str[i])
            if xyi == 0:
                points[ki][0] = num_tmp
                xyi = 1
            else:
                points[ki][1] = num_tmp
                xyi = 0
                ki += 1
        except:
            pass
    return points

#Effect: change list of string way to int number (less than 10) list
#only fix to 4
def string_list_one_num(list_str):
    points = [[0, 0] for i in range(4)]
    xyi = 0
    ki = 0
    for i in range(len(list_str)):
        try:
            num_tmp = int(list_str[i])
            if xyi == 0:
                points[ki][0] = num_tmp
                xyi = 1
            else:
                points[ki][1] = num_tmp
                xyi = 0
                ki += 1
        except:
            pass
    return points



argv = sys.argv
print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: ", str(sys.argv))
list = list(sys.argv[1])
points = string_list(list)
'''
#reconstruct a list
geo_points = [[0,0] for i in range(4)]
xyi = 0
ki = 0
for i in range(len(list)):
    try:
        num_tmp = int(list[i])
        if xyi == 0:
            geo_points[ki][0] = num_tmp
            xyi = 1
        else:
            geo_points[ki][1] = num_tmp
            xyi = 0
            ki += 1
    except:
        pass
'''
print(points)
