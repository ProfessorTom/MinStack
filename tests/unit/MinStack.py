import pytest

from src.MinStack.MinStack import MinStack


def test_initialization():
    minstack = MinStack()
    assert len(minstack.stack)  == 0
    assert len(minstack.lesser_list) == 0

