from copy import deepcopy
import numpy as np

def vector_norm(vec):
    return np.sqrt(np.power(vec[0],2)+np.power(vec[1],2))

def vector_divide(vec,divider=1):
    assert(len(vec)==2)
    vec_new = deepcopy(vec)
    vec_new[0] = vec_new[0]/divider
    vec_new[1] = vec_new[1]/divider
    return vec_new

def vector_add(add_list):

    vec_new = [0,0]
    if len(add_list) == 0:
        return vec_new
    for i in range(len(add_list)):
        vec_new[0] = vec_new[0] + add_list[i][0]
        vec_new[1] = vec_new[1] + add_list[i][1]
    return vec_new

def vector_subtract_2(sub_list):

    vec_new = [0,0]
    assert len(sub_list) == 2


    vec_new[0] = sub_list[0][0] - sub_list[1][0]
    vec_new[1] = sub_list[0][1] - sub_list[1][1]
    return vec_new



#Effect: given four geo_points locations and their pixel locations
#and a list of polygon positions, transfer the four polygon_locations as geo_points
#Require:
#the sequence of the geo_locations is corresponding to the pix_locations
# 1     2
#
# 4     3
def polygon_pix2geo(polygon_indexes,pix_locations,geo_locations):
    polygon_new = deepcopy(polygon_indexes)
    num_points = len(polygon_indexes)
    gO_0 = geo_locations[3]
    #4->1
    tmp_sub_list = [geo_locations[3],geo_locations[0]]
    gx_0 = vector_subtract_2(tmp_sub_list)
    gx_0_norm = vector_norm(gx_0)
    # 4->3
    tmp_sub_list = [geo_locations[3],geo_locations[2]]
    gy_0 = vector_subtract_2(tmp_sub_list)
    gy_0_norm = vector_norm(gy_0)
    for i in range(num_points):
        tmp_add_list = []
        tmp_add_list.append(O_0)
        tmp_add_list.append()


    return polygon_new

pix_locations =[[10,10],[10,240],[240,240],[240,10]]
geo_locations = [[99,3],[100,3],[100,4],[99,4]]#la,long
polygon_indexes = [[0,0],[100,50],[30,70]]

polygon_new = polygon_pix2geo(polygon_indexes=polygon_indexes,pix_locations=pix_locations,geo_locations=geo_locations)
print(polygon_new)

