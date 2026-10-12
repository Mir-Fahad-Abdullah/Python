class TreeNode:     ## Tree Node class
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

## Inorder Traversal in BST
def inorder_traversal(root):
    if root is None:    ## if the node is empty then return the node itself
        return
    inorder_traversal(root.left)    ## left --> root --> right
    print(root.data, end=",")
    inorder_traversal(root.right)


## Search for a Value in a BST
def search_in_bst(root, target):
    if root is None:        ## if the root has not assigned then return not found
        return None     
    elif root == target:    ## if the root/node matches the target then return the current node
        return root
    elif target>root:       ## if target is greater, then move to the right side
        return search_in_bst(root.right, target)
    else:
        return search_in_bst(root.left, target)


## Insert new node in the BST
def insert_node(root, new_data):
    if root is None:    ## if root is not assigned or current node is the leaf node 
        return insert_node(new_data)    ## then make a instance/instert 
    elif new_data>root:
        root.right = insert_node(root.right, new_data)  ## move to the right side and insert new
    elif new_data<root:
        root.left = insert_node(root.left, new_data)    ## move to the left side and insert new

    return root


## Find the minimum or lowest value in the BST
def find_min_value(root):
    current_node = root

    while current_node is not None: ## untill we find leaf node
        current_node = current_node.left    ## move to the left most node

    return current_node



## Delete a Node in a BST
def delete_node(root, target_node):
    if root is None:
        return None

    ## case-1: if the target node is a leaf node only
    if target_node>root:
        root.right = delete_node(root.right, target_node)   ## move to right
    elif target_node<root:
        root.left = delete_node(root.left, target_node)
    else:   # Node with only one child or no child
        if root.left is None:   ## if the current node do not have any left child
            temp = root.right   ## preserve the right child and return 
            root = None
            return temp
        elif root.right is None:    ## if the current node do not have any left child
            temp = root.left    ## ## preserve the left child and return 
            root = None
            return temp

        # Node with two children, get the in-order successor
        successor = find_min_value(root.right)
        root.data = successor.data
        root.right = delete_node(root.right, successor.data)


    return root


## 6. Create a BST and Test All Functions
root = None

# Insert values into the BST
values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    root = insert_node(root, value)


# Display the BST using inorder traversal
print("Inorder Traversal:")
inorder_traversal(root)
print()


# Search for a value
target = 60
result = search_in_bst(root, target)

if result is not None:
    print(f"{target} found in the BST.")
else:
    print(f"{target} not found in the BST.")


# Find the minimum value
minimum = find_min_value(root)

if minimum is not None:
    print("Minimum value:", minimum.data)


# Delete a node
root = delete_node(root, 30)

print("Inorder Traversal after deleting 30:")
inorder_traversal(root)
print()




