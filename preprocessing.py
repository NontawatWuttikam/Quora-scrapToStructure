import os
import numpy as np
import tqdm
import copy
import numpy as np
import matplotlib.pyplot as plt
class Node():
    def __init__(self, text,sub_comment=[]):
        self.text = text
        self.sub_comment = []
    def append_child(self,node):
        self.sub_comment.append(node)

ans_stck = []
data_folder = "scroll_25_15_iteration"
for question in tqdm.tqdm(os.scandir(f"./data/{data_folder}")):
    if "total" in question.name:
        root = np.load(question.path.replace("\\","/"), allow_pickle = True).tolist()
        # print(ar)
        if len(root.sub_comment) != 0:
            ans_stck.extend(root.sub_comment)

count_element = 0
comment_chains = []

def recurse_all(node,chain):
    if node is None: return
    global count_element, comment_chains
    count_element += 1
    chain.append(node.text)
    if len(node.sub_comment) == 0:
        comment_chains.append(copy.deepcopy(chain))
        return
    for n in node.sub_comment:
        recurse_all(n,chain)

for i in ans_stck:
    if i is None: continue
    recurse_all(i,[])

print(len(ans_stck))
print(count_element)
# print(len(comment_chains[2]))

print(sorted([len(i) for i in comment_chains])[::-1])
x = list(filter(lambda x:x != 1 and x != 0 ,sorted([len(i) for i in comment_chains])[::-1]))
print(len(x))
plt.yscale('log')
plt.hist(x,95)
plt.savefig(f"histogram_{data_folder}_.png")
plt.show()
