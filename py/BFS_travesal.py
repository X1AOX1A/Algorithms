def BFS_travesal(BT):
    '''Inplementation of Depth-first tree traversal
    
    Args:
    - Binary_Tree: binary tree
    
    Output:
    - BFS_result: list, result of BFS
    '''
    
    BFS_result = []
    current_nodes = [BT.root]
    bottom = False

    while bottom is False:
        val = []
        next_nodes = []
        bottom = True
        for node in current_nodes:
            if node is not None:
                bottom = False
                val.append(node.value)
                next_nodes.append(node.left)
                next_nodes.append(node.right) 
            else:
                val.append(None)  
                next_nodes.append(None)
                next_nodes.append(None) 
              
        BFS_result.append(val)
        current_nodes = next_nodes
    
    return BFS_result[:-1]