
from individual_class import individual
from generation_class import generation
#import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.144])
class Simulation:
    def __init__(self,
                 image_name,
                 loss_type,
                 gene_transfer_method,
                 individuals_per_generation,
                 ratio_of_individuals_for_next_gen,
                 mutation_rate,
                 max_generation_num):

        self.image = mpimg.imread(image_name)
        self.image = rgb2gray(self.image)

        self.loss_type = loss_type
        self.gene_transfer_method = gene_transfer_method
        self.individuals_per_generation = individuals_per_generation
        self.ratio_of_individuals_for_next_gen = ratio_of_individuals_for_next_gen
        self.mutation_rate = mutation_rate
        self.max_generation_num = max_generation_num

        self.max_score_list = []
        self.min_score_list = []
        self.best_ind_list = []
        self.worst_ind_list = []

    def run_simulation(self):
        previous_generation_individual_list = []
        for iGen in range(0, self.max_generation_num):
            print(iGen)
            gen = generation(iGen,
                             self.individuals_per_generation,
                             self.loss_type,
                             self.image,
                             self.gene_transfer_method,
                             self.ratio_of_individuals_for_next_gen,
                             previous_generation_individual_list,
                             self.mutation_rate)

            gen.calc_generation_score()
            print(gen)
            self.update_result_lists(gen)
            previous_generation_individual_list = gen.ind_list

    def update_result_lists(self, gen):
        self.max_score_list.append(gen.max_score)
        self.min_score_list.append(gen.min_score)
        self.best_ind_list.append(gen.max_score_ind)
        self.worst_ind_list.append(gen.min_score_ind)




if __name__ == "__main__":
    image_name = "test_image6.jpg"
    # image = rgb2gray(image)

    LOSS_TYPE = "simple_diff"
    GENE_TRANSFER_METHOD = "random_genes"

    INDIVIDUALS_PER_GENERATION = 50
    RATIO_OF_INDIVIDUALS_FOR_NEXT_GEN = 0.1
    MUTATION_RATE = 0.05
    MAX_GENERATION_NUM = 500

    sim = Simulation(image_name,
                     LOSS_TYPE,
                     GENE_TRANSFER_METHOD,
                     INDIVIDUALS_PER_GENERATION,
                     RATIO_OF_INDIVIDUALS_FOR_NEXT_GEN,
                     MUTATION_RATE,
                     MAX_GENERATION_NUM)
    sim.run_simulation()

    # gen = generation(0, IND_NUM_PER_GEN, LOSS_TYPE, origin, PARENTING_TYPE, PARENT_RATIO, [], MUT_RATE)
    #
    # gen.calc_generation_score()
    # gen.get_best_ind()
    # max_score_list = []
    # min_score_list = []
    # best_ind_list = []
    # worst_ind_list = []
    #
    # max_score_list.append(gen.max_score)
    # min_score_list.append(gen.min_score)
    # best_ind_list.append(gen.max_score_ind)
    # worst_ind_list.append(gen.min_score_ind)
    #
    # for igen in range(0, MAX_GEN):
    #     print(igen)
    #     gen.calc_generation_score()
    #     gen.sort_ind_list()
    #     gen.get_best_ind()
    #     gen.get_worst_ind()
    #     print(gen)
    #     plt.imshow(gen.ind_list[0].data, cmap = 'gray')
    #     # plt.show()
    #     max_score_list.append(gen.max_score)
    #     min_score_list.append(gen.min_score)
    #     best_ind_list.append(gen.max_score_ind)
    #     worst_ind_list.append(gen.min_score_ind)
    #     gen = generation(igen, IND_NUM_PER_GEN, LOSS_TYPE, origin, PARENTING_TYPE, PARENT_RATIO, gen.ind_list, MUT_RATE)




