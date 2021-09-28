# importing the module
import json
import os
# Opening JSON file
with open('data.json') as json_file:
    data = json.load(json_file)
    ls = data["annotations"]["images"]
    file_name_list = []
    for item in ls:
        file_name_list.append(item["file_name"])
    old_dir = "/home/qb/jetson-inference/jetson-inference/python/training/segmentation/data/coco/train2017/"
    new_dir = old_dir.replace("train2017","val2017")
    for m in file_name_list:
        if (os.path.isfile(old_dir+m)):
            os.rename(old_dir+m, new_dir+m)
    