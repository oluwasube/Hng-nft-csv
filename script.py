#!/usr/bin/python3

import json
import csv
import hashlib



with open ("HNGi9 CSV FILE.csv", "r") as opened_file:
    content = csv.reader(opened_file)
    
    data = []
    for each_row in content:
        
        json_file =  {
        "format": "CHIP-0007",
        "name":each_row[2],
        "minting tool" :each_row[0],
        "sensitive_content": False,
        "series_number": each_row[1],
        "series_total": 420,
         "attributes": [
      {
        "trait_type": "",
        "value": ""
      }
    ],
        'collection' : {
            'name' : 'Zuri NFT Tickets for Free Lunch',
            'id' : each_row[7]
                }, 
        
        }
        
        data.append(json_file)

with open ("nft.json", "w") as f:
    json.dump(data, f, indent=4)
          
        

with open ("nft.json") as jsonfile: # hashing the json data file
    contents = json.load(jsonfile)
    
    for each_content in contents:
        altcontent = f"{each_content}"
        json_hash = hashlib.sha256(altcontent.encode()).hexdigest()
        each_content.update({"Hash":json_hash})
    contents.append({"Hash":json_hash})
    

with open ("nft_hash.json", "w") as nft_hash: # export the hash data to a new json file
    json.dump(contents, nft_hash, indent=4)


with open("nft_hash.json", "r") as hashed_json: #load the hashd data
    hashed_content = json.load(hashed_json)

#Convert nft_hash data to csv(filename.output.csv)
with open ("HNGi9 CSV FILE.output.csv", "w", newline="") as f:
    update_content =  hashed_content[0].keys()
    writer = csv.DictWriter(f, fieldnames= update_content)
    writer.writeheader()
    for content in  hashed_content:
        writer.writerow(content)