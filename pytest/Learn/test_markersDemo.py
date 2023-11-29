import pytest

@pytest.mark.regression
def test_regression():
    print("Test 1")

@pytest.mark.xfail
def test_regression2():
    print("Test 2")
    assert 4 == 5

@pytest.mark.regression
def test_regression2():
    print("Test 2")

# pytest -m regression  -v  => run regression
# pytest -v -m "not regression"  => run not regression

