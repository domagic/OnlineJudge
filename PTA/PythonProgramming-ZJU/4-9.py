print("[1] apple")
print("[2] pear")
print("[3] orange")
print("[4] grape")
print("[0] exit")

choices = input().split()
fruit_price = {1: ('apple', 3.00), 2: ('pear', 2.50), 3: ('orange', 4.10),
               4: ('grape', 10.20)}
search_times = 0
while True:
    choice = int(choices[search_times])
    if choice == 0:
        break
    elif choice not in fruit_price:
        price = 0
    else:
        price = fruit_price[choice][-1]
    print('price = {:.2f}'.format(price))
    search_times += 1
    if search_times >= 5:
        break
