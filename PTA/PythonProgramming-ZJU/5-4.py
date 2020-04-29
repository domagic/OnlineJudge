sequence = list(map(int, input().split(',')))
a_group = list(range(1, 6))
b_group = list(range(6, 11))
ticket_a_group = {}
ticket_b_group = {}
for ticket_number in sequence:
    if ticket_number <= a_group[-1]:
        pass
    else:
        ticket_b_group[ticket_number] = 1
no_ticket_in_b_group = [member for member in b_group if
                        member not in ticket_b_group]
print(' '.join(list(map(str, no_ticket_in_b_group))), end='')
