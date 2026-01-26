# Project 1: Doubly Linked Lists

**Due: Monday, January 12th at 9:00 PM EST**

_This is not a team project. Do not copy someone else’s work._

# Assignment Overview

Doubly linked lists (DLLs) are a fundamental data structure used to store sequential information. DLLs consist of a chain of _nodes_ linked to one another by _forward_ and _backward_ references, such that one may traverse the chain from the _head_ to the _tail_, or vice-versa. Each node stores a _value_, which may be a number, string, or more complex object.

![](img/basic_DLL.png)

Traditional _arrays_ provide a simpler means for storing sequential information, but come with a major drawback which DLLs avoid: arrays require contiguous blocks of memory, while DLLs may utilize memory wherever it is available. In settings where data is updated, manipulated or deleted frequently, DLLs outperform traditional arrays by avoiding the need for memory reallocation. [This article](https://www.geeksforgeeks.org/linked-list-vs-array/) gives a nice overview of the distinction between DLLs and arrays.

Also see Zybooks Chapter 20 if you need further review of DLL.

# Assignment Notes

1. Each method/function specifies both **time** and **space complexity**; be sure to follow these specifications, as they are important for project quizzes and exams.
2. **Testcases** are your friend: before asking about the form of input/output or what happens in a particular edge case, check to see if the test cases answer your question for you. By showing the expected output in response to each input, they supplement the specs provided here.
3. Don't be afraid to go to D2L Course Tools for tutorial videos on how to debug, it will help you figure out where you're going wrong far more quickly than ad-hoc print statements!
4. Throughout the specs, we mention Python double-underscore "magic" methods. These are central to the structure of object-oriented programming in Python, and will continue to appear in future projects in CSE 331 and beyond. [This page](https://rszalski.github.io/magicmethods/) is a great reference if you'd like to learn more about how they work!
5. There are two functions which may seem a little odd to you _\_find_nodes_ and remove_node. These functions are intended as helper functions to help you reuse code and allow you to practice writing modular code.
6. We **strongly** encourage you to avoid calling `remove` in `remove_all`. Why? It's far less efficient to repeatedly call `remove`, as each call to remove begins searching at the beginning of the list. In the worst case, this will lead our function to operate with O(n^2) time complexity, **violating the required time complexity.**
7. In the testcases for this project, you will notice the use of assertEqual and assertIs. What's the difference? It ties back to the difference between == and is in Python. The double-equal sign compares _values_ in Python, while the is operator compares _memory addresses_ in Python. Put simply, the is keyword is stronger than ==: if two objects are at the same memory address, they must contain the same value. However, it is possible for two objects _not_ at the same memory address to have the same value. In other words, if a is b then we know a == b as well, but if a == b we cannot conclude a is b. A great read on the subject is [available here](https://realpython.com/courses/python-is-identity-vs-equality/).

### **Auxiliary Space Complexity: An Overview**

Auxiliary space complexity refers to the amount of additional space, aside from the input, that an algorithm or a method requires to execute. This is especially important when evaluating the efficiency of algorithms. It's different from the space complexity in that it doesn't consider the space required by the inputs; instead, it looks only at the extra space (temporary space) taken up, typically for variables, temporary structures, etc.


# Assignment Specifications

**class Node:**

A class that implements the nodes to be created for a DLL.

_DO NOT MODIFY the following attributes/functions_

- **Attributes**
  - **value: T:** Value held by the Node. Note that this may be any type, such as a str, int, float, dict, or a more complex object.
  - **next: Node:** Reference to the next Node in the linked list (may be None).
  - **prev: Node:** Reference to the previous Node in the linked list (may be None).
  - **child: Node:** Reference to the child Node of this Node. Note: this will only be used for the application problem, you should not be using the child member in any of your functions aside from the application problem.
- **\_\_init\_\_(self, value: T, next: Node = None, prev: Node = None, child: Node = None) -> None**
  - Constructs a doubly linked list node.
  - **value: T:** Value held by the Node.
  - **next: Node:** Reference to the next Node in the linked list (may be None).
  - **prev: Node:** Reference to the previous Node in the linked list (may be None).
  - **Returns:** None.
- **\_\_str\_\_(self) -> str** and **\_\_repr\_\_(self) -> str**
  - Represents the Node as a string.
  - Note that Python will automatically invoke this function when using printing a Node to the console, and PyCharm will automatically invoke this function when displaying a Node in the debugger.
  - As with all double-underscore "magic" methods in Python (see note 5), this function may be called with str(node) or repr(node). It is not necessary (and stylistically improper) to use node.\_\_str\_\_() or node.\_\_repr\_\_(), just as it is preferable to call len(some_list) instead of some_list.\_\_len\_\_().
  - **Returns:** str.

**class DLL:**

A class that implements the doubly linked list with previous and forward references.

_DO NOT MODIFY the following attributes/functions_

- **Attributes**
  - **head: Node:** Head (first node) of the doubly linked list (may be None).
  - **tail: Node:** Tail (last node) of the doubly linked list (may be None).
  - **size: int:** Number of nodes in the doubly linked list.
  - Note that the implementation in this project does not use a [sentinel node](https://en.wikipedia.org/wiki/Sentinel_node). As such, an empty DLL will have head and tail attributes which are None.
- **\_\_init\_\_(self) -> None**
  - Construct an empty DLL. Initialize the head and tail to None, and set the size to zero.
  - **Returns:** None.
- **\_\_str\_\_(self) -> str** and **\_\_repr\_\_(self) -> str**
  - Represents the DLL as a string of the form "value <-> value <-> ... <-> value."
  - Note that Python will automatically invoke this function when printing a DLL to the console, and PyCharm will automatically invoke this function when displaying a DLL in the debugger.
  - As with all double-underscore "magic" methods in Python (see note 5), this function may be called with str(dll) or repr(dll). It is not necessary (and stylistically improper) to use dll.\_\_str\_\_() or dll.\_\_repr\_\_(), just as it is preferable to call len(some_list) instead of some_list.\_\_len\_\_().
  - **Returns:** str.

*IMPLEMENT the following functions*

- **empty(self) -> bool**
  - Returns a boolean indicating whether the DLL is empty.
  - _Required time complexity:_ O(1).
  - _Required space complexity:_ O(1).
  - **Returns:** True if DLL is empty, else False.
  - Since this method is simply checking if the doubly linked list (DLL) is empty (likely by verifying if the head of the list is `None` or if the size of the list is 0), its space complexity is O(1). 
- **push(self, val: T, back: bool = True) -> None**
  - Adds a Node containing val to the back (or front) of the DLL and updates size accordingly.
  - _Required time complexity:_ O(1).
  - _Required space complexity:_ O(1).
  - **val: T:** Value to be added to the DLL.
  - **back: bool:** If True, add val to the back of the DLL. If False, add to the front. Note that the default value is True.
  - **Returns:** None.
  - The act of pushing a value onto a DLL involves creating a new node and adjusting a couple of pointers (previous and next). It doesn't matter how long the DLL is; the process of adding a node requires a fixed amount of space. Hence, its space complexity remains `O(1)`.
- **pop(self, back: bool = True) -> None**
  - Removes a Node from the back (or front) of the DLL and updates size accordingly.
  - In the case that the DLL is empty, pop does nothing.
  - _Required time complexity:_ O(1).
  - _Required space complexity:_ O(1).
  - **back: bool:** If True, remove from the back of the DLL. If False, remove from the front. Note that the default value is True.
  - **Returns:** None.
  - Popping a value from the DLL involves adjusting pointers and, in some implementations, deallocating the node's memory. Like the push method, the space it requires doesn't depend on the size of the DLL. Therefore, its space complexity is `O(1)`.
- **list_to_dll(self, source: list[T]) -> None**
  - Creates a DLL from a standard Python list. If there are already nodes in the DLL, the DLL should be cleared and replaced by **source**.
  - Hint: clearing the DLL can be very simple. Think about what an empty DLL looks like (what are the values of head and tail?).
  - _Required time complexity:_ O(n).
  - _Required space complexity:_ O(n).
  - **source: list[T]:** Standard Python list from which to construct DLL.
  - **Returns:** None.
  - When transforming a standard Python list into a DLL, the method will likely iterate over each item in the source list and create a new node in the DLL. The number of nodes created will be proportional to the size of the source list. Thus, in the worst-case scenario, if the source list contains 'n' elements, the method will require space for 'n' nodes. Hence, its space complexity is `O(n)`, meaning it requires linear space relative to the size of the input list.
- **dll_to_list(self) -> list[T]**
  - Creates a standard Python list from a DLL.
  - _Required time complexity:_ O(n).
  - _Required space complexity:_ O(n).
  - **Returns:** list[T] containing the values of the nodes in the DLL.
- **\_find_nodes(self, val: T, find_first: bool =False) -> List[Node]:**
  - Construct list of Node with value val in the DLL and returns the associated Node object list
  - _Required time complexity:_ O(n).
  - _Required space complexity:_ O(n).
  - MUST BE CALLED FROM find AND find_all
    - If find and find_all do not call \_find_nodes, **all testcase and manual points** for find and find_all will be forfeited.
  - Will not be tested explicitly
    - Tests for find and find_all will ensure functionality
  - **val: T:** Value to be found in the DLL.
  - **find_first: bool:** if True find only the first element in the DLL, it false find all instances of the elements in the DLL.
  - **Returns:** list of Node objects in the DLL whose value is val. If val does not exist in the DLL, returns empty list.
- **find(self, val: T) -> Node**
  - Finds first Node with value val in the DLL and returns the associated Node object.
  - _Requires call to_ \_find_nodes
    - Failure to call \_find_nodes will result in **all testcase and manual points** being forfeited for find.
  - _Required time complexity:_ O(n).
  - _Required space complexity:_ O(n).
  - **val: T:** Value to be found in the DLL.
  - **Returns:** first Node object in the DLL whose value is val. If val does not exist in the DLL, return None.
- **find_all(self, val: T) -> list[Node]**
  - Finds all Node objects with value val in the DLL and returns a standard Python list of the associated Node objects.
  - _Requires call to_ `_find_nodes`
    - Failure to call `_find_nodes` will result in **all testcase and manual points** being forfeited for find_all.
  - _Required time complexity:_ O(n).
  - _Required space complexity:_ O(n).
  - **val: T:** Value to be found in the DLL.
  - **Returns:** standard Python list of all Node objects in the DLL whose value is val. If val does not exist in the DLL, returns an empty list.
- **remove_node(self, to_remove: Node) -> None**
  - Given a reference to a node in the linked list, remove it
  - MUST BE CALLED FROM `remove` AND `remove_all`
  - Will not be tested explicitly
    - Tests for remove and remove_all will ensure functionality
  - _Required time complexity:_ O(1).
  - _Required space complexity:_ O(1).
  - **to_remove: Node:** Node to be removed from the DLL.
  - **Returns:** None.
- **remove(self, val: T) -> bool**
  - removes first Node with value val in the DLL.
  - MUST CALL `remove_node`
    - Failure to call `remove_node` will result in **all testcase and manual points** being forfeited for remove.
  - Hint
    - Use of `find` allows this to be implemented in less than 10 lines.
  - _Required time complexity:_ O(n).
  - _Required space complexity:_ O(1).
  - **val: T:** Value to be removed from the DLL.
  - **Returns:** True if a Node with value val was found and removed from the DLL, else False.
- **remove_all(self, val: T) -> int**
  - removes all Node objects with value val in the DLL. See note 7.
  - MUST CALL `remove_node`
    - Failure to call `remove_node` will result in **all testcase and manual points** being forfeited for remove_all.
  - Hint
    - Use of `find_all` allows this to be implemented in less than 10 lines.
  - _Required time complexity:_ O(n).
  - _Required space complexity:_ O(n).
  - **val: T:** Value to be removed from the DLL.
  - **Returns:** number of Node objects with value val removed from the DLL. If no node containing val exists in the DLL, returns 0.
- **reverse(self) -> None**
  - Reverses the DLL in-place by modifying all next and prev references of Node objects in DLL. Updates self.head and self.tail accordingly. See note 8.
  - _Required time complexity:_ O(n).
  - _Required space complexity:_ O(1).
  - **Returns:** None.

# Application Problem: Dream Escaper
![inception](./img/inception-deeper.gif)

You have made millions of dollars as a highly-skilled "extractor" - someone who specializes in stealing juicy corporate secrets straight from the dreams of their targets.

However, the jig is up; some of your would-be victims have started to prepare for your attacks. They try to trap you in their subconscious forever by creating dreams within dreams or **dreamceptions**.
After a few narrow escapes from these newly bolstered defenses, you decide to deploy your 331 skills to take matters into your own hands. You realize that you can represent these dreamceptions with a **multilevel DLL**.

Thus, you decide to build an algorithm called `dream_escaper`. This algorithm will transform a multilevel DLL full of malicious dreamceptions into a single-level DLL that is much easier to escape from!


## Multilevel DLL Description
Each node in the multilevel DLL has an extra data member named child. Everything in the child’s DLL should occur after the current `node` but before current `node.next`. 

A small aside:
Though a multi-level structure seems odd, there are actually applications of this structure in the popular Pandas data science library. The Pandas library supports a multi-index structure that is structured in this way. If you would like to learn more, check out the links [here](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html) and [here](https://datascientyst.com/flatten-multiindex-in-pandas/).

**Multi-level Input**

![](img/Multilevel_DLL.png)


**Single-level Output**

![](img/Single_level_DLL.png)

**Explanation**
- A is the first node in multi so it will also be first in single level
- A has no children so B is A's next
- B has children so those are brought up to be B's next
- J has no children so it's next would be B's next, C
- C has a child so E becomes C's next
- E has no child so E's next stays the same, F
- F has a child so it's next becomes F's Next
- H has no next and no child so H's next is F's next
- G's has no next and no child so it's next is D
- Compiling this gives you the single level DLL above

## Function Description
Let's summarize:

- **dream\_escaper (dll: DLL) -> DLL**
  - Turns a multilevel dll into a single level dll
  - Child nodes are placed after the `parent` node but before the `parent.next` node in the final DLL.
  - *Required time complexity:* O(n).
  - *Auxiliary space complexity:* O(n).
  - **dll: DLL:** A DLL where each Node holds a value of str where the string is the task. The Node may also hold a child in `.child` and store the child DLL to the current node.
  - **Returns:** a DLL holding str representing the names of all of the tasks
  - Notes:
    - **IMPORTANT:** if your solution contains any hard-coding of the number of levels in the DLL, you will automatically lose all points for this section.  
    - If the DLL is empty, return an empty DLL.
    - When `node.child` is `None` it means there is no child DLL
    - All child values should be `None` in the DLL that is returned
    

**Example 1**

```
Input
A - B - C - D
    |   |
    E   F
    

Output
A - B - E - C - F - D
```

- **Explanation:**
  - A is the first node in the input  so it is the first in the output
  - A has no children so it is followed by its next, B.
  - B has a child DLL so nodes from that are inserted next, E.
  - All of B’s child’s are finished so it goes to B’s next, C
  - C has a child DLL so nodes from that are inserted next, F.
  - All of C’s child’s are finished so it goes to C’s next, D
  - Compiling the nodes into a DLL gives us the desired result.

**Example 2**
```
Input
A - B - C
|       | 
E - F   G
        |
        H
Output
A - E - F - B - C - G - H
```

- **Explanation:**
  - A is the first node in the input so it is the first in the output
  - A has 2 children so they will be placed before B
  - E is first in A’s child DLL so it is placed first
  - E has no children so its next is placed into the output, F
  - F is the last element in the child DLL and has no children so A’s Next is placed in the output, B
  - B has no child DLL so it's next is C
  - C has child DLL with start of G so G is placed in output
  - G has child DLL beginning with H so H is placed in output
  - Compiling the nodes into a DLL gives us the desired result.

**Example 3**
```
Input
A - B - C
    |
    D - F
    |   |
    E   H
    |
    G

Output 
A - B - D - E - G - F - H - C
```

- **Explanation:**
  - A is the first node in the input  so it is the first in the output
  - A has no children so it is followed by its next, B.
  - B has a child DLL so nodes from that are inserted next, D.
  - D has a child DLL so that is inserted next, E
  - E has child DLL so that is inserted next, G
  - G has no children and no next so the next element inserted is F
  - F has child DLL so that is inserted next, H
  - H has no child DLL and no next so F’s next is inserted, C
  - C has no DLL and no next so we are finished
  - Compiling the nodes into a DLL gives us the desired result.




**Here is some music for you to listen while working on this project:**
[Chillstep Music for Programming](https://youtu.be/M5QY2_8704o)


---

## **Grading** 

* **Auto Graded Tests (100 points)** see below for the point distribution for the auto graded tests:
    * 01 - test\_empty: \_\_/7
    * 02 - test\_push: \_\_/7
    * 03 - test\_pop: \_\_/7
    * 04 - test\_list\_to\_dll: \_\_/7
    * 05 - test\_dll\_to\_list: \_\_/7
    * 06 - test\_find: \_\_/9
    * 07 - test\_find\_all: \_\_/9
    * 08 - test\_remove: \_\_/9
    * 09 - test\_remove\_all: \_\_/9
    * 10 - test\_reverse: \_\_/9 
    * 11 - test\_dream\_escaper: \_\_/20 

* **Late penalty:** Projects submitted late incur a 10% deduction per hour past the deadline, applied to the earned project score. Late submissions are accepted only until the accumulated penalty reduces the score to 0; beyond that point, submissions will no longer be graded.
For example:
    * 1 hour late → 10% deduction
    * 5 hours late → 50% deduction
    * 10 hours late → 100% deduction (grade = 0)
    * After that point → submission not accepted

* **No submission = -100:** No submission or submission of the exact starter code will result in a score of −100, so be sure to submit on time.

## **Submission Guidelines**

### **Deliverables:**

Projects are submitted through the D2L Assignment tool.
The submission link allows two separate file uploads, so no folders or ZIP files are required.
Students must upload exactly two files:
1. solution.py – the Python implementation
2. README.txt – a brief, structured self-report

Both files must be uploaded directly to the appropriate D2L assignment link.


### **README.txt:**
Projects are graded primarily on completion and honest reporting.
Failure to upload the required README.txt file by the assignment deadline will result in a 5% deduction per hour until the README is submitted.
This policy is in place to ensure that both required files are uploaded and that students practice complete and professional submission habits.
If a student is found to have been dishonest in the README (e.g., misreporting which unit tests passed or failed), the earned score for that coding challenge will be reduced by 50% on the first occurrence.
If the same student is found to be dishonest again on a subsequent coding challenge, the score for that assignment will be 0 (−100%).


You may copy and paste the following format into your README.txt and fill in the points you earned for each test case:

```
Total points for Project01: ___

Detailed points for each project:
1) test_empty: ___
2) test_push: ___
3) test_pop: ___
4) test_list_to_dll: ___
5) test_dll_to_list: ___
6) test_find: ___
7) test_find_all: ___
8) test_remove: ___
9) test_remove_all: ___
10) test_reverse: ___
11) test_dream_escaper: ___
```


### **How to Work on a Project Locally:**
1. 🖥️ Ensure PyCharm is installed.
2. 📦 **Download** the starter package from the *Projects* tab on D2L. *(See the tutorial video on D2L if needed)*.
3. 📝 Write your code and run **tests.py**, once ready, 📤 **upload** your `solution.py` and `READ.txt` to D2L. 



---


## **Outside resources:** 
Note students can not use Chegg or similar sites, see syllabus for details, use of outside resources for the application problem is strictly forbidden, use of outside resources is limited to max of 2 functions in a project.
