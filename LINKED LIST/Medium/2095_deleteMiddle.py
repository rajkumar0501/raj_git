class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: [ListNode]) -> [ListNode]:
        if not head.next:
            return None
        s = head
        f = head.next.next

        while f and f.next:
            s = s.next
            f = f.next.next


        s.next = s.next.next

        return head


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
head = array_to_linked_list([1, 3, 4, 7, 1, 2, 6])
new_head = solution.deleteMiddle(head)
print(linked_list_to_array(new_head))
