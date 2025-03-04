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

os.system('clear')
user_input = ''
while user_input != 'quit':
    user_input = input('Product NDC or \'quit\' to exit: ')
    if user_input != 'quit':
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