import pytest

from src.MinStack.MinStack import MinStack

@pytest.mark.initailization
def test_stack_member():
    minstack = MinStack()
    assert len(minstack.stack) == 0

