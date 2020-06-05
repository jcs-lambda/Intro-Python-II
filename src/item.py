import re

any_whitespace_pattern = re.compile(r'.*\s.*')


class Item(object):
    all_items = []

    def __init__(self, name:str, description:str):
        name, description = name.strip(), description.strip()

        if any_whitespace_pattern.match(name):
            raise ValueError('Name must be a single word')

        for item in Item.all_items:
            if name.lower() == item.name.lower():
                raise ValueError(f'Item already exists: {name}')

        self.name = name
        self.description = description
        Item.all_items.append(self)

    def on_take(self):
        print(f'{self}, has been aquired.')
    
    def on_drop(self):
        print(f'{self}, has been relinquished.')

    def __str__(self):
        return f'{self.name}, {self.description}'
