class Node:
    def __init__(self, type, value=None, left=None, right=None):
        self.type = type
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        if self.type == "operator":
            return f"({self.value} {self.left} {self.right})"
        else:
            return str(self.value)