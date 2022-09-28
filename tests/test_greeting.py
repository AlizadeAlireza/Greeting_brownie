from scripts.helpful_scripts import get_account
from brownie import Greeting


def test_static_value():
    # arrange
    account = get_account()

    # act
    greeting_contract = Greeting.deploy("", {"from": account})

    # assert
    assert greeting_contract.greetingPrefix() == "Hello "


def test_first_name():
    # arrange
    account = get_account()

    # act
    # deploy the contract
    greeting_contract = Greeting.deploy("alireza", {"from": account})
    expected_name = "alireza"

    # assert
    assert greeting_contract.name() == expected_name


def test_new_name():
    # arrange
    account = get_account()

    # act
    greeting_contract = Greeting.deploy("", {"from": account})
    new_name = "mohsen"
    greeting_contract.setName(new_name)

    # assert
    assert greeting_contract.name() == new_name
    assert greeting_contract.getGreeting() == "Hello mohsen"
