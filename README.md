# Buy and Sell Pump Fun Tokens (Python) 

This repository holds the metadata and transaction instruction blueprint for buying and selling pump fun tokens. 

## Main File pump_fun.py 

Functions: 
buy(mint_str sol_in, slippage, priority_in_lamports)
sell(mint_str, priority_in_lamports,token_balance, slippage,  close_token_account: bool)

## Constants (constants.py): 

Important metadata information as well as conversion standard units can be found here. 


## Coin Data (coin_data.py): 

Gets the information (such as price) about the coin via its bonding curve

## Configurations (config.py): 

Replace "PRIV_KEY" and "RPC" with your Private Key and RPC URL. (required) 


## Utils (config.py): 

More functions are used in the process of sending and confirming transactions. 
e.g confirm_txn will get the result of the transaction. 




## Last but not least... 

Be sure to join our Discord for more trading tools and code. 

Donation Wallet: 6ZnZwDYvDU38ztgN5KzWgkD3UcYYs7sKEPPL531zDPyT







