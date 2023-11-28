"""
Looping program to read a book with for
"""
book_count = 10
print('Mom said, "Read all your books"')

read_count = 0
print(f'The number of books that have been read is {read_count}')

for read_count in range(1, book_count + 1):
    print(f"Book {read_count} has been read")

print(f'The number of books that have been read is {read_count}')
