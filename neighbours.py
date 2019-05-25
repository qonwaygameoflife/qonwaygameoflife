#!/usr/bin/env python3

from collections import deque

def neighbours3(index, elements):
    actual_index = index
    actual_elements = elements
    if index == 0:
        actual_index = 1

        tmp_elements = deque(elements)
        tmp_elements.rotate(1)
        actual_elements = list(tmp_elements)
    elif index == (len(elements) - 1):
        actual_index = len(elements) - 2

        tmp_elements = deque(elements)
        tmp_elements.rotate(-1)
        actual_elements = list(tmp_elements)

    return actual_elements[(actual_index - 1):(actual_index + 2)]

def neighbours5(index, elements):
    actual_index = index
    actual_elements = elements
    if index < 2:
        actual_index = 2

        tmp_elements = deque(elements)
        tmp_elements.rotate(2 - index)
        actual_elements = list(tmp_elements)
    elif index >= (len(elements) - 2):
        actual_index = len(elements) - 3

        tmp_elements = deque(elements)
        tmp_elements.rotate(len(elements) - 1 - index - 2)
        actual_elements = list(tmp_elements)

    return actual_elements[(actual_index - 2):(actual_index + 3)]
