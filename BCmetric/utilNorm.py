from math import atan2,sqrt,cos
import numpy as np


def averageDirection(angleArray,n):

   return sum(anglearr)/float(n)


def angleDistance(angle):
    return angle

def std(angleArray, n, averageDir):
    sumValue = sum([pow(angleDistance(angle - averageDir), 2) for angle in angleArray])
    return sqrt(float(sumValue)/n)

def kurtosis(angleArray, n, averageDir, std):
    sumValue = sum([float(pow(angleDistance(angle - averageDir)/std, 4)) for angle in angleArray])
    return float(sumValue)/float(n)

def skewness(angleArray, n, averageDir, std):
    sumValue = sum([float(pow(angleDistance(angle - averageDir)/std, 3)) for angle in angleArray])
    return float(sumValue)/float(n)

def BCMetric(kurtosisValue, skewnessValue, n):
    return (pow(skewnessValue,2) + 1)/(kurtosisValue-3+float(3*pow(n-1, 2))/((n-2)*(n-3)))

def BCCal(angleArry):
    arrLen = len(angleArry)
    averageDir = averageDirection(angleArry, arrLen)
    stdValue = std(angleArry,arrLen,averageDir)
    kurtosisValue = kurtosis(angleArry, arrLen, averageDir, stdValue)
    skewnessValie = skewness(angleArry,arrLen,averageDir,stdValue)

    print(averageDir, stdValue, kurtosisValue, skewnessValie)
    return BCMetric(kurtosisValue, skewnessValie, arrLen)

# anglearr = [[91.0, 1], [271.0, 1], [270.0, 1], [225.0, 1], [91.0, 1], [90.0, 1], [91.0, 1], [90.0, 1], [206.0, 1], [273.0, 1], [270.0, 1], [255.0, 1], [270.0, 1], [269.0, 1], [91.0, 1], [90.0, 1], [271.0, 1], [270.0, 1], [270.0, 1], [91.0, 1], [90.0, 1], [86.0, 1], [91.0, 1], [92.0, 1], [86.0, 1], [90.0, 1], [91.0, 1], [88.0, 1], [90.0, 1], [270.0, 1], [271.0, 1], [265.0, 1], [83.0, 1], [91.0, 1], [24.0, 1], [90.0, 1], [180.0, 1], [271.0, 1], [270.0, 1], [270.0, 1], [271.0, 1], [270.0, 1], [72.0, 1], [248.0, 1], [271.0, 1], [270.0, 1], [78.0, 1], [91.0, 1], [39.0, 1], [91.0, 1], [270.0, 1], [88.0, 1], [92.0, 1], [89.0, 1], [90.0, 1], [90.0, 1]]
# anglearr = [elem[0] for elem in anglearr]
# #anglearr = [0,0,0,180,180,180]
#
# #anglearr = [[125.0, 1], [189.0, 1], [282.0, 1], [189.0, 1], [9.0, 1], [9.0, 1], [10.0, 1], [9.0, 1], [195.0, 1], [190.0, 1], [188.0, 1], [131.0, 1], [36.0, 1], [89.0, 1], [186.0, 1], [8.0, 1], [11.0, 1], [7.0, 1], [9.0, 1], [10.0, 1], [189.0, 1], [189.0, 1], [9.0, 1], [10.0, 1], [8.0, 1], [11.0, 1], [189.0, 1], [189.0, 1], [309.0, 1], [101.0, 1], [358.0, 1], [189.0, 1], [8.0, 1], [191.0, 1], [8.0, 1], [9.0, 1], [9.0, 1], [10.0, 1], [187.0, 1], [9.0, 1], [189.0, 1], [190.0, 1], [96.0, 1], [319.0, 1], [36.0, 1], [89.0, 1], [11.0, 1], [8.0, 1], [11.0, 1], [7.0, 1], [9.0, 1], [9.0, 1], [189.0, 1], [189.0, 1], [8.0, 1], [9.0, 1], [10.0, 1], [325.0, 1], [189.0, 1], [188.0, 1], [9.0, 1], [345.0, 1]]
# #anglearr = [elem[0] for elem in anglearr]
# arr1 = [elem for elem in anglearr if elem < 180]
# arr2 = [elem for elem in anglearr if elem >= 180]
# #print(sum(anglearr)/len(anglearr))
# print(len(arr1))
# print(len(arr2))
# #arr2 = [elem for ]
# print(anglearr)
# #print(np.cos(np.pi*90/180))
# print(BCCal(arr1))
# print(BCCal(arr2))
# print(BCCal(anglearr))
#
# angle = [85.58574700962049, 262.1222544967792]
# y = (np.sin(np.pi*angle[0]/180)*31 + np.sin(np.pi*angle[1]/180)*25)/56
# x = (np.cos(np.pi*angle[0]/180)*31 + np.cos(np.pi*angle[1]/180)*25)/56
# print(y,x)
# print((atan2(y,x)))

#print(-35%360)
#print(sum([angle+1 for angle in anglearr]))
# anglearr = [0,0,0,180,180,180,180,180,180,180,180,180,180,180,180]
# print(BCCal(anglearr))
#anglearr = [[288.0, 1], [102.0, 1], [95.0, 1], [251.0, 1], [259.0, 1], [355.0, 1], [256.0, 1], [259.0, 1], [89.0, 1], [106.0, 1], [104.0, 1], [242.0, 1], [275.0, 1], [274.0, 1], [89.0, 1], [92.0, 1], [270.0, 1], [254.0, 1], [96.0, 1], [86.0, 1], [277.0, 1], [259.0, 1], [92.0, 1], [273.0, 1], [90.0, 1], [91.0, 1], [29.0, 1], [288.0, 1], [95.0, 1], [80.0, 1], [272.0, 1], [87.0, 1], [355.0, 1], [282.0, 1], [77.0, 1], [82.0, 1], [95.0, 1], [80.0, 1], [275.0, 1], [283.0, 1], [275.0, 1], [79.0, 1], [90.0, 1], [286.0, 1], [272.0, 1], [81.0, 1], [82.0, 1], [94.0, 1], [273.0, 1], [112.0, 1], [86.0, 1]]
#anglearr = [elem[0] for elem in anglearr]

#anglearr = [[308.0, 1], [283.0, 1], [141.0, 1], [140.0, 1], [120.0, 1], [296.0, 1], [122.0, 1], [137.0, 1], [297.0, 1], [304.0, 1], [312.0, 1], [119.0, 1], [122.0, 1], [312.0, 1], [127.0, 1], [121.0, 1], [120.0, 1], [161.0, 1], [332.0, 1], [303.0, 1], [302.0, 1], [119.0, 1], [184.0, 1], [129.0, 1], [308.0, 1], [111.0, 1], [129.0, 1], [307.0, 1], [128.0, 1], [339.0, 1], [299.0, 1], [316.0, 1], [271.0, 1], [299.0, 1], [209.0, 1], [96.0, 1], [301.0, 1], [124.0, 1], [140.0, 1], [106.0, 1], [125.0, 1], [152.0, 1], [300.0, 1]]

#anglearr = [[99.0, 1], [96.0, 1], [98.0, 1], [99.0, 1], [279.0, 1], [287.0, 1], [295.0, 1], [287.0, 1], [279.0, 1], [279.0, 1], [100.0, 1], [102.0, 1], [311.0, 1], [277.0, 1], [279.0, 1], [96.0, 1], [277.0, 1], [287.0, 1], [99.0, 1], [99.0, 1], [99.0, 1], [280.0, 1], [99.0, 1], [99.0, 1], [275.0, 1], [279.0, 1], [271.0, 1], [279.0, 1], [202.0, 1], [97.0, 1], [105.0, 1], [96.0, 1], [311.0, 1], [277.0, 1], [99.0, 1], [96.0, 1], [277.0, 1], [99.0, 1]]

#anglearr = [[107.0, 1], [90.0, 1], [146.0, 1], [326.0, 1], [265.0, 1], [235.0, 1], [284.0, 1], [182.0, 1], [38.0, 1], [302.0, 1], [233.0, 1], [357.0, 1], [283.0, 1], [256.0, 1], [66.0, 1], [276.0, 1], [256.0, 1], [97.0, 1], [91.0, 1], [90.0, 1], [90.0, 1], [146.0, 1], [326.0, 1], [235.0, 1], [87.0, 1], [103.0, 1], [92.0, 1], [182.0, 1], [38.0, 1], [108.0, 1], [233.0, 1], [357.0, 1], [287.0, 1], [356.0, 1], [66.0, 1], [276.0, 1], [77.0, 1]]
#anglearr =
#anglearr = [[182.0, 1], [85.0, 1], [193.0, 1], [283.0, 1], [174.0, 1], [159.0, 1], [347.0, 1], [341.0, 1], [60.0, 1], [93.0, 1], [154.0, 1], [112.0, 1], [183.0, 1], [209.0, 1], [84.0, 1], [182.0, 1], [296.0, 1], [94.0, 1], [76.0, 1], [256.0, 1], [127.0, 1], [272.0, 1], [348.0, 1], [267.0, 1], [174.0, 1], [159.0, 1], [347.0, 1], [341.0, 1], [60.0, 1], [1.0, 1], [21.0, 1], [257.0, 1], [112.0, 1], [342.0, 1], [15.0, 1], [333.0, 1], [349.0, 1]]

#anglearr = [[134.0, 1], [130.0, 1], [143.0, 1], [30.0, 1], [201.0, 1], [168.0, 1], [137.0, 1], [130.0, 1], [150.0, 1], [286.0, 1], [142.0, 1], [332.0, 1], [142.0, 1], [149.0, 1], [260.0, 1], [121.0, 1], [14.0, 1], [294.0, 1], [313.0, 1], [272.0, 1], [30.0, 1], [128.0, 1], [168.0, 1], [147.0, 1], [306.0, 1], [150.0, 1], [310.0, 1], [124.0, 1], [262.0, 1], [332.0, 1], [296.0, 1], [149.0, 1], [260.0, 1]]
#anglearr = [[29.0, 1], [271.0, 1], [137.0, 1], [75.0, 1], [147.0, 1], [147.0, 1], [191.0, 1], [254.0, 1], [272.0, 1], [144.0, 1], [310.0, 1], [288.0, 1], [286.0, 1], [91.0, 1], [335.0, 1], [147.0, 1], [88.0, 1], [90.0, 1], [272.0, 1], [271.0, 1], [147.0, 1], [356.0, 1], [150.0, 1], [147.0, 1], [250.0, 1], [191.0, 1], [274.0, 1], [90.0, 1], [151.0, 1], [310.0, 1], [288.0, 1], [41.0, 1], [86.0, 1], [154.0, 1], [324.0, 1]]

#anglearr = [[51.0, 1], [216.0, 1], [53.0, 1], [97.0, 1], [26.0, 1], [2.0, 1], [225.0, 1], [190.0, 1], [90.0, 1], [270.0, 1], [47.0, 1], [80.0, 1], [117.0, 1], [51.0, 1], [230.0, 1], [230.0, 1], [234.0, 1], [50.0, 1], [277.0, 1], [56.0, 1], [224.0, 1], [53.0, 1], [90.0, 1], [270.0, 1], [285.0, 1], [80.0, 1], [295.0, 1]]

anglearr = [ [330.0, 1], [344.0, 1], [241.0, 1], [288.0, 1], [264.0, 1], [242.0, 1], [66.0, 1], [75.0, 1], [66.0, 1], [318.0, 1], [316.0, 1], [67.0, 1], [333.0, 1], [22.0, 1], [264.0, 1], [138.0, 1], [288.0, 1], [171.0, 1], [242.0, 1], [66.0, 1], [241.0, 1], [68.0, 1], [248.0, 1], [251.0, 1], [198.0, 1], [254.0, 1], [279.0, 1]]

anglearr = [[135.0, 1], [33.0, 1], [136.0, 1], [90.0, 1], [305.0, 1], [317.0, 1], [314.0, 1], [334.0, 1], [120.0, 1], [216.0, 1], [316.0, 1], [132.0, 1], [135.0, 1], [61.0, 1], [137.0, 1], [135.0, 1], [33.0, 1], [309.0, 1], [90.0, 1], [305.0, 1], [318.0, 1], [58.0, 1], [291.0, 1], [318.0, 1], [281.0, 1], [132.0, 1], [315.0, 1]]
anglearr = [elem[0] for elem in anglearr]
print(anglearr)
anglearr = [135,134,132,132,140,133,133,135,320,325,326,327,327,325,328,328]
anglearr = [0,45,90,135,180,225,270,315,360,0,45,90,135,180,225,270,315,360,0,45,90,135,180,225,270,315,360,0,45,90,135,180,225,270,315,360,0,45,90,135,180,225,270,315,360,0,45,90,135,180,225,270,315,360,0,45,90,135,180,225,270,315,360,0,45,90,135,180,225,270,315,360,0,45,90,135,180,225,270,315,360,0,45,90,135,180,225,270,315,360,]
anglearr = [80,80,80,80,80,80,80,80,80,180,180,180,180,180,180,180,180,80,80,80,80,80,80,80,80,80,180,180,180,180,180,180,180,180,80,80,80,80,80,80,80,80,80,180,180,180,180,180,180,180,180,80,80,80,80,80,80,80,80,80,180,180,180,180,180,180,180,180]
anglearr = [80,80,80,80,80,80,80,80,80,180,180,180,180,180,180,180,180,80,80,80,80,80,80,80,80,80,180,180,180,180,180,180,180,180,80,80,80,80,80,80,80,80,80,180,180,180,180,180,180,180,180,80,80,80,80,80,80,80,80,80,180,180,180,180,180,180,180,180,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,270,520,520,520]
print(BCCal(anglearr))
