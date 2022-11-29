

pets = {'cat': 4, 'dog': 15, 'bird': 5, 'velociraptor': 150}

pets['mouse'] = 1
pets['dog'] = 20
pets.pop('bird')

for key, value in pets.items():
    print(f" {key}: {value}")