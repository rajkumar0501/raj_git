class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: [ListNode]) -> [int]:

        if not head or not head.next:
            return [-1, -1]

        pre = head
        node = head.next
        index = 2

        arr = []

        while node.next:
            if (node.val < pre.val and node.val < node.next.val) or (node.val > pre.val and node.val > node.next.val):
                arr.append(index)

            pre = node
            node = node.next
            index += 1


        if len(arr) < 2:
            return [-1, -1]


        maxD = arr[-1] - arr[0]
        minD = float('inf')

        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            if diff < minD:
                minD = diff

        return [minD, maxD]



def array_to_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head



solution = Solution()
head = array_to_linked_list([6,8,4,1,9,6,6,10,6])
new_head = solution.nodesBetweenCriticalPoints(head)
print((new_head))
