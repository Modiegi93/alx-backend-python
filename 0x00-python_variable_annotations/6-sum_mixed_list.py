#!/usr/bin/env python3
"""
Write a type-annotated function sum_mixed_list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    return sum(mxd_lst)
