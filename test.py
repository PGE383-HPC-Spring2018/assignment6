#/usr/bin/env python

import os

def test_lla():

    with open('lla.txt', 'r') as f:

        first_line = f.readline()
        split_line = first_line.rstrip().split()
        
        assert split_line[0] == 'alias'
        assert split_line[1] == "lla='ls"
        assert split_line[2] == "-la'"

def test_conda_in_path():

    path_var = os.environ['PATH']
    path_list = path_var.split(':')
    assert '/home/ubuntu/miniconda3/bin' in path_list


