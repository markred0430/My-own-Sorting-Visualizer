def cocktail_shaker_Sort():
    global barList
    global lengthList

    n = len(lengthList)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if lengthList[i - 1] > lengthList[i]:
                lengthList[i - 1], lengthList[i] = lengthList[i], lengthList[i - 1]
                barList[i - 1], barList[i] = barList[i], barList[i - 1]
                swap(barList[i], barList[i - 1])
                swapped = True
                yield
            else:
                colorBar(barList[i - 1], "white")
        if swapped == False:
            return
        swapped = False
        for i in range(n - 1, 0, -1):
            if lengthList[i - 1] > lengthList[i]:
                lengthList[i - 1], lengthList[i] = lengthList[i], lengthList[i - 1]
                barList[i - 1], barList[i] = barList[i], barList[i - 1]
                swap(barList[i - 1], barList[i])
                swapped = True
                yield
            else:
                colorBar(barList[i], "white")