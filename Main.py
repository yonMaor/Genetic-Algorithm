
from individual_class import individual
from generation_class import generation
#import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.144])

#img1 = plt.imread("D:\Yonatan\Projects\Genetic Algorithm for Images\\test_image.jpg")

origin = mpimg.imread("test_image2.jpg")

#loss_type = "simple_diff"
#parenting_type = "random_genes"
#image_type = "first_gen"


origin = rgb2gray(origin)
#plt.imshow(origin)
#origin = cv2.cvtColor(origin, cv2.COLOR_BGR2GRAY)

LOSS_TYPE = "simple_diff"
PARENTING_TYPE = "random_genes"

IND_NUM_PER_GEN = 50
PARENT_RATIO = 0.2
MUT_RATE = 0.1
MAX_GEN = 1000
#gen_list = []

gen = generation(0, IND_NUM_PER_GEN, LOSS_TYPE, origin, PARENTING_TYPE, PARENT_RATIO, [], MUT_RATE)

#max_score_list = np.zeros(shape=(1, MAX_GEN))
gen.calc_generation_score()
gen.get_best_ind()
max_score_list = []
min_score_list = []
best_ind_list = []
worst_ind_list = []

max_score_list.append(gen.max_score)
min_score_list.append(gen.min_score)
best_ind_list.append(gen.max_score_ind)
worst_ind_list.append(gen.min_score_ind)

for igen in range(0, MAX_GEN):
    print(igen)
    gen.calc_generation_score()
    gen.sort_ind_list()
    gen.get_best_ind()
    gen.get_worst_ind()
    print(gen)
    plt.imshow(gen.ind_list[0].data, cmap = 'gray')
    plt.show()
#    gen_list.append(gen)
    max_score_list.append(gen.max_score)
    min_score_list.append(gen.min_score)
    best_ind_list.append(gen.max_score_ind)
    worst_ind_list.append(gen.min_score_ind)
    gen = generation(igen, IND_NUM_PER_GEN, LOSS_TYPE, origin, PARENTING_TYPE, PARENT_RATIO, gen.ind_list, MUT_RATE)
    


