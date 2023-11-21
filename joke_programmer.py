# Sequential
print('Mother said, "Buy 1 bottle of milk. And if there are eggs, buy 6 eggs too"')
print('Budi answered, "Okay"')
print('Budi went to the shop')

# Branching
print('Is there milk?')
there_is_milk = True
if there_is_milk:
    print('there is milk')
    print('Buy 1 bottle of milk')
    print('Is there egg?')
    there_is_egg = True
    if there_is_egg:
        print('there is egg')
        print('Buy 6 eggs')
    else:
        print('Do not buy eggs')
else:
    print('Do not buy milk')
    print('Is there egg?')
    there_is_egg = True
    if there_is_egg:
        print('there is egg')
        print('Buy 6 eggs')
    else:
        print('Do not buy eggs')
print('Budi returns home')
print('Budi handed over the results of his shopping to his mother')
