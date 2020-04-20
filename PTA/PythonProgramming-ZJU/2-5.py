n = int(input())
sequence = [i / (2 * i - 1) for i in range(1, n + 1)]
positiveSequence = [element for index, element in enumerate(sequence) if
                    index % 2 == 0]
negativeSequence = [element for index, element in enumerate(sequence) if
                    index % 2 != 0]
print("{0:.3f}".format(sum(positiveSequence) - sum(negativeSequence)))
