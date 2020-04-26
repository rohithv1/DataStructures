# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 17:33:28 2020

@author: Rohith_Vemulapally
"""

# LinkedList using Recursion
class LinkedList():
    
    def __init__(self, payload):
        if type(payload) in [list, dict]:
            raise TypeError("List and Dictionary objects are prohibited as elements")
        self.payload = payload
        self.next = None
    
    def append(self, payload):
        """ This method adds the elements at the end of the linked list."""
        if self.next:
            self.next.append(payload)
        else:
            self.next = LinkedList(payload)
            
    def push(self, payload):
        """ This method adds the elements at the start of the linked list."""
        temp = self.next
        self.next = LinkedList(self.payload)
        self.next.next = temp
        self.payload = payload
        
    def insert_after(self, ele, payload):
        if not self.next:
            raise ValueError("Element {} not in linked list".format(ele))
        if self.payload == ele:
            temp = self.next
            temp.push(payload)
            self.next = temp
            return
        else:
            self.next.insert_after(ele, payload)
        
    def print_elements(self):
        """ This method is useful for debugging purposes."""
        if self.next:
            print("{} -> ".format(self.payload), end="")
            self.next.print_elements()
        else:
            print("{}".format(self.payload))
            
    def delete_element(self, element):
        """ This method deletes the given element."""
        if not self.next:
            raise ValueError("Element not in the Linked list")
        if self.next.payload == element:
            temp = self.next.next
            self.next = None
            self.next = temp
        elif self.payload == element:
            self.payload = self.next.payload
            self.next = self.next.next
        else:
            self.next.delete_element(element)

if __name__ == "__main__":
    new_ll = LinkedList(5)
    new_ll.append(3)
    new_ll.append(10)
    new_ll.append(6)
    new_ll.append(4)
    new_ll.append(27)
    new_ll.print_elements()
    new_ll.delete_element(3)
    new_ll.print_elements()
    new_ll.delete_element(5)
    new_ll.print_elements()