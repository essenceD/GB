while True:
    startDist, goal = input('Enter a first-day distance: '), input('Enter your goal: ')
    if startDist.isdigit() and goal.isdigit():
        counter = 1
        startDist = float(startDist)
        goal = float(goal)
        while startDist < goal:
            startDist = startDist * 1.1
            counter += 1
        break
    else:
        print('\nDistances is a positive integer!\n')
print('\nRunner achieves the goal distance after {} days'.format(counter))
