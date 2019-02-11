# import glob
#
# a = glob.iglob('dubl', recursive=True)
# print(a)

from pathlib import Path
import csv
i = 4000
b = list()
for i in range(i, 5000):
    i += 1

    a = list(Path('dubl').glob('*-' + str(i) + '.jpg'))

    if len(a) > 1:
        print(a)
        l = 0
        for row in a:
            l =+ 1
            print(row[l])
        # with open('list.csv', 'wb') as myfile:
        #     wr = csv.writer(myfile)
        #     wr.writerow(a)


