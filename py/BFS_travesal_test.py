from BFS_travesal import BFS_travesal
from Bi_Search_Tree import Bi_Search_Tree

def draw_tree(array):
    BST = Bi_Search_Tree()
    for i in array:
        BST.insert(i)

    for vals in BFS_travesal(BST):
        print(vals)

if __name__ == '__main__':
    array = [5,8,3,9,2,6,1,4]
    draw_tree(array)