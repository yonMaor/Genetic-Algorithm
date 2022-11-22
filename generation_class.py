from individual_class import Individual
import numpy as np
import logging
class generation:
    
    def __init__(self, gen_num, number_of_individuals, loss_type, original_image, gene_transfer_method, ratio_of_individuals_for_next_gen, prev_gen_ind_list, mut_rate):
        logging.info(f'Creating generation number {gen_num}')
        self.gen_num = gen_num
        self.number_of_individuals = number_of_individuals
        self.gene_transfer_method = gene_transfer_method
        self.loss_type = loss_type
        self.ratio_of_individuals_for_next_gen = ratio_of_individuals_for_next_gen
        self.mut_rate = mut_rate
        self.original_image = original_image
        self.max_score_ind = None
        self.max_score = 0
        self.median_score_ind = None
        self.min_score_ind = None
        self.min_score = 0
        self.ind_list = []
        logging.info(f'Creating list of individuals for generation number {self.gen_num}')
        for iind in range(0, self.number_of_individuals):
            self.create_individual(prev_gen_ind_list)

    def __str__(self):
        return (str(self.max_score) +",  " + str(self.min_score))
    
    
    ###########################################################################
    # Creates an individual to be added to the generation's list
    ###########################################################################      
    def create_individual(self, prev_gen_ind_list):
        if self.gen_num == 0:
            image_type = "first_gen"
            parent1 = None
            parent2 = None
        else:
            image_type = "general"
            parent1, parent2 = self.choose_parents(prev_gen_ind_list)
    
        size_x, size_y = self.original_image.shape
        specimen = Individual(size_x, size_y, image_type, self.gene_transfer_method, self.loss_tpye, self.mut_rate, parent1, parent2)
        self.add_individual(specimen)
    
    ###########################################################################
    # Adds an individual to the generation
    ###########################################################################         
    def add_individual(self, specimen):
        self.ind_list.append(specimen)

    ###########################################################################
    # Calculates the loss for each individual of the generation
    ###########################################################################          
    def calc_generation_score(self):
        logging.info(f'Creating generation score for generation number {self.gen_num}')
        for iind in range(0, self.number_of_individuals):
            self.ind_list[iind].calc_score(self.original_image, self.loss_type)
        self.sort_ind_list()
        self.get_best_ind()
        self.get_worst_ind()
            
    ###########################################################################
    # Sorts the individuals list in this generation according to their score
    ###########################################################################      
    def sort_ind_list(self):
        logging.info(f'Sorting individual list according to score')
        self.ind_list.sort(key=lambda ind: ind.score)         
        
    ###########################################################################
    # Randomly chooses the two parents for the individual that is about ot be created
    ###########################################################################          
    def choose_parents(self, prev_gen_ind_list):
        parent1_ind = 0
        parent2_ind = 0
        
        while parent1_ind == parent2_ind: 
            parent1_ind = np.random.randint(0, self.number_of_individuals*self.ratio_of_individuals_for_next_gen)
            parent2_ind = np.random.randint(0, self.number_of_individuals*self.ratio_of_individuals_for_next_gen)
            parent1_ind = round(parent1_ind)
            parent2_ind = round(parent2_ind)

        return prev_gen_ind_list[parent1_ind], prev_gen_ind_list[parent2_ind] 
    
    ###########################################################################
    # Get the specimen with the highest score
    ###########################################################################      
    def get_best_ind(self):
        self.max_score_ind = self.ind_list[0] 
        self.max_score = self.ind_list[0].score
                  
    ###########################################################################
    # Get the specimen with the highest score
    ###########################################################################      
    def get_worst_ind(self):
        self.min_score_ind = self.ind_list[-1]
        self.min_score = self.ind_list[-1].score
        
    ###########################################################################
    # Get the specimen with median score
    ###########################################################################      
    def get_median_ind(self):
        self.median_score_ind = self.ind_list[round(self.ind_list.length()/2)]
        self.median_score_ind_score = self.ind_list[round(self.ind_list.length()/2)].score