
anyone = set()
total_anyone = 0
total_everyone = 0
with open('input.txt') as forms:
    for line in forms:
        if line == '\n':
            total_anyone += len(anyone)
            total_everyone += len(everyone)
            anyone = set()

        else:
            answer = line.strip()
            if anyone == set():
                everyone = answer
            for i in answer:
                anyone.add(i)
                for j in everyone:
                    if j not in answer:
                        everyone = everyone.replace(j, '')

total_anyone += len(anyone)
total_everyone += len(everyone)

print('Sum of answered yes by anyone in each group:', total_anyone)
print('Sum of answered yes by everyone in each group:', total_everyone)
