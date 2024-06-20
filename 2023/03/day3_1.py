def readInput() :
    lines = []
    with open('input.txt', 'r') as f:
        for line in f:
            lines.append(line.rstrip())
    return lines

def getArea(number, input) :
    xmin = number["x"][0]-1
    xmax = number["x"][1]+1
    ymin = number["y"]-1
    ymax = number["y"]+2
    xmin = 0 if xmin < 0 else xmin
    xmax = len(input[0]) if xmax > len(input[0]) else xmax
    ymin = 0 if ymin < 0 else ymin
    ymax = len(input) if ymax > len(input) else ymax
    return xmin, xmax, ymin, ymax

def getNumbers(line, y) :
    numbers = []
    find = False
    for x in range(len(line)) :
        if find :
            if not line[x].isnumeric() :
                end = x
                find = False
                numbers.append({"num":int(line[start:end]), "x":[start, end], "y":y})
            elif x == len(line)-1 :
                end = x+1
                find = False
                numbers.append({"num":int(line[start:end]), "x":[start, end], "y":y})
        else :
            if line[x].isnumeric() :
                start = x
                find = True
    return numbers

if __name__ == '__main__':
    input = readInput()
    result = 0
    numbers = []
    for y in range(len(input)):
        numbersLine = getNumbers(input[y], y)
        if len(numbersLine) > 0:
            numbers.extend(numbersLine)
    for number in numbers:
        xmin, xmax, ymin, ymax = getArea(number, input)
        numberValide = False
        for y in range(ymin, ymax):
            for x in range(xmin, xmax):
                if (not input[y][x].isnumeric()) and input[y][x] != '.':
                    numberValide = True
                    break
            if numberValide:
                break
        if numberValide:
            result += number["num"]
    print(result)