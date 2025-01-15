import pytest 


@pytest.mark.slow
def test_ex1():

    assert 1==1

@pytest.mark.slow
def test_ex2():

    assert 1==1

@pytest.mark.api
def test_ex3():

    assert 1==1