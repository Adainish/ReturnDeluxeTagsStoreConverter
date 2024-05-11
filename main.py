import yaml

# Load the config.yml file
with open('files/config.yml', 'r') as file:
    config_data = yaml.safe_load(file)

# Load the shop.yaml file
with open('files/shop.yaml', 'r') as file:
    shop_data = yaml.safe_load(file)

# Extract the tags from the config.yml file
tags = config_data['deluxetags']

# Generate entries for each ptag and add them to the shop.yaml file
for tag, details in tags.items():
    # Generate the entry
    print(details["permission"])
    permission = details["permission"]
    description = details["description"]
    #skip if description contains the word Dex
    if 'Dex' in description:
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
with open('files/shop.yaml', 'w') as file:
    yaml.safe_dump(shop_data, file)
