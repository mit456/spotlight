"""
Utilities for fetching the custom dataset from local filepath.
"""

import os

#import h5py
import numpy as np
import torch

from spotlight.datasets import _transport
from spotlight.interactions import Interactions

def _get_custom_dataset(dataset):
    extension = '.csv'
    URL_PREFIX = '/home/***/****/*****/********2017_05_01/'

    data = np.genfromtxt(URL_PREFIX + dataset + extension, delimiter=',', names=True, dtype=(int, int, int, int))

    user_ids = data['user_id']
    product_ids = data['product_id']
    ratings = data['product_id_total_orders']

    return (user_ids, product_ids, ratings)

def get_dataset(datafile):
    """
    Returns
    -------

    Interactions: :class:`spotlight.interactions.Interactions`
        instance of the interactions class
    """

    url = datafile

    return Interactions(*_get_custom_dataset(url))
