import math

name = ["Slashing", "Radiant"]
minD = [4.0, 3.0]
maxD = [8.0, 7.0]
atkS = [1.0, .33]
crit = [.10, 1]
critDM = [2, 2]

def avgD(_minD, _maxD):
    avgD = math.ceil((int(_minD) + int(_maxD)) / 2)
    return float(avgD)

for i in xrange(2):
    avgDam = avgD(minD[i], maxD[i])
    apm = (60.0 / atkS[i])
    baseD = ((avgDam * apm) / 60.0)
    critHits = (apm * crit[i])
    #critD = (((apm * crit[i]) * (avgDam * critDM[i])) / apm) + baseD
    critD = (((critHits * (avgDam * critDM[i])) + (apm-critHits) * (avgDam)) / 60.0)
    print(name[i])
    print(80 * "=")
    print("Minimum damage: {0}\nMaximum damage: {1}\nAverage damage: {2}".format(minD[i], maxD[i], avgDam))
    print("")
    print("Attack speed: {0}\nAttacks per min: {1}".format(atkS[i], apm))
    print("")
    print("Crit chance: {0}\nCrit dmg mod: {1}".format(crit, critDM))
    print(80 * "=")
    print("Base damage: {0}\nCrit damage: {1}".format(baseD, critD))
    print(80 * "=")
