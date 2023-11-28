"""
Looping program to read a book with while
"""
book_count = 10
print('Mom said, "Read all your books"')

read_count = 0
print(f'The number of books that have been read is {read_count}')

while read_count < book_count:
    read_count = read_count + 1
    print(f'Book {read_count} has been read')

print(f'The number of books that have been read is {read_count}')
