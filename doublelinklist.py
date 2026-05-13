from node import Node
class DoubleLinkList:
    def __init__(self):
        self.head = None
        self.tail = None
    def add_child(self, parent:Node, child:Node):
        if parent.sub_list is None:
            parent.sub_list = DoubleLinkList()
            parent.sub_list.head = child
            parent.sub_list.tail = child
        else:
            current = parent.sub_list.tail
            current.next = child
            child.prev = current
            parent.sub_list.tail = child
        return parent.sub_list
    def search_by_attr(self, attr, value):
        current = self.head
        while current:
            if getattr(current, attr) == value:
                return current
            current = current.next
        return None
    def update_value(self, search_value, **attrs):
        node = self.search_by_attr('id', search_value)
        if node:
            for k, v in attrs.items():
                setattr(node, k, v)
            return True
        return False
    def delete_value(self, search_value):
        current = self.head
        while current:
            if current.id == search_value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return True
            current = current.next
        return False
