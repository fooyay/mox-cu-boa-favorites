import boa  # type: ignore
from boa.contracts.vyper.vyper_contract import VyperContract  # type: ignore


def main():
    print("Read in our Vyper contract and deploy to pyevm network using titanoboa")
    favorites_contract: VyperContract = boa.load("favorites.vy")
    print(type(favorites_contract))

    starting_favorite_number = favorites_contract.retrieve()
    print(f"Starting favorite number is: {starting_favorite_number}")

    favorites_contract.store(42)
    updated_favorite_number = favorites_contract.retrieve()
    print(f"Updated favorite number is: {updated_favorite_number}")


if __name__ == "__main__":
    main()
