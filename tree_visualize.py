import numpy as np
class Node():
    def __init__(self, text,sub_comment=[]):
        self.text = text
        self.sub_comment = []
    def append_child(self,node):
        self.sub_comment.append(node)
root = np.load("D:\Quora-scrapToStructure\question_NO_1_total_8_iterations.npy",allow_pickle=True)
root = root.tolist()
txt = ""
def traverse(ele,level):
    global txt
    if ele is None: return
    txt += "        "*level + ele.text[:40].replace("\n","")+"...\n"
    for e in ele.sub_comment:
        traverse(e,level+1)

traverse(root,level=0)
import io
with io.open("tree_visualize.txt", "w", encoding="utf-8") as f:
    f.write(txt)
