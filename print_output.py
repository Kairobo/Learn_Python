from copy import deepcopy

#Effect:get two list of points and pass it to a list of dict
def two_list_to_dict_list(a,b):
    dict_l = []
    num_polygon = len(b)
    first_name = 'polygon_indexes'
    second_name = 'area_ratios'
    for i in range(num_polygon):
        tmp_dict = {}
        tmp_dict[first_name] = deepcopy(a[i])
        tmp_dict[second_name] = deepcopy(b[i])
        dict_l.append(tmp_dict)
    return dict_l

a = [[[1,1],[2,2]],[[3,3],[4,4],[5,5]]]
b = [0.5,1]

dict_l = two_list_to_dict_list(a,b)

print(dict_l)
'''
dict_l = []
tmp_d = dict()
tmp_d['a'] = deepcopy(a[0])
tmp_d['b'] = deepcopy(b[0])
dict_l.append(tmp_d)
tmp_d = dict()
tmp_d['a'] = deepcopy(a[1])
tmp_d['b'] = deepcopy(b[1])
dict_l.append(tmp_d)
print(dict_l)
'''