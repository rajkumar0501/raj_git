class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: [ListNode]) -> [ListNode]:

        if not head or not head.next:
            return head

        first = head
        second = first.next



        while second and second.next:

            first.val += second.val

            if second.val == 0:
                first.next = second
                first = second


            second = second.next

        first.next = None

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
head = array_to_linked_list([0,3,1,0,4,5,2,0])
new_head = solution.mergeNodes(head)
print(linked_list_to_array(new_head))
