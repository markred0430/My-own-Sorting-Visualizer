def _comb_sort():
    global barList
    global lengthList

    n = len(lengthList)
    gap = n
    shrink = 1.3
    sorted = False
    while not sorted:
        gap = int(gap / shrink)
        if gap > 1:
            sorted = False
        else:
            gap = 1
            sorted = True

        i = 0
        while i + gap < n:
            if lengthList[i] > lengthList[i + gap]:
                lengthList[i], lengthList[i + gap] = lengthList[i + gap], lengthList[i]
                barList[i], barList[i + gap] = barList[i + gap], barList[i]
                swap(barList[i], barList[i + gap])
                sorted = False
                yield
            else:
                colorBar(barList[i], "white")
            i = i + 1