def selection_Sort():
    global barList
    global lengthList

    for i in range(len(lengthList)):
        min = i
        for j in range(i + 1, len(lengthList)):
            if (lengthList[j] < lengthList[min]):
                min = j
        lengthList[min], lengthList[i] = lengthList[i], lengthList[min]
        barList[min], barList[i] = barList[i], barList[min]
        swap(barList[min], barList[i])
        yield