import sys
input = sys.stdin.readline

n = int(input())
tree = {}

for i in range(n):
    root, left, right = input().split()
    tree[root] = (left, right)

def preorder(node):
    if node == ".":
        return
    
    print(node, end="")
    left, right = tree[node]
    preorder(left)
    preorder(right)

def inorder(node):
    if node == ".":
        return
    
    left, right = tree[node]
    inorder(left)
    print(node, end="")
    inorder(right)

def postorder(node):
    if node == ".":
        return
    
    left, right = tree[node]
    postorder(left)
    postorder(right)
    print(node, end="")

preorder("A")
print()

inorder("A")
print()

postorder("A")