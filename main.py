""""
This python script is used to generate entries for each ptag in the config.yml file
and adds them to the shop.yaml file to save time and work
"""
import yaml

# Load the config.yml file
with open('files/config.yml', 'r', encoding='utf-8') as file:
    config_data = yaml.safe_load(file)

# Load the shop.yaml file
with open('files/shop.yaml', 'r', encoding='utf-8') as file:
    shop_data = yaml.safe_load(file)

# Extract the tags from the config.yml file
tags = config_data['deluxetags']

# Generate entries for each ptag and add them to the shop.yaml file
for tag, details in tags.items():
    # Generate the entry
    print('Processing entry for tag:', tag)
    permission = details["permission"]
    description = details["description"]
    # skip if description contains the word Dex
    if 'Dex' in description:
        print('Skipping entry with description containing Dex')
        print(details)
        continue

    entry = {
        'ItemID': 'minecraft:name_tag',
        'ItemDisplay': details['tag'],
        'Cost': 1000,  # Set a default cost
        'Lore': [details['description']],
        'Commands': ['lp user %pl% permission set' + permission],  # Set default commands
        'PurchaseLimit': 1
    }

    # Add the entry to the ShopItems section of the shop.yaml file
    shop_data['ShopItems'][tag] = entry

    # Add the entry ID to the Tags section of the ShopCategories
    shop_data['ShopCategories']['Tags']['EnabledItems'].append(tag)

# Save the updated shop.yaml file
with open('files/shop.yaml', 'w', encoding='utf-8') as file:
    yaml.safe_dump(shop_data, file)
