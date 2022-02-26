import requests
import json
from tqdm import tqdm
accounts =["1be22fd8d66989e2d4f34502a5c87e2236c8417b", "8453bce5364b4492f18d93ee6463a8bd51acf734", "80c979509646c0f5dd9f1a88b08ea7965f9b0e9e", "08e4cd68aa603eb44d03265d56569f68bd028eac", "9bdd8d4daea2443d15211f3667dd6c4dac75e033", "47032e8217830a3fb2d5d446dbeac88d2f31b15e", "eb0a478f1854fd386f38413e037156d1bf4e13b6", "97a4607e8ad137b748411c63c4fb9ddd03f456ba", "724812eba34c3c664cd9ed237dd50e3dbe1618aa", "f9a80db815a49e2c07bdada3412ae5644ca807d6"]
nodes = []

def accountTxs(address):
    data = requests.post("http://localhost:8081/v1/query/accounttxs", headers={"Content-Type": "application/json","Accept": "Accept: application/json"}, data=json.dumps({"address":address,"page":1,"per_page":10000, "sort":"desc"})).json()

    return data["txs"]
out = open("nodes.txt", "w")

for account in tqdm(accounts):
    accountNodes =0
    txs = accountTxs(account)
    for tx in txs:
        try:
            if int(tx["stdTx"]["msg"]["value"]["amount"])==15375000000:
                accountNodes+=1
                nodes.append(tx["stdTx"]["msg"]["value"]["to_address"])
        except:
            pass
    print(account, accountNodes)

for node in nodes:
    out.write(node+",\n")
