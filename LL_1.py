class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
        

    def find_middle_node(self):
        slow = self.head
        fast = self.head

        while fast != None and fast.next != None:
            slow = slow.next 
            fast = fast.next.next
        
        return slow


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)

print( my_linked_list.find_middle_node().value )

new_int = input()
while new_int != "stop":
    if new_int.isdigit():
        my_linked_list.append(new_int) 
    else:
        print("not int")
    new_int = input()

print(my_linked_list.tail.value)
