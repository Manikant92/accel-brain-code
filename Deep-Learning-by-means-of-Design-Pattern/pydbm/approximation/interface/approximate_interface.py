#!/user/bin/env python
# -*- coding: utf-8 -*-
import pyximport; pyximport.install()
from abc import ABCMeta, abstractmethod


class ApproximateInterface(metaclass=ABCMeta):
    '''
    The interface for function approximations.
    '''

    @abstractmethod
    def approximate_learn(self, graph, double learning_rate, observed_data_matrix, int traning_count=1000):
        '''
        learning with function approximation.

        Args:
            graph:                Graph of neurons.
            learning_rate:        Learning rate.
            observed_data_matrix: observed data points.
            traning_count:        Training counts.
        Returns:
            Graph of neurons.
        '''
        raise NotImplementedError()
