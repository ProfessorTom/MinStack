from collections import deque
import pytest

from src.MinStack.MinStack import MinStack
from src.MinStack.MinStackElement import MinStackElement

@pytest.mark.initailization
def test_stack_member():
    minstack = MinStack()
    assert len(minstack.stack) == 0


@pytest.mark.push
def test_single_element():
    minstack = MinStack()
    minstack.push(33)

    expected_element = MinStackElement(33, 33)

    expected = deque()
    expected.appendleft(expected_element)
    assert minstack.stack == expected


@pytest.mark.push
def test_multiple_elements():
    minstack = MinStack()
    minstack.push(64)
    minstack.push(33)
    minstack.push(99)

    expected_element_1 = MinStackElement(64, 64)
    expected_element_2 = MinStackElement(33, 33)
    expected_element_3 = MinStackElement(99, 33)

    expected = deque()
    expected.appendleft(expected_element_1)
    expected.appendleft(expected_element_2)
    expected.appendleft(expected_element_3)
    assert minstack.stack == expected


@pytest.mark.push
def test_negative_number_multiple_elements(): # sanity check
    minstack = MinStack()
    minstack.push(64)
    minstack.push(-2)
    minstack.push(99)

    expected_element_1 = MinStackElement(64, 64)
    expected_element_2 = MinStackElement(-2, -2)
    expected_element_3 = MinStackElement(99, -2)

    expected = deque()
    expected.appendleft(expected_element_1)
    expected.appendleft(expected_element_2)
    expected.appendleft(expected_element_3)
    assert minstack.stack == expected
