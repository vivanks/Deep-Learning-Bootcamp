#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 10:52:54 2020

@author: vivanksharma
"""


import numpy as np
import pandas as pd

admission = pd.read_csv('dataset.csv')

#Make dummy variable for rank

data = pd.concat([admission,pd.get_dummies(admission['rank'],prefix='rank')],axis=1)

# Standardise features
for field in ['gre', 'gpa']:
    mean, std = data[field].mean(), data[field].std()
    data.loc[:,field] = (data[field]-mean)/std

# Split off random 10% of the data for testing
np.random.seed(42)
sample = np.random.choice(data.index, size=int(len(data)*0.9), replace=False)
data, test_data = data[:,sample], data.drop(sample)
# Split into features and targets
features, targets = data.drop('admit', axis=1), data['admit']
features_test, targets_test = test_data.drop('admit', axis=1), test_data['admit']

