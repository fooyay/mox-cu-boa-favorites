import boa  # type: ignore
from boa.contracts.vyper.vyper_contract import VyperContract  # type: ignore


def main():
    print("Read in our Vyper contract and deploy to pyevm network using titanoboa")
    favorites_contract: VyperContract = boa.load("favorites.vy")
    print(type(favorites_contract))


if __name__ == "__main__":
    main()
