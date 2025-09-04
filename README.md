# GoogleInterviewTwo
**PROBLEM STATEMENT**
Given a Binary Search Tree (BST) and a pointer/reference to a particular node, write an algorithm to find:
1. The next smallest value (inorder predecessor).
2. The next largest value (inorder successor).
**Example:**

        10
       /  \
      5    15
     /     / \
    2    12  20

**Input:** 
node = 15
**Output:**
Next smallest = 12
Next largest = 20

**APPROACH**
We need to find the inorder predecessor (next smallest) and the inorder successor (next largest) of a given node in a Binary Search Tree (BST).
🔹 **Successor (next largest)**
1. If the node has a right child → the successor is the leftmost node in its right subtree.
2. If the node has no right child → go upward using the parent pointer until you find a node where the current node is in its left subtree. That parent is the successor.
3. If no such parent exists → the node is the largest in the tree, so no successor exists.
🔹 **Predecessor (next smallest)**
1. If the node has a left child → the predecessor is the rightmost node in its left subtree.
2. If the node has no left child → go upward using the parent pointer until you find a node where the current node is in its right subtree. That parent is the predecessor.
3. If no such parent exists → the node is the smallest in the tree, so no predecessor exists.

**CODE EXPLANATION**
Node Structure
Each node stores a value (val), and links to its left, right, and parent.
Having a parent pointer allows us to move upward in the tree when needed.
Successor Function
If the node has a right child → the successor is found by going one step right, then continuously left until the smallest value in that subtree is reached.
If the node has no right child → move upward along parent pointers until you find a node where you came from its left child. That parent is the successor.
If no such parent exists → the node is the largest, so no successor.
Predecessor Function
If the node has a left child → the predecessor is found by going one step left, then continuously right until the largest value in that subtree is reached.
If the node has no left child → move upward along parent pointers until you find a node where you came from its right child. That parent is the predecessor.
If no such parent exists → the node is the smallest, so no predecessor.
Tree Construction
The example BST is built manually with parent pointers set, so we can test directly by passing any node reference.
Testing
When the node is 15:
Predecessor → 12
Successor → 20
