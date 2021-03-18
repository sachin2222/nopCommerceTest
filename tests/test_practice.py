import pytest


class Testpractice:

    def test_function_demo(self):
        print("Demo Function")

    def test_function_1(self, get_Data):
        print(get_Data[0])
        print(get_Data[1])

    @pytest.fixture(params=[("sachin", "sharma"), ("delhi", "mumbai")])
    def get_Data(self, request):
        return request.param
