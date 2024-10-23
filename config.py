from solana.rpc.api import Client
from solders.keypair import Keypair #type: ignore





PRIV_KEY = "YOUR PRIVATE KEY"
RPC = "YOUR RPC URL"
client = Client(RPC)
payer_keypair = Keypair.from_base58_string(PRIV_KEY)
