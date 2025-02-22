class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = ListNode(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(value)

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def merge_sort(self):
        if not self.head or not self.head.next:
            return self.head
        
        def split(head):
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            middle = slow.next
            slow.next = None
            return head, middle
        
        def merge(left, right):
            dummy = ListNode()
            tail = dummy
            while left and right:
                if left.value < right.value:
                    tail.next = left
                    left = left.next
                else:
                    tail.next = right
                    right = right.next
                tail = tail.next
            tail.next = left or right
            return dummy.next

        def merge_sort_recursive(head):
            if not head or not head.next:
                return head
            left, right = split(head)
            left = merge_sort_recursive(left)
            right = merge_sort_recursive(right)
            return merge(left, right)

        self.head = merge_sort_recursive(self.head)

    @staticmethod
    def merge_sorted_lists(l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.value < l2.value:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next

# Приклад
ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)
print("Оригінальний список:")
ll.print_list()

ll.reverse()
print("Реверсований список:")
ll.print_list()

ll.merge_sort()
print("Відсортований список:")
ll.print_list()

ll1 = LinkedList()
ll1.append(1)
ll1.append(3)
ll1.append(5)

ll2 = LinkedList()
ll2.append(2)
ll2.append(4)
ll2.append(6)

merged_head = LinkedList.merge_sorted_lists(ll1.head, ll2.head)
print("Об'єднаний відсортований список:")
while merged_head:
    print(merged_head.value, end=" -> ")
    merged_head = merged_head.next
print("None")