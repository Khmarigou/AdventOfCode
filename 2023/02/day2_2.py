import re

if __name__ == '__main__':
    with open('input.txt') as f:
        result = 0
        for line in f:
            maxRed = 0
            maxGreen = 0
            maxBlue = 0
            match = re.match(r"Game (\d+): (.*)", line)
            if match:
                rounds = match.group(2).split("; ")
                for round in rounds:
                    red = re.search("(\d+) red", round)
                    green = re.search("(\d+) green", round)
                    blue = re.search("(\d+) blue", round)
                    if red:
                        if int(red.group(1)) > maxRed:
                            maxRed = int(red.group(1))
                    if green:
                        if int(green.group(1)) > maxGreen:
                            maxGreen = int(green.group(1))
                    if blue:
                        if int(blue.group(1)) > maxBlue:
                            maxBlue = int(blue.group(1))
            result += maxRed * maxGreen * maxBlue
        print(result)