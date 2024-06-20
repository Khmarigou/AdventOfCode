def isNumber(i):
    if i in '0123456789':
        return True


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        result = 0
        for line in f :
            num = ''
            for i in line :
                if isNumber(i) :
                    num += i
                    break
            for i in line[::-1] :
                if isNumber(i) :
                    num += i
                    break
            result += int(num)
        print(result)