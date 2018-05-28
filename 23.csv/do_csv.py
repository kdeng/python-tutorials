import csv
from itertools import islice

f1 = csv.reader(open('1.csv'))
f2 = csv.reader(open('2.csv'))
writer = csv.writer(open('out.csv', 'w'), delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
writer.writerow(["id", "lat", "lng", "sta"])

for line in islice(f1, 1, None):
    line[1] = int(line[1])
    line[2] = int(line[2])

    print("f1: {} : {}".format(line[1], line[2]))
    
    a = line[1]
    b = line[2]
    f2_lines = islice(f2, 1, None)
    
    for line1 in f2_lines:
        line1[1] = int(line1[1])
        line1[2] = int(line1[2])
        line1[3] = str(line1[3])
        print("f2: {} : {}".format(line1[1], line1[2]))

        c = line1[1]
        d = line1[2]
        e = line1[3]
        if a > c - 1 and a < c + 1 and b > d - 1 and b < d + 1:
            writer.writerow([line[0:3] + [e]])