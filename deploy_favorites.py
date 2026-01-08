import boa  # type: ignore
from dotenv import load_dotenv
import os
from boa.network import NetworkEnv, EthereumRPC  # type: ignore
from eth_account import Account

load_dotenv()


def main():
    print("Deploying favorites contract...")
    rpc = os.getenv("RPC_URL")
    env = NetworkEnv(EthereumRPC(rpc))
    boa.set_env(env)

    anvil_key = os.getenv("ANVIL_PRIVATE_KEY")
    my_account = Account.from_key(anvil_key)
    boa.env.add_account(my_account, force_eoa=True)

    favorites_contract = boa.load("favorites.vy")

    starting_favorite_number = favorites_contract.retrieve()
    print(f"Starting favorite number is: {starting_favorite_number}")

    print("Storing new favorite number: 42")
    favorites_contract.store(42)

    updated_favorite_number = favorites_contract.retrieve()
    print(f"Updated favorite number is: {updated_favorite_number}")


if __name__ == "__main__":
    main()
