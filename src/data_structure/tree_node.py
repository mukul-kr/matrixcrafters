class TreeNode:
    def __init__(self, digit):
        self.digit = digit
        self.children = []

    def to_dict(self):
        return {'d': self.digit, 'c': [child.to_dict() for child in self.children]}

