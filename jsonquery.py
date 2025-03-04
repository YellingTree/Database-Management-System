import json
import os

loadfile = open('drug-ndc-0001-of-0001.json')
dataset = json.load(loadfile)



def ItemFormatting(item):
    generic_name = item.get('generic_name')
    labeler_name = item.get('labeler_name')
    brand_name = item.get('brand_name')
    ingredient_list = []
    for ingredient in item.get('active_ingredients'):
        ingredient_set = {ingredient['name']},{ingredient['strength']}
        ingredient_list.append(ingredient_set)
    formatted_product = []
    formatted_product.append(generic_name)
    formatted_product.append(labeler_name)
    formatted_product.append(brand_name)
    return formatted_product, ingredient_list

def DatabaseLookup(ndc_number):
    for item in dataset['results']:
        if item.get('product_ndc') == ndc_number:
            print('Found Item')
            return item

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
            
os.system('clear')
user_input = ''
while user_input != 'quit':
    user_input = input('Product NDC or \'quit\' to exit: ')
    if user_input != 'quit':
        upc_to_ndc = UPCLookup(user_input)
        if upc_to_ndc is not None:
            search_item = DatabaseLookup(upc_to_ndc)
        else:
            search_item = NDCExtractor(user_input)
        if search_item == None:
            search_item = DatabaseLookup(user_input)
        if search_item is not None:
            results, ingredients = ItemFormatting(search_item)
            print('Generic/Labeler/Brand Names:')
            for item in results:
                print(item)
            print("Active Ingredients:")
            for item in ingredients:
                print(item)
        else:
            print("No item found")
    print('End of Operation')