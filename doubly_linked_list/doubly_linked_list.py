"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            #set head and tail to the new node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1
            # set new node's next to current head
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # store value head
        value = self.head.value
        # delete head
        if self.head.next is not None:
                # headnext to none
            self.head.next = None
                #value to head.next
            value = self.head.next
        elif self.head.next is None:
                #head to None
            self.head = None
                #tail to None
            self.tail = None
              # dec. length
            self.length -= 1
            return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.head is None and self.tail is None:
            #head/tail to new node
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            #new node to tail
            new_node.prev = self.tail
            #tail next to new node
            self.tail.next = new_node
            #tail to the new node
            self.tail = new_node
            # inc, length
            self.length += 1
    
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        value = self.tail.value
        if self.tail.prev is None:
                #tail to None
            self.tail = None
                #head to None
            self.head = None
                # dec. length
            self.length -= 1
        else:
            value.prev.next = value.next
            value.next.prev = value.prev
            self.length -= 1
        return value 
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        node.delete()

      
        # self.length -= 1

        if self.head == node:
        #     self.head = self.head.next
            node.delete()
            self.head = node.next

        # if self.tail == node:
        #     self.tail = self.tail.prev

        # return node
        # node.delete()

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        current = self.head
        max = 0

        while current is not None:
            if current.value > max:
                max = current.value
            current = current.next

        return max