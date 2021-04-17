import os
from pathlib import Path
from termcolor import colored

# Used for pretty representation
PIPE = "│"
ELBOW = "└──"
TEE = "├──"
PIPE_PREFIX = "│   "
SPACE_PREFIX = "    "


def get_absolute_path(path):
    path = Path(path)
    if not path.is_absolute():
        path = Path.cwd() / path

    return path


def colorize(node):
    """Returns blue for dir and uncolored for files"""
    return colored(node.name, "blue") if node.is_dir() else node.name


def format(prefix, connector, node):
    """Tree print format"""
    return f"{prefix}{connector} {colorize(node)}"


class TreeGenerator:
    """Concrete tree generator. This returns the same visual
    representation as one would get by using unix tree command."""

    def __init__(self, root_dir, max_depth):
        """
        Params
        ------
        root_dir: dir to start traveral from.
        max_depth: max level till which tree seach would go.
        """
        self._root_dir = get_absolute_path(root_dir)
        self._tree = [colorize(self._root_dir)]
        self._max_depth = max_depth

    def build_tree(self):
        """Generates the printable tree form representation"""
        self._traverse(node=self._root_dir, prefix="", depth=1)

        return self._tree

    def _traverse(self, node, prefix, depth):
        """traverse tree and appends each level in formatted tree list"""
        children = list(node.iterdir())
        child_count = len(children)

        for pos, child in enumerate(children):
            connector = ELBOW if pos == child_count - 1 else TEE
            self._tree.append(format(prefix, connector, child))
            if depth < self._max_depth and child.is_dir():
                extension = SPACE_PREFIX if pos == child_count - 1 else PIPE_PREFIX
                self._traverse(node=child, prefix=prefix + extension, depth=depth + 1)
