class BlockErrors:
    def __init__(self, ignored_exceptions):
        self.ignored_exceptions = ignored_exceptions

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type in self.ignored_exceptions:

            return True
        return False


