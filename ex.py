start1 = ['fee', 'fie', 'foe']
rhymes=[
    ('flop', 'get a mop'),
    ('fope', 'turn the rope'),
    ('fa', 'get your ma'),
    ('fudge', 'call the judge'),
    ('fat', 'pet the cat'),
    ('fog', 'wlk the dog'),
    ('fun', "say we're done")
]
start2 = "Someone better"
start1_cap = ' '.join([word.capitalize()+'!' for word in start1])
for first, second in rhymes :

    print(f'{start1_cap} {first.capitalize()}!')
    print(f'{start2} {second}.')