# This is some basic chain analysis scripts I created to track down poktpool nodes.

## How it works
First get the addressees of where poktpool nodes are directly staked from. You can do this by looking at the account-txs of c46fd195948d7c5c19b8f3c69ad69cfa4f6a7cb9 (poktpool wallet), and viewing all outgoing transactions for each tranche. They are easy to spot because they usually have a descriptive memo, and they usually send a lot of POKT. Get the receiving addresses of these big staking transactions, and then query all of the account-txs of those. For every outoing transaction of 15375 POKT (the amount poktpool stakes on their nodes), add that address to the list.

## How to run

Git clone this repo onto a pokt node with an rpc available at localhost:8081, or replace the localhost:8081 with any POKT endpoint.

```
pip3 install tqdm requests

python3 getNodes.py

python3 getServicers.py
```


## Support

If you support this work and wish to donate, then it would mean the world to me.

POKT wallet: c4bd169241a0b40acbf0a6917f3c74bdf42295f9
