import json
loadfile = open('drug-ndc-0001-of-0001.json')
dataset = json.load(loadfile)
def UPCLookup(upc_number):
    for item in dataset['results']:
        if item.get("upc") == upc_number:
            return item.get("product_ndc")
        else:
            print("UPC not in Database, try NDC.")
            return None
def NDCExtractor(upc_number):
    #may god forgive me
    if len(upc_number) != 13:
        return None
    ndc_format_01_part_1 = upc_number[1:6]
    ndc_format_01_part_2 = upc_number[6:10]
    ndc_format_01_part_3 = upc_number[10:12]
    ndc_format_01 = f"{ndc_format_01_part_1}-{ndc_format_01_part_2}-{ndc_format_01_part_3}"
    for item in dataset['results']:
        if item.get("product_ndc") == ndc_format_01:
            print(item)
            return ndc_format_01
    ndc_format_02_part_1 = upc_number[1:6]
    ndc_format_02_part_2 = upc_number[6:9]
    ndc_format_02_part_3 = upc_number[9:11]
    ndc_format_02 = f"{ndc_format_02_part_1}-{ndc_format_02_part_2}-{ndc_format_02_part_3}"
    for item in dataset['results']:
        if item.get("product_ndc") == ndc_format_02:
            print(item)
            return ndc_format_02
    ndc_format_03_part_1 = upc_number[1:5]
    ndc_format_03_part_2 = upc_number[5:9]
    ndc_format_03_part_3 = upc_number[9:11]
    ndc_format_03 = f"{ndc_format_03_part_1}-{ndc_format_03_part_2}-{ndc_format_03_part_3}"
    for item in dataset['results']:
        if item.get('product_ndc') == ndc_format_03:
            print(item)
            return ndc_format_03
    print('Unable to Extract NDC')
    return None