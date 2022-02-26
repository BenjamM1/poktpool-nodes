import requests
import json
from tqdm import tqdm

with open("nodes.txt") as file:
    nodes = file.read().split()

def node_(address):
    data = requests.post("http://localhost:8081/v1/query/node", headers={"Content-Type": "application/json","Accept": "Accept: application/json"}, data=json.dumps({"address":address})).json()

    return data["service_url"]

out = open("node_urls.txt", "w")
string = ""
for node in tqdm(nodes):
    print(node, node_(node))
    string += str(node+" "+node_(node)+"\n")

out.write(string)
