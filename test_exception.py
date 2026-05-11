import pytest

def withdraw(balance, amount):

    if amount > balance:
        raise ValueError("Insufficient balance")

    return balance - amount


def test_withdraw():

    with pytest.raises(ValueError):
        withdraw(1000, 1500)