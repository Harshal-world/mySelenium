# import pytest
# @pytest.fixture(autouse=True,scope="class")
# def greet():
#     print("in greet function")
#
# class Testmain:
#
#     def test_ge1(self):
#         print("in first greet")
#
#     def test_ge2(self):
#         print("in second greet")

import pytest


@pytest.fixture(autouse=True, scope="class")
def greet():
    print("\n In greet")
    return "Hello"


class TestSample:
    def test_greet(self):
        print("\n In test_greet")

    def test_greetings(self):
        print("\n In test_greetings")
