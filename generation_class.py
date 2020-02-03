from individual_class import individual
import numpy as np

class generation:
    
    def __init__(self, gen_num, NUM_OF_IND, LOSS_TYPE, original_image, PARENTING_TYPE, PARENT_RATIO, prev_gen_ind_list, mut_rate):
        self.NUM_OF_IND = NUM_OF_IND
        self.PARENTING_TYPE = PARENTING_TYPE
        self.LOSS_TYPE = LOSS_TYPE
        self.PARENT_RATIO = PARENT_RATIO
        self.mut_rate = mut_rate
        self.original_image = original_image
        self.gen_num = gen_num
        self.max_score_ind = None
        self.max_score = 0
        self.median_score_ind = None
        self.min_score_ind = None
        self.min_score = 0
        self.ind_list = []
        for iind in range(0, self.NUM_OF_IND):
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
        specimen = individual(size_x, size_y, image_type, self.PARENTING_TYPE, self.LOSS_TYPE, self.mut_rate, parent1, parent2)
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
        for iind in range(0, self.NUM_OF_IND):
            self.ind_list[iind].calc_score(self.original_image, self.LOSS_TYPE)
            
    ###########################################################################
    # Sorts the individuals list in this generation according to their score
    ###########################################################################      
    def sort_ind_list(self):
        self.ind_list.sort(key=lambda ind: ind.score)         
        
    ###########################################################################
    # Randomly chooses the two parents for the individual that is about ot be created
    ###########################################################################          
    def choose_parents(self, prev_gen_ind_list):
        parent1_ind = 0
        parent2_ind = 0
        
        while parent1_ind == parent2_ind: 
            parent1_ind = np.random.randint(0, self.NUM_OF_IND*self.PARENT_RATIO)
            parent2_ind = np.random.randint(0, self.NUM_OF_IND*self.PARENT_RATIO)
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