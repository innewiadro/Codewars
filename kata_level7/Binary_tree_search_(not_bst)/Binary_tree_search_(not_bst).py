
from preloaded import Node

def search(n: int, root: Node | None) -> bool:
    """Determines if a value is in a binary tree (NOT bst)."""
    if root is None:
        return False
    if root.value == n:
        return True
    return search(n, root.left) or search(n, root.right)