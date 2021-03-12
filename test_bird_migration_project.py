# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 10:19:20 2021

@author: Joe
"""

import pytest
import bird_migration_project
import pandas as pd

def test_file_load_good():
    data = pd.read_csv('arctic_loon_import.csv', sep='\t',low_memory=False)
    assert type(data) == pd.core.frame.DataFrame