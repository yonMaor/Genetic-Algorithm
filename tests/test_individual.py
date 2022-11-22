import pytest
from individual_class import Individual
import numpy as np


@pytest.fixture
def size():
    return 10


@pytest.fixture
def individual_first_gen(size):
    loss_type = None
    mut_rate = 0.05
    parent1 = Individual(size, size, "first_gen", "random_genes", loss_type, mut_rate)
    parent2 = Individual(size, size, "first_gen", "random_genes", loss_type, mut_rate)
    return Individual(size, size, "first_gen", "random_genes", loss_type, mut_rate, parent1, parent2)


@pytest.fixture
def individual_any_gen(size):
    loss_type = None
    mut_rate = 0.05
    parent1 = Individual(size, size, "first_gen", "random_genes", loss_type, mut_rate)
    parent2 = Individual(size, size, "first_gen", "random_genes", loss_type, mut_rate)
    return Individual(size, size, "general", "random_genes", loss_type, mut_rate, parent1, parent2)


def test_get_individual_data_first_gen(individual_first_gen, size):
    assert np.shape(individual_first_gen.data) == (size, size)


def test_get_individual_data_from_parents(individual_any_gen, size):
    assert np.shape(individual_any_gen.data) == (size, size)


def test_individual_string_before_score(individual_first_gen):
    individual_string = individual_first_gen.__str__()
    assert individual_string == "Individual of size 10x10 with no score yet"


def test_individual_string_after_score(individual_first_gen):
    individual_first_gen.score = 1
    individual_string = individual_first_gen.__str__()
    assert individual_string == "Individual of size 10x10 with score 1"
