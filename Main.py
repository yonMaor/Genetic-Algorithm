
from individual_class import individual
from generation_class import generation
#import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.144])

if __name__ == "__main__":
    origin = mpimg.imread("test_image6.jpg")
    origin = rgb2gray(origin)

    LOSS_TYPE = "simple_diff"
    PARENTING_TYPE = "random_genes"

    IND_NUM_PER_GEN = 100
    PARENT_RATIO = 0.1
    MUT_RATE = 0.05
    MAX_GEN = 2000

    gen = generation(0, IND_NUM_PER_GEN, LOSS_TYPE, origin, PARENTING_TYPE, PARENT_RATIO, [], MUT_RATE)

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
        # plt.show()
        max_score_list.append(gen.max_score)
        min_score_list.append(gen.min_score)
        best_ind_list.append(gen.max_score_ind)
        worst_ind_list.append(gen.min_score_ind)
        gen = generation(igen, IND_NUM_PER_GEN, LOSS_TYPE, origin, PARENTING_TYPE, PARENT_RATIO, gen.ind_list, MUT_RATE)

    print("Hello")



