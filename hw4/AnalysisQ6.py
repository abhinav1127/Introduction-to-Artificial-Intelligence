import Testing

penMeanAccuracy = []
penStandardDeviation = []
penMaxAccuracy = []

carMeanAccuracy = []
carStandardDeviation = []
carMaxAccuracy = []

for j in range(0, 45, 5):
    print "Currently testing ", j, " nodes."
    penAccuracies = []
    carAccuracies = []

    for i in range(5):
        penAccuracies.append(Testing.testPenData([j])[1])
        carAccuracies.append(Testing.testCarData([j])[1])

    penMeanAccuracy.append(Testing.average(penAccuracies))
    penStandardDeviation.append(Testing.stDeviation(penAccuracies))
    penMaxAccuracy.append(max(penAccuracies))

    carMeanAccuracy.append(Testing.average(carAccuracies))
    carStandardDeviation.append(Testing.stDeviation(carAccuracies))
    carMaxAccuracy.append(max(carAccuracies))

print "penMeanAccuracy: ", penMeanAccuracy
print "penStandardDeviation: ", penStandardDeviation
print "penMaxAccuracy: ", penMaxAccuracy
print "\n\n"

print "carMeanAccuracy: ", carMeanAccuracy
print "carStandardDeviation: ", carStandardDeviation
print "carMaxAccuracy: ", carMaxAccuracy
