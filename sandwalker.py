import sqlite3
import json
from tqdm import tqdm
connection = sqlite3.connect('data/timeline-backup.db')
c = connection.cursor()

amounts =[]
amountsTxt = open("amounts.txt","w")
for node in tqdm(open("nodes-with-comma.txt").read().split(",\n")):
    c.execute(f"select amount from timeline where account='{node}' and date('2022-02-23')<time and time<date('2022-02-24');")
    # print(f"select amount from timeline where account='{node}' and {firstBlock}<block<{secondBlock};")
    amount = 0
    for row in c:
        # print(row)
        amount+=row[0]

    # print(node, amount)
    amounts.append(amount)
    amountsTxt.write(str(amount)+",\n")
# print(amounts)
print("avg:",sum(amounts)/len(amounts))

open("amountsList.txt","w").write(json.dumps(amounts))
