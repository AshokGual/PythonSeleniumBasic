import pytest


# if u want to use fixture in class level then use @pytest.fixture(scope="class")
@pytest.fixture(scope="class")
def testsetup():
    print("i will execute before any test")
    yield
    print("i will execute at last")


@pytest.fixture()
def dataLoad():
    print("user profile data is stored")
    return ["ashok", "kumar", "gual"]


# send multiple data in a single run
@pytest.fixture(params=[("firefox", "Ashok"), ("chrome", "kumar"), ("IE", "gual")])
def cross_browser(request):
    return request.param
