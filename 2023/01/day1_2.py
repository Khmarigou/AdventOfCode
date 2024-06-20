import re

def convert(num) :
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    if num in numbers :
        return numbers.index(num)
    else :
        return int(num)

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        result = 0
        for line in f:
            reg1 = re.compile('([0-9]|one|two|three|four|five|six|seven|eight|nine)')
            num1 = reg1.search(line)
            reversedLine = line[::-1]
            reg2 = re.compile('([0-9]|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)')
            num2 = reg2.search(reversedLine)
            num1 = convert(num1.group())
            num2 = convert(num2.group()[::-1])
            result += num1 * 10 + num2
        print(result)