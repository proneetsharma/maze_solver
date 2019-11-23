#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import collections
from helper import write_to_file, next_movement
sys.setrecursionlimit(4500)

# implement dls function 
def dls(maze_map, maze_dict, pose_queue, depth, end, obstacle):

        if len(pose_queue) == 0:
            return 0
        
        current = pose_queue.popleft() 

        if current == end:
            return 1
  
        if depth <= 0:
            return 0
        else:
            for i in next_movement(current):
                if i not in maze_dict and i not in obstacle:
                    maze_dict[i] = current
                    pose_queue.append(i)   
            # Recursively calling dls with one decremented depth.      
            result = dls(maze_map, maze_dict, pose_queue, depth-1, end, obstacle)
            if result == 1:
                return 1
            return 0


def iterative_deepening_depth_first_search(maze_map):

    # Extract information from the maze_map
    obstacle = list()
    goal = list()
    start = tuple()

    for i in range(len(maze_map)):
        for j in range(len(maze_map[0])-1):
            if maze_map[i][j] == "|" or maze_map[i][j] == "=":
                obstacle.append((i, j))
            elif maze_map[i][j] == "*":
                goal.append((i, j))
            elif maze_map[i][j] == "s":
                start = (i, j)

    maximum_depth = len(maze_map)*(len(maze_map[0]))
    print(len(goal))
    for i in goal:
        print(i)
        for depth in range(0, maximum_depth+1):
            maze_dict = {}
            maze_dict[start] = None

            pose_queue = collections.deque()
            pose_queue.append(start)
            result = dls(maze_map, maze_dict, pose_queue, depth, i, obstacle)
            if result == 1:
                break


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
    
    path_map1 = iterative_deepening_depth_first_search(maze_map_map1)
    write_to_file("./results/iddfs_map1.txt", path_map1, maze_map_map1)

    path_map2 = iterative_deepening_depth_first_search(maze_map_map2)
    write_to_file("./results/iddfs_map2.txt", path_map2, maze_map_map2)

    path_map3 = iterative_deepening_depth_first_search(maze_map_map3)
    write_to_file("./results/iddfs_map3.txt", path_map3, maze_map_map3)