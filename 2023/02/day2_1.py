import re

if __name__ == '__main__':
    maxRed = 12
    maxGreen = 13
    maxBlue = 14
    result = 0
    with open('input.txt') as f:
        for line in f:
            match = re.match(r"Game (\d+): (.*)", line)
            game = int(match.group(1))
            gamePossible = True
            if match:
                rounds = match.group(2).split("; ")
                for round in rounds:
                    red = re.search("(\d+) red", round)
                    green = re.search("(\d+) green", round)
                    blue = re.search("(\d+) blue", round)
                    if red:
                        if int(red.group(1)) > maxRed:
                            gamePossible = False
                    if green:
                        if int(green.group(1)) > maxGreen:
                            gamePossible = False
                    if blue:
                        if int(blue.group(1)) > maxBlue:
                            gamePossible = False
            if gamePossible:
                result += game
    print(result)
