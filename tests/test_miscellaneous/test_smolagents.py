"""Test the smolagents package."""

from typing import Literal

import pytest
from smolagents import tool


ReturnType = Literal["str", "bool"]


def dummy_function_to_be_tooled(return_type: str) -> str | bool:
    """Dummy function to be tooled.

    Args:
        return_type: ReturnType
            The type of the return value indicated as a string.

    Returns:
        The return value.
    """

    if return_type == "str":
        return "Hello, world!"
    else:
        return True


def test_tool_decorator_on_function_that_returns_union_type():
    """Test the tool decorator on a function that returns a union type."""

    with pytest.raises(TypeError):
        tool(dummy_function_to_be_tooled)


def main():
    test_tool_decorator_on_function_that_returns_union_type()
    print("All tests passed!")


if __name__ == "__main__":
    main()
