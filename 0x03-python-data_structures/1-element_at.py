#!/usr/bin/python3
""" retrieve an element from a list"""


def element_at(my_list, idx):
    if idx >= len(my_list):
        return None
    if idx < 0:
        return None
    return my_list[idx]
