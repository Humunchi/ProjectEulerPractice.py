#find sun of even fibonachi numbers not exceeding 4 million (4613732)

total = 0

i, j = 1, 0

while j <= 4000000:
        if j % 2 == 0:
                total += j
        i, j = j, i + j

print (total)
