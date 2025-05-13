
from sample_module import greet

def test_greet(capsys):
    greet("World")
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, World!"
