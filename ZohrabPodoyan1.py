custom_dict = {
    'fruits': ['apple', 'banana', 'cherry'],
    'vegetables': ['carrot', 'lettuce', 'pea'],
    'grains': ['rice', 'wheat', 'quinoa']
}
def add_item(category, item):
    if category in custom_dict:
        custom_dict[category].append(item)
    else:
        custom_dict[category] = [item]
def display_items():
    for category, items in custom_dict.items():
        print(f"{category.capitalize()}: {', '.join(items)}")
def remove_item(category, item):
    if category in custom_dict and item in custom_dict[category]:
        custom_dict[category].remove(item)
def clear_category(category):
    if category in custom_dict:
        custom_dict[category] = []
def item_exists(category, item):
    return category in custom_dict and item in custom_dict[category]
add_item('fruits', 'orange')
add_item('dairy', 'milk')
add_item('dairy', 'cheese')
print("Custom Dictionary:")
display_items()
if 'banana' in custom_dict['fruits']:
    custom_dict['fruits'].remove('banana')
print("\nAfter removing 'banana' from fruits:")
display_items()
remove_item('dairy', 'milk')
clear_category('grains')
print("\nAfter removing 'milk' from dairy and clearing grains:")
display_items()
print(f"\nDoes 'carrot' exist in vegetables? {'Yes' if item_exists('vegetables', 'carrot') else 'No'}")