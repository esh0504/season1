class Node:
    def __init__(self, value='A', left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def preorder(head):
    print(head.value, end='')
    if head.left != None:
        preorder(head.left)
    if head.right != None:
        preorder(head.right)

def inorder(head):
    if head.left != None:
        inorder(head.left)
    print(head.value, end='')
    if head.right != None:
        inorder(head.right)

def postorder(head):
    
    if head.left != None:
        postorder(head.left)
    if head.right != None:
        postorder(head.right)
    print(head.value, end='')




if __name__=='__main__':
    N = int(input())
    Linked_list = []
    head = Node()
    for i in range(N):
        Linked_list.append(Node(chr(i+65)))

    for i in range(N):
        parent, left, right = map(ord, input().split())

        if left != 46:
            Linked_list[parent-65].left = Linked_list[left-65]
        if right != 46:
            Linked_list[parent-65].right = Linked_list[right-65]


    preorder(Linked_list[0])
    print()
    inorder(Linked_list[0])
    print()
    postorder(Linked_list[0])