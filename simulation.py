
from individual_class import individual
from generation_class import generation
#import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import logging
logging.basicConfig(filename = 'test.log', filemode = 'w', format = '%(asctime)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)

logger = logging.getLogger()

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
        logger.info(f'Updating results lists for generation number {gen.gen_num}')
        self.max_score_list.append(gen.max_score)
        self.min_score_list.append(gen.min_score)
        self.best_ind_list.append(gen.max_score_ind)
        self.worst_ind_list.append(gen.min_score_ind)

if __name__ == "__main__":
    logger.info('Starting simulation')

    loss_type = "mean_square_error_loss"
    gene_transfer_method = "random_genes"

    individuals_per_generation = 50
    ratio_of_individuals_for_next_generation = 0.1
    mutation_rate = 0.05
    max_generation_num = 1

    logger.info(f'Simulation will run with the following paramters: \n'
                f'loss type: {loss_type},\n '
                f'gene transfer method from parent to child: {gene_transfer_method},\n '
                f'individuals per generation: {individuals_per_generation}, \n'
                f'ratio of individuals for the next generation: {ratio_of_individuals_for_next_generation}, \n'
                f'mutation rate: {mutation_rate}, \n'
                f'max generation number: {max_generation_num}')

    image_name = "test_image6.jpg"
    logger.info(f'The image that will be used for this simulation is {image_name}')
    sim = Simulation(image_name,
                     loss_type,
                     gene_transfer_method,
                     individuals_per_generation,
                     ratio_of_individuals_for_next_generation,
                     mutation_rate,
                     max_generation_num)
    logger.info('Running simulation')
    sim.run_simulation()




