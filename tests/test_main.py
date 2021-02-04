import direx


def test_dir():
    assert dir(direx) == [
        "__builtins__",
        "__cached__",
        "__doc__",
        "__file__",
        "__loader__",
        "__name__",
        "__package__",
        "__path__",
        "__spec__",
        "__version__",
        "direx",
        "show_dir_info",
        "show_dir_method",
        "show_dir_module",
    ]
