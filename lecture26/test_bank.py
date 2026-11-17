import pytest
from bank import BankAccount


def test_initial_balance():
    account = BankAccount("Natia")
    assert account.balance == 0.0


def test_deposit_success():
    account = BankAccount("Natia", 100)
    account.deposit(50)
    assert account.balance == 150


def test_deposit_negative():
    account = BankAccount("Natia", 100)

    with pytest.raises(ValueError):
        account.deposit(-50)


def test_withdraw_success():
    account = BankAccount("Natia", 200)
    account.withdraw(50)
    assert account.balance == 150


def test_withdraw_insufficient_funds():
    account = BankAccount("Natia", 100)

    with pytest.raises(ValueError):
        account.withdraw(200)


def test_withdraw_negative():
    account = BankAccount("Natia", 100)

    with pytest.raises(ValueError):
        account.withdraw(-50)

