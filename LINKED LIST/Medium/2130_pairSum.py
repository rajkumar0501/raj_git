class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: [ListNode]) -> [ListNode]:

        if head == None:
            return None

        a1 = []

        current = head

        while current:
            a1.append(current.val)
            current = current.next


        a2 = []

        pre, cur = None, head

        while cur:
            temp = cur.next
            cur.next = pre
            pre, cur = cur, temp

        current = pre

        while current:
            a2.append(current.val)
            current = current.next

        max = 0
        length = int(len(a1) / 2)

        for i in range(length):
            x = a1[i] + a2[i]
            if x > max:
                max = x

        return max




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
head = array_to_linked_list([47,22,81,46,94,95,90,22,55,91,6,83,49,65,10,32,41,26,83,99,14,85,42,99,89,69,30,92,32,74,9,81,5,9])
new_head = solution.pairSum(head)
print(new_head)
