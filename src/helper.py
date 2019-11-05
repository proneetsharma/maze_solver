#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 01:36:01 2018

@author: Iswariya Manivannan
"""

# import sys
# import os
# import time
import collections
import string
import copy


def next_movement(position):
    x, y = position
    next_pos = [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]

    return next_pos


def write_to_file(file_name, all_path, maze_map):
    """Function to write output to console and the optimal path
    from start to each goal to txt file.
    Please ensure that it should ALSO be possible to visualize each and every
    step of the tree traversal algorithm in the map in the console.
    This enables understanding towards the working of your
    tree traversal algorithm as to how it reaches the goals.

    Parameters
    ----------
    filen_name : string
        This parameter defines the name of the txt file.
    path : [type]
        [description]

    """

    out = list()
    for i in range(len(maze_map)):
        a = list()
        for j in range(len(maze_map[0])-1):    
            a.append(maze_map[i][j])
        out.append(a)

    f = open(file_name, "w+")
    for path in all_path:
        maze_path = copy.deepcopy(out)
        for i in path:
            x, y = i
            maze_path[x][y] = "+"
        for i in maze_path:
            n = "".join(i)
            print(n)
            f.write(n)
            f.write("\n")
    f.close()
