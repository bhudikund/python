import sys
from contextlib import contextmanager


class Redirect:
    def __init__(self, stdout=None, stderr=None):
        self.stdout = stdout
        self.stderr = stderr
        self.old_stdout = sys.stdout
        self.old_stderr = sys.stderr

    def __enter__(self):
        if self.stdout is not None:
            sys.stdout = self.stdout
        if self.stderr is not None:
            sys.stderr = self.stderr

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = self.old_stdout
        sys.stderr = self.old_stderr

        if exc_type:
            print(f"Exception caught: {exc_val}", file=self.old_stderr)

        return False


if __name__ == '__main__':
    stdout_file = open('stdout.txt', 'w')
    stderr_file = open('stderr.txt', 'w')

    with Redirect(stdout=stdout_file, stderr=stderr_file):
        print('Hello stdout.txt')
        raise Exception('Hello stderr.txt')

    print('Hello stdout again')
    raise Exception('Hello stderr')

    stdout_file.close()
    stderr_file.close()