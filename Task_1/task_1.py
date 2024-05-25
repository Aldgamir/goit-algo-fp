class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    head = prev
    return head

def insertion_sort_linked_list(head):
    if head is None:
        return None
    sorted_list = None
    current = head
    while current:
        next_node = current.next
        sorted_list = insert_in_sorted_list(sorted_list, current)
        current = next_node
    return sorted_list

def insert_in_sorted_list(sorted_list, node):
    if sorted_list is None or sorted_list.data >= node.data:
        node.next = sorted_list
        return node
    current = sorted_list
    while current.next and current.next.data < node.data:
        current = current.next
    node.next = current.next
    current.next = node
    return sorted_list if sorted_list else node

def merge_sorted_linked_lists(list1, list2):
    dummy = Node(0)
    current = dummy
    while list1 and list2:
        if list1.data < list2.data:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    current.next = list1 if list1 else list2
    return dummy.next

# Приклад використання:

# Створення списку
head = Node(3)
head.next = Node(1)
head.next.next = Node(2)

# Реверсування списку
reversed_head = reverse_linked_list(head)
print("Реверсований список:")
while reversed_head:
    print(reversed_head.data, end=" ")
    reversed_head = reversed_head.next
print("\n")

# Створення та сортування списку
unsorted_head = Node(4)
unsorted_head.next = Node(2)
unsorted_head.next.next = Node(3)
unsorted_head.next.next.next = Node(1)

sorted_head = insertion_sort_linked_list(unsorted_head)
print("Відсортований список:")
while sorted_head:
    print(sorted_head.data, end=" ")
    sorted_head = sorted_head.next
print("\n")

# Об'єднання двох відсортованих списків
list1 = Node(1)
list1.next = Node(3)
list1.next.next = Node(5)

list2 = Node(2)
list2.next = Node(4)
list2.next.next = Node(6)

merged_head = merge_sorted_linked_lists(list1, list2)
print("Об'єднаний відсортований список:")
while merged_head:
    print(merged_head.data, end=" ")
    merged_head = merged_head.next
