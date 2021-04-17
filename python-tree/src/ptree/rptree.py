class DirectoryTree:
    """Directory Tree generator.

    This uses some concrete implementation of directory tree
    generation that could be injected.

    It expects that the concrete generator implements the
    build_tree method which returns printable values"""

    def __init__(self, generator):
        self._generator = generator

    def generate(self):
        for entry in self._generator.build_tree():
            print(entry)
