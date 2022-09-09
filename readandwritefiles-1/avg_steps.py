import csv

infile = open('steps.csv','r')
outfile = open('avg_steps.csv','w')

csvfile = csv.reader(infile)
writer = csv.writer(outfile)

next(csvfile)

runMonth = 0

monthlist = ['January','February','March','April','May','June','July','August','September','October','November','December']
totalSteps = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for record in csvfile:
    month = int(record[0])
    steps = int(record[1])

    if month == 1:
        totalSteps[0] += steps

    elif month == 2:
        totalSteps[1] += steps

    elif month == 3:
        totalSteps[2] += steps

    elif month == 4:
        totalSteps[3] += steps

    elif month == 5:
        totalSteps[4] += steps

    elif month == 6:
        totalSteps[5] += steps

    elif month == 7:
        totalSteps[6] += steps

    elif month == 8:
        totalSteps[7] += steps

    elif month == 9:
        totalSteps[8] += steps

    elif month == 10:
        totalSteps[9] += steps

    elif month == 11:
        totalSteps[10] += steps

    elif month == 12:
        totalSteps[11] += steps

average_steps = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

average_steps[0] = totalSteps[0] / 31
average_steps[1] = totalSteps[1] / 28
average_steps[2] = totalSteps[2] / 31
average_steps[3] = totalSteps[3] / 30
average_steps[4] = totalSteps[4] / 31
average_steps[5] = totalSteps[5] / 30
average_steps[6] = totalSteps[6] / 31
average_steps[7] = totalSteps[7] / 31
average_steps[8] = totalSteps[8] / 30
average_steps[9] = totalSteps[9] / 31
average_steps[10] = totalSteps[10] / 30
average_steps[11] = totalSteps[11] / 31

writer.writerow([monthlist[0], average_steps[0]])
writer.writerow([monthlist[1], average_steps[1]])
writer.writerow([monthlist[2], average_steps[2]])
writer.writerow([monthlist[3], average_steps[3]])
writer.writerow([monthlist[4], average_steps[4]])
writer.writerow([monthlist[5], average_steps[5]])
writer.writerow([monthlist[6], average_steps[6]])
writer.writerow([monthlist[7], average_steps[7]])
writer.writerow([monthlist[8], average_steps[8]])
writer.writerow([monthlist[9], average_steps[9]])
writer.writerow([monthlist[10], average_steps[10]])
writer.writerow([monthlist[11], average_steps[11]])