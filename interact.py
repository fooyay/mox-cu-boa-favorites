import os
import boa  # type: ignore
from dotenv import load_dotenv
from boa.network import NetworkEnv, EthereumRPC  # type: ignore
from eth_account import Account


load_dotenv()


MY_CONTRACT = "0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512"


def main():
    print("Interacting with existing favorites contract...")
    rpc = os.getenv("RPC_URL")
    env = NetworkEnv(EthereumRPC(rpc))
    boa.set_env(env)

    anvil_key = os.getenv("ANVIL_PRIVATE_KEY")
    my_account = Account.from_key(anvil_key)
    boa.env.add_account(my_account, force_eoa=True)

    favorites_deployer = boa.load_partial("favorites.vy")
    favorites_contract = favorites_deployer.at(MY_CONTRACT)

    starting_favorite_number = favorites_contract.retrieve()
    print(f"Favorite number is: {starting_favorite_number}")

    favorites_contract.store(22)
    updated_favorite_number = favorites_contract.retrieve()
    print(f"Updated favorite number is: {updated_favorite_number}")


if __name__ == "__main__":
    main()
