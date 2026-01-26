"""
Project 1
CSE 331 SS26
solution.py
"""

from __future__ import annotations
from typing import List, TypeVar, Tuple, Optional

# for more information on type hinting, check out https://docs.python.org/3/library/typing.html
T = TypeVar("T")  # represents generic type
Node = TypeVar("Node")  # represents a Node object (forward-declare to use in Node __init__)
DLL = TypeVar("DLL")

# pro tip: PyCharm auto-renders docstrings (the multiline strings under each function definition)
# in its "Documentation" view when written in the format we use here. Open the "Documentation"
# view to quickly see what a function does by placing your cursor on it and using CTRL + Q.
# https://www.jetbrains.com/help/pycharm/documentation-tool-window.html


class Node:
    """
    Implementation of a doubly linked list node.
    
    DO NOT MODIFY THIS CLASS
    """
    __slots__ = ["value", "next", "prev", "child"]

    def __init__(self, value: T, next: Node = None, prev: Node = None, child: Node = None) -> None:
        """
        Construct a doubly linked list node.

        :param value: value held by the Node.
        :param next: reference to the next Node in the linked list.
        :param prev: reference to the previous Node in the linked list.
        :param child: reference used by the application problem dream_escaper.
        :return: None.

        DO NOT MODIFY
        """
        self.next = next
        self.prev = prev
        self.value = value

        # The child attribute is only used for the application problem
        self.child = child

    def __repr__(self) -> str:
        """
        Represents the Node as a string.

        :return: string representation of the Node.

        DO NOT MODIFY
        """
        return f"Node({str(self.value)})"

    __str__ = __repr__


class DLL:
    """
    Implementation of a doubly linked list without padding nodes.

    Modify only below the indicated line.
    """
    __slots__ = ["head", "tail", "size"]

    def __init__(self) -> None:
        """
        Construct an empty doubly linked list.

        :return: None.

        DO NOT MODIFY
        """
        self.head = self.tail = None
        self.size = 0

    def __repr__(self) -> str:
        """
        Represent the DLL as a string.

        :return: string representation of the DLL.

        DO NOT MODIFY
        """
        result = []
        node = self.head
        while node is not None:
            result.append(str(node))
            node = node.next
        return " <-> ".join(result)

    def __str__(self) -> str:
        """
        Represent the DLL as a string.

        :return: string representation of the DLL.

        DO NOT MODIFY
        """
        return repr(self)

    # MODIFY BELOW #

    def empty(self) -> bool:
        """
        Return boolean indicating whether DLL is empty.

        :return: True if DLL is empty, else False.
        """

        if self.head == None and self.tail == None:
            return True
        return False

    def push(self, val: T, back: bool = True) -> None:
        """
        Create Node containing `val` and add to back (or front) of DLL. Increment size by one.

        :param val: value to be added to the DLL.
        :param back: if True, add Node containing value to back (tail-end) of DLL; if False, add to front (head-end).
        :return: None.
        """

        newNode = Node(val)

        if self.size == 0:
            self.head = newNode
            self.tail = newNode

        elif back:
            self.tail.next = newNode
            newNode.prev = self.tail

            self.tail = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head

            self.head = newNode
        self.size += 1
        return None

    def pop(self, back: bool = True) -> None:
        """
        Remove Node from back (or front) of DLL. Decrement size by 1. If DLL is empty, do nothing.

        :param back: if True, remove Node from (tail-end) of DLL; if False, remove from front (head-end).
        :return: None.
        """
        if self.size == 0:
            return

        if self.size == 1:
            self.head = self.tail = None

        elif back:
            self.tail = self.tail.prev

            self.tail.next = None

        else:
            self.head = self.head.next

            self.head.prev = None

        self.size -= 1
        return None

    def list_to_dll(self, source: List[T]) -> None:
        """
        Construct DLL from a standard Python list.

        :param source: standard Python list from which to construct DLL.
        :return: None.
        """
        self.head = None
        self.tail = None
        self.size = 0

        for i in source:
            self.push(i)

        return None

    def dll_to_list(self) -> List[T]:
        """
        Construct standard Python list from DLL.

        :return: standard Python list containing values stored in DLL.
        """
        if self.size == 0:
            return []

        list = []
        node = self.head
        while (node.next != None):
            list.append(node.value)
            node = node.next
        list.append(node.value)

        return list

    def _find_nodes(self, val: T, find_first: bool = False) -> List[Node]:
        """
        Construct list of Nodes with value val in the DLL and return the associated Node list

        :param val: The value to be found
        :param find_first: If True, only return the first occurrence of val. If False, return all
        occurrences of val
        :return: A list of all the Nodes with value val.
        """

        positions = []

        if self.size == 0:
            return positions


        node = self.head
        while (node != None):
            if node.value == val:
                positions.append(node)
                if find_first:
                    return positions
            node = node.next

        return positions

    def find(self, val: T) -> Node:
        """
        Find first instance of `val` in the DLL and return associated Node object.

        :param val: value to be found in DLL.
        :return: first Node object in DLL containing `val`. If `val` does not exist in DLL, return None.
        """

        if self.size == 0:
            return None

        node = self.head
        while (node != None):
            if node.value == val:
                return node
            node = node.next

        return node

    def find_all(self, val: T) -> List[Node]:
        """
        Find all instances of `val` in DLL and return Node objects in standard Python list.

        :param val: value to be searched for in DLL.
        :return: Python list of all Node objects in DLL containing `val`. If `val` does not exist in DLL, return an empty list.
        """
        positions = []

        if self.size == 0:
            return positions

        node = self.head
        while (node != None):
            if node.value == val:
                positions.append(node)
            node = node.next

        return positions

    def remove_node(self, to_remove: Node) -> None:
        """
        Given a node in the linked list, remove it.

        :param to_remove: node to be removed from the list
        :return: None
        """
        if self.size == 0:
            return None

        if self.size == 1 and self.head == to_remove:
            self.head = self.tail = None
            del to_remove

        elif self.head == to_remove:
            to_remove.next.prev = None
            self.head = to_remove.next

        elif self.tail == to_remove:
            to_remove.prev.next = None
            self.tail = to_remove.prev

        else:
            to_remove.next.prev = to_remove.prev
            to_remove.prev.next = to_remove.next
        self.size -= 1

        return None

    def remove(self, val: T) -> bool:
        """
        Delete first instance of `val` in the DLL. Must call _remove_node.

        :param val: value to be deleted from DLL.
        :return: True if Node containing `val` was deleted from DLL; else, False.
        """
        if self.size == 0:
            return False

        node = self.head
        while (node != None):
            if node.value == val:
                self.remove_node(node)
                return True
            node = node.next
        return False

    def remove_all(self, val: T) -> int:
        """
        Delete all instances of `val` in the DLL. Must call _remove_node.

        :param val: value to be deleted from DLL.
        :return: integer indicating the number of Nodes containing `val` deleted from DLL; if no Node containing `val` exists in DLL, return 0.
        """
        count = 0
        if self.size == 0:
            return False

        node = self.head
        while (node != None):
            if node.value == val:
                self.remove_node(node)
                count += 1
            node = node.next
        return count

    def reverse(self) -> None:
        """
        Reverse DLL in-place by modifying all `next` and `prev` references of Nodes in the DLL and resetting the `head` and `tail` references.

        :return: None.
        """

        return None

def dream_escaper(dll: DLL) -> DLL:
    """
    Takes the head of a multi-level DLL and compresses it into a single level DLL.

    :param dll: The dll to turn into a single-level DLL.
    :return: The new DLL.
    """
    pass