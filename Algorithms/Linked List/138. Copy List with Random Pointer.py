"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head==None:
            return None
        hashmap={}
        dummy=Node(0)
        cur=dummy
        hashmap={}
        while head!=None:
            if head not in hashmap:
                hashmap[head]=Node(head.val)
            cur.next=hashmap[head]
            if head.random!=None:
                if head.random not in hashmap:
                    hashmap[head.random]=Node(head.random.val)
                cur.next.random=hashmap[head.random]
            head=head.next
            cur=cur.next
        return dummy.next

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head==None:
            return None
        cur=head
        while cur!=None:
            copy=Node(cur.val)
            copy.next=cur.next
            cur.next=copy
            cur=cur.next.next
        cur=head
        while cur!=None:
            if cur.random !=None:
                cur.next.random=cur.random.next
            cur=cur.next.next
        dummy=Node(0)
        copy=dummy
        cur=head
        while cur!=None:
            copy.next=cur.next
            cur.next=cur.next.next
            copy=copy.next
            cur=cur.next
        return dummy.next