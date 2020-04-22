money = int(input())
five_cents = 5
two_cents = 2
one_cent = 1
coins = [five_cents, two_cents, one_cent]
num_least_each_coin = 1
num_solutions = 0
solutions = []
for num_five_cents in range(num_least_each_coin, money // five_cents + 1):
    change_money_with_five_cents = num_five_cents * five_cents
    for num_two_cents in range(num_least_each_coin, (
                                                            money - change_money_with_five_cents) // two_cents + 1):
        change_money_with_five_and_two_cents = change_money_with_five_cents + num_two_cents * two_cents
        for num_one_cent in range(num_least_each_coin,
                                  (money - change_money_with_five_and_two_cents)
                                  // one_cent + 1):
            change_money = change_money_with_five_and_two_cents + \
                           num_one_cent * one_cent
            if change_money > money:
                break
            elif change_money == money:
                num_solutions += 1
                solutions.append((num_five_cents, num_two_cents, num_one_cent,
                                  num_five_cents + num_two_cents + num_one_cent))
                break

solutions.sort(reverse=True)
for value in solutions:
    print("fen5:{}, fen2:{}, fen1:{}, total:{}".format(value[0], value[1],
                                                       value[2], value[3]))
print('count = {}'.format(num_solutions))
