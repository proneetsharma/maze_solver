#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 21:15:04 2018

@author: Iswariya Manivannan
"""
import sys
import os
import collections
import string
from helper import write_to_file, next_movement


def breadth_first_search(maze_map):

    # Extract information from the maze_map
    obstacle = list()
    goal = list()
    start = tuple()
    print(len(maze_map))
    print(len(maze_map[0]))

    for i in range(len(maze_map)):
        for j in range(len(maze_map[0])-1):
            if maze_map[i][j] == "|" or maze_map[i][j] == "=":
                obstacle.append((i, j))
            elif maze_map[i][j] == "*":
                goal.append((i, j))
            elif maze_map[i][j] == "s":
                start = (i, j)

    # BFS algorithm
    pose_queue = collections.deque()
    pose_queue.append(start)

    maze_dict = {}
    maze_dict[start] = None

    while pose_queue:

        parent = pose_queue.popleft()
        child = next_movement(parent)

        for i in child:
            if i not in maze_dict and i not in obstacle:
                maze_dict[i] = parent
                pose_queue.append(i)

    # Backpropagate path from the goal
    all_path = list()
    for i in goal:
        if maze_dict.get(i) != None:
            path = list()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
            k = maze_dict[i]
            while k != start:
                path.append(k)
                k = maze_dict[k]
            all_path.append(path)

    return all_path


if __name__ == '__main__':

    working_directory = os.getcwd()

    if len(sys.argv) > 1:
        map_directory = sys.argv[1]
    else:
        map_directory = 'maps'

    file_path_map1 = os.path.join(working_directory, map_directory + '/map1.txt')
    file_path_map2 = os.path.join(working_directory, map_directory + '/map2.txt')
    file_path_map3 = os.path.join(working_directory, map_directory + '/map3.txt')

    print(working_directory)
    print(map_directory)

    maze_map_map1 = []
    with open(file_path_map1) as f1:
        maze_map_map1 = f1.readlines()

    maze_map_map2 = []
    with open(file_path_map2) as f2:
        maze_map_map2 = f2.readlines()

    maze_map_map3 = []
    with open(file_path_map3) as f3:
        maze_map_map3 = f3.readlines()

    # Calling all the functions for each maze

    path_map1 = breadth_first_search(maze_map_map1)
    write_to_file("./results/bfs_map1.txt", path_map1, maze_map_map1)

    path_map2 = breadth_first_search(maze_map_map2)
    write_to_file("./results/bfs_map2.txt", path_map2, maze_map_map2)

    path_map3 = breadth_first_search(maze_map_map3)
    write_to_file("./results/bfs_map3.txt", path_map3, maze_map_map3)
