""" cct2coco.py

Convert a COCOCameraTraps-formatted JSON into a COCO-formatted JSON.
"""
import json
import os
import time
from datetime import date
import exiftool
import command

folder = "/Users/lorybuttazzoni/Documents/TMU/CVIS-lab/Project/data/ena24/"

with open("../ena24.json", "r") as f:
    ena24 = json.load(f)

with open("/Users/lorybuttazzoni/Documents/TMU/CVIS-lab/Project/data/COCO/annotations/instances_val2017.json", "r") as q:
    instances_train2017 = json.load(q)

# INFO

info = ena24["info"]

info["description"] = "ENA24 in COCO"
info["url"] = folder
info["version"] = "1.1"
info["year"] = 2022
info["contributor"] = "cindris"
info["date_created"] = "2022/12/08"

# LICENSES

ena24["licenses"] = [
    {
        "url": "http://creativecommons.org/licenses/by-nc-sa/2.0/",
        "id": 1,
        "name": "Attribution-NonCommercial-ShareAlike License"
    },
    {
        "url": "http://creativecommons.org/licenses/by-nc/2.0/",
        "id": 2,
        "name": "Attribution-NonCommercial License"
    }
]

# IMAGES

for i in range(len(ena24["images"])):
    ena24["images"][i]["license"] = 1
    ena24["images"][i]["coco_url"] = folder + ena24["images"][i]["file_name"]
    ena24["images"][i]["flickr_url"] = ena24["images"][0]["coco_url"]
    ena24["images"][i]["date_captured"] = ""
    ena24["images"][i]["id"] = int(ena24["images"][i]["id"])


# CATEGORIES

for category in ena24["categories"]:
    category["supercategory"] = "ENA24"

# ANNOTATIONS

for i in range(len(ena24["annotations"])):
    ena24["annotations"][i]["iscrowd"] = 0
    ena24["annotations"][i]["image_id"] = int(ena24["annotations"][i]["image_id"])
    ena24["annotations"][i]["id"] = i
    ena24["annotations"][i]["area"] = ena24["annotations"][i]["bbox"][2] * ena24["annotations"][i]["bbox"][3]

# output

print(ena24["annotations"][0])
print(instances_train2017["annotations"][0])


with open("../ena24coco.json", "w") as o:
    json.dump(ena24, o, indent=2)

with open("/Users/lorybuttazzoni/Documents/TMU/CVIS-lab/Project/data/COCO/annotations/instances_val2017_humanreadable.json", "w") as r:
    json.dump(instances_train2017, r, indent=2)
