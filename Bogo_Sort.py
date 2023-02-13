def bogo_Sort():
    global barList
    global lengthList

    n = len(lengthList)
    gap = n

    def is_sorted(lengthList):
        for i in range(0,n-1):
            if lengthList[i] > lengthList[i+1]:
                return False
        return True

    while not is_sorted(lengthList):
        for i in range(0,n-1):
            if lengthList[i] < lengthList[i+1]:
                lengthList[i], lengthList[i] = lengthList[i -1], lengthList[i]
                barList[i], barList[i -1] = barList[i  -1], barList[i]
                random.shuffle(lengthList)
                swap(barList[i], barList[i -1])
                yield
            else:
                colorBar(barList[i], "white")
            i = i + 1