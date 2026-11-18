"""Implementation of a stack application."""


class Stack:
    """A simple stack implementation."""

    def __init__(self):
        """Initialize an empty stack."""
        self._items = []

    def __len__(self):
        """Return the number of items in the stack."""
        return len(self._items)

    def __str__(self):
        return f"Stack with items: {self._items}"

    def __repr__(self):
        return f"Stack({self._items!r})"

    def push(self, item):
        """Add an item to the top of the stack."""
        self._items.append(item)

    def pop(self):
        """Remove and return the item from the top of the stack."""
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        """Return the item at the top of the stack without removing it."""
        if not self._items:
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def size(self):
        """Return the number of items in the stack."""
        return len(self._items)

