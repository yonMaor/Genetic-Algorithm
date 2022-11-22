import numpy as np


class Individual:
    def __init__(self, size_x, size_y, gen_type, parenting_type, loss_type, mut_rate, parent1=None, parent2=None):
        # TODO: remove max_color_value from here, it needs to be defined at the simulation level
        self.MAX_COLOR_VALUE = 255
        self.parenting_type = parenting_type
        self.image_type = gen_type
        self.size_x = size_x
        self.size_y = size_y
        self.parent1 = parent1
        self.parent2 = parent2
        self.score = 0
        self.mut_rate = mut_rate
        self.data = self.get_individual_data()

    def __str__(self):
        # TODO: Improve the returned string to be clearer
        return str(self.score)

    ###########################################################################
    # Creates the data for the individual (either randomly for first generation,
    # Creates the data for the individual (either randomly for first generation,
    # or from parents for subsequenct generations)
    ###########################################################################
    def get_individual_data(self):
        if self.image_type == "first_gen":
            return np.random.randint(0, 255, (self.size_x, self.size_y))
        elif self.image_type == "general":
            return self.choose_parenting_type()
        else:
            print("Error in the image type - image.get_data_from_image")

    ###########################################################################
    # Chooses the method by which data is inherited from the parents to the 
    # child
    ###########################################################################    

    def choose_parenting_type(self):
        # TODO: This needs to be its own class
        if self.parenting_type == "random_genes":
            return self.get_random_parent_genes()
        elif self.parenting_type == "average":
            return self.get_average_parent_genes()
        #        elif self.parenting_type == "random_weighted_average":
        #            return self.get_rand_weighted_average_genes()
        else:
            print("Error in parenting type - individual.choose_parenting_type")

    ###########################################################################
    # Returns child data with genes from both parent, distributed randomly
    ###########################################################################            
    def get_random_parent_genes(self):
        # TODO: break this function up
        gene = np.random.randint(1, 3, (self.size_x, self.size_y))
        data = np.zeros((self.size_x, self.size_y))
        for ix in range(0, self.size_x):
            for iy in range(0, self.size_y):
                if gene[ix, iy] == 1:
                    data[ix, iy] = self.parent1.data[ix, iy]
                else:
                    data[ix, iy] = self.parent2.data[ix, iy]
                # mut_flag = np.random.rand()
                # if mut_flag < 0.05:
                # rand_value = np.random.randint(0, self.MAX_COLOR_VALUE)
                # data[ix, iy] = rand_value
        for imut in range(0, int(self.mut_rate * 100)):
            x_to_mut = np.random.randint(0, self.size_x)
            y_to_mut = np.random.randint(0, self.size_y)
            rand_value = np.random.randint(0, self.MAX_COLOR_VALUE)
            data[x_to_mut, y_to_mut] = rand_value
        return data

    ###########################################################################
    # Returns child data with the average of genes from both parents
    # Does not appear to work well currently
    ###########################################################################       
    def get_average_parent_genes(self):
        return (self.parent1.data + self.parent2.data) / 2

    ###########################################################################
    # Decides how to calculate the loss for the individual
    ###########################################################################     
    def calc_score(self, original_image, loss_type):
        # TODO: Score calculation should be its own class
        if loss_type == "simple_diff":
            self.score = self.simple_diff_loss(original_image)
        else:
            print("Error in score calculation type - individual.calc_score")

    ###########################################################################
    # Calculates the loss with a simple least mean square
    ###########################################################################     
    def simple_diff_loss(self, original_image):
        diff = np.square((self.data - original_image) / self.MAX_COLOR_VALUE)
        return np.sum(diff) / (self.size_x * self.size_y)
