x = 1007
y = 1079

def numbersCalls(x, y):
    _basisCell = 1
    _callsY = y - 1000
    _callsX = x - 1000

    if _callsX >= _callsY: _callsX += _basisCell
    if _callsX < _callsY: _callsY += _basisCell

    print("Пройдено по оси 'X' %s, по оси 'Y' %s. Всего %s клеток." %(_callsX, _callsY, _callsX + _callsY))
    return

def sumDigits(x, y):
    totalSum = 0
    if x >= 1000 and y >= 1000:
        for digit in str(x) + str(y):
            totalSum += int(digit)
            if totalSum > 25:
                print ('Муравью сюда закрыто')
                return

    print("Муровей собрал %s бал(ов). Может собрать еще %s бал(ов)." % (totalSum, 25 - totalSum))
    numbersCalls(x, y)
    return





if __name__ == '__main__':
    sumDigits(x, y)


