"""
Semua sintaksis dasar bahasa pemrograman terdiri dari:
1. Sekuensial: langkah berurutan
2. Percabangan: langkah melompat jika kondisi terpenuhi
3. Perulangan: mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""
# Sekuensial
print('Ibu memberi perintah, "Beli 1 botol susu. Dan jika ada telur, beli juga 6 butir telur"')
print('Budi menjawab, "Ok"')
print('Budi pergi ke toko')
print('Apakah susu ada?')
Susu_ada = True
if Susu_ada:
    print('Beli 1 botol susu')
else:
    print('Tidak membeli susu')
print('Apakah telur ada?')
Telur_ada = True
if Telur_ada:
    print('Beli 6 butir telur')
else:
    print('Tidak membeli telur')
print('Budi pulang ke rumah')
print('Budi menyerahkan hasil belanjanya kepada Ibu')
