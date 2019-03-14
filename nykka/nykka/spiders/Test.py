

def all_even():
    n = 0
    while True:
        yield n
        n += 2

for item in all_even():
    print(item)        