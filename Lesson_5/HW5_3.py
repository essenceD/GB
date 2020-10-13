avg_sal = 0
with open('samples\\inputs\\text_3.txt', 'r', encoding='utf-8') as file:
    f = file.readlines()
print('\nLosers (salary < 20000) are:')
for i in f:
    avg_sal += float(i.split()[len(i.split()) - 1])
    if float(i.split()[len(i.split()) - 1]) < 20000:
        print(i.split()[0])
print('\nAverage salary: {}'.format(avg_sal / len(f)))





