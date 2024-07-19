class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: [ListNode]) -> [ListNode]:

        if head == None:
            return None

        pre, cur = None, head

        while cur:
            temp = cur.next
            cur.next = pre
            pre, cur = cur, temp

        return pre

def array_to_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_array(head):
    arr = []
    current = head
    while current:
        arr.append(current.val)
        current = current.next
    return arr


solution = Solution()
head = array_to_linked_list([1,2,3,4,5])
new_head = solution.reverseList(head)
print(linked_list_to_array(new_head))
