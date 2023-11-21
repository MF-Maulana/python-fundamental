"""
Semua sintaksis dasar bahasa pemrograman terdiri dari:
1. Sekuensial: langkah berurutan
2. Percabangan: langkah melompat jika kondisi terpenuhi
3. Perulangan: mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""

# Sequential
print('Mom said, "Go to the shop"')
print('Budi answered, "Okay, what should I do at the shop?"')
print('Mother answered, "Buy one bottle of milk, and if there are eggs, buy 6"')
print('So Budi went to the shop')
print('And start shopping')

# Branching
milk_bottle_count = 173
egg_count = 1587
print(f'number of milk bottles is {milk_bottle_count} bottles')
print(f'number of eggs {egg_count} pieces')

if milk_bottle_count > 0:
    print('Budi checked the price, and it turned out he had enough money')
    if egg_count == 0:
        print('Budi bought 1 bottle of milk')
    else:
        print('Budi bought 6 bottles of milk')
else:
    print('Budi did not buy a bottle of milk')

print('Budi returns home')
print('Convey the results to his mother')
