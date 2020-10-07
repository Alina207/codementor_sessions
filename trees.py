"""

Trees Data structure

-> is a data structure that is used for heirarchical data
-> each node can have a maximum of 2 children (left_child and right_child)

class LinkListNode():
    data
    pointer to the next child

class TreeNode():
    data
    pointer to the left child
    pointer to the right child


Main concepts:
    -> DFS (Depth first search)
    -> BFS (Breadth first search)


/* Constructed binary tree is
              1
            /   \
          2      3
        /  \
      4     5
*/


-> every question can be solved using both BFS and DFS
-> Trees is always represented as an Array
    -> there are 3 ways to do this
    -> there are three traversal techniques

        1. Preorder (Root, Left, Right)
        2. Postorder (Left, Right, Root)
        3. Inorder (Left, Root, Right)


/* Constructed binary tree is
              1
            /   \
          2      3
        /  \
      4     5
*/

Preorder : [1, 2, 4, 5, 3]
Postorder : [4, 5, 2, 3, 1]
Inorder: [4, 2, 5, 1, 3]

============================================
Binary Search Tree

-> a tree where the left node is always smaller than root, and right node is always greater than root.
-> The left and right subtree each must also be a binary search tree.


    10
   /   \
  5     40
 /  \      \
1    7      50

Inorder : [1,5,7,10,40,50]
Preorder: [10,5,1,7,40,50]
#  Postorder: [1,7,5,10,40,50]


Left View of a tree (recursive/non-recurive)
Right view
top view
bottom view
vertical view
diagnol view
postorder
preorder
inorder
"""
