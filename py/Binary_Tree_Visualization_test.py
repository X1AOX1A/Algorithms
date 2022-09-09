from Binary_Tree_Visualization import draw_tree
from Bi_Search_Tree import Bi_Search_Tree

def creat_tree(array):
    BST = Bi_Search_Tree()
    for i in array:
        BST.insert(i)        
    return BST

array = [5, 2, 8, 4, 6, 9]
BST = creat_tree(array)
draw_tree(BST.root)