from class_1_poetry import main

def test_function1():
    r = main.my_first_function
    assert r == "Hello Rabeea"

def test_function2():
    r = main.my_first_function
    assert r != "Hello Rabi"