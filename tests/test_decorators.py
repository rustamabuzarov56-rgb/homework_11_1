from src.decorators import log


def test_my_function_ok(capsys):
    @log(filename=None)
    def my_function(x, y):
        return x + y

    my_function(4, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n\n"


def test_my_function_error(capsys):
    @log(filename=None)
    def my_function(x, y):
        return x / y

    my_function(4, 0)
    captured = capsys.readouterr()
    assert captured.out == "my_function error: division by zero. Inputs: (4, 0), {}\n"
