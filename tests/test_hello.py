import io 
import pytest 
from contextlib import redirect_stdout
from hello import print_hello_world


def test_print_hello_world():
    captured_output = io.StringIO()
    with redirect_stdout(captured_output):
        print_hello_world()

    assert captured_output.getvalue().strip() == "Hello, World!"