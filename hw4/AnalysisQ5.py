import Testing

penAccuracies = []
carAccuracies = []

for i in range(1):
    penAccuracies.append(Testing.testPenData()[1])
    carAccuracies.append(Testing.testCarData()[1])

print "Pen Data"
print "Accuracies: ", penAccuracies
print "Average: ", Testing.average(penAccuracies)
print "Standard Deviation: ", Testing.stDeviation(penAccuracies)
print "Max: ", max(penAccuracies), "\n\n"

print "Car Data"
print "Accuracies: ", carAccuracies
print "Average: ", Testing.average(carAccuracies)
print "Standard Deviation: ", Testing.stDeviation(carAccuracies)
print "Max: ", max(carAccuracies)
