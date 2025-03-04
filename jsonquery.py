import json
loadfile = open('drug-ndc-0001-of-0001.json')
dataset = json.load(loadfile)
user_input = ''

while user_input is not 'quit':
    user_input = input('Product NDC Code: ')
    for item in dataset['results']:
        if item.get('product_ndc') == user_input:
            print('Generic Name: ',item.get('generic_name'))
            print('Labeler Name: ',item.get('labeler_name'))
            print('Active Ingredients: ',item.get('active_ingredients'))
    print('End of Operation')