class WishList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __getitem__(self, item):
        return self.items[item]

    def __add__(self, other):
        self.items.append(other)

    def __str__(self):
        wL = []
        print('List of items in WishList')
        print('-' * 30)
        for i , item in enumerate(self.items):
            wL.append(f'{i + 1}. {item}')
        return '\n'.join(wL)

w = WishList(['He', 'She', 'It'])
print(len(w))
print(w[2])
w + 'They'
print(w)