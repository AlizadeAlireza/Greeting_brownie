from brownie import Greeting
from scripts.helpful_scripts import get_account


def deploy():
    account = get_account()
    print()
    print(f"the current account that uses is : {account}")
    print()
    # deploy the contract
    first_initialize_name = input(
        "enter your first name to initialize the constructor: "
    )
    greeting_contract = Greeting.deploy(first_initialize_name, {"from": account})
    print()
    print(f"the contract deployed in {greeting_contract.address}")
    print()
    print(
        f"the first name is initialize in constructor is : {greeting_contract.name()}\n\nso we want to say you hello\n"
    )
    print(greeting_contract.getGreeting())
    print()
    # set the new name
    while True:
        print("you want another name??\n")
        choice = int(input("\nplease enter your choice.\n\n1: yes\n2: No\n"))
        if choice == 1:
            new_name = input("\nset your new name: ")
            greeting_contract.setName(new_name)
            print(f"{greeting_contract.getGreeting()}\n")

        else:
            break


def main():
    deploy()
