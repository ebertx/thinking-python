def print2by2Grid():
    printHorizontalBorder(2)
    printGap(2)
    printHorizontalBorder(2)
    printGap(2)
    printHorizontalBorder(2)

def print4by4Grid():
    printHorizontalBorder(4)
    printGap(4)
    printHorizontalBorder(4)
    printGap(4)
    printHorizontalBorder(4)
    printGap(4)
    printHorizontalBorder(4)
    printGap(4)
    printHorizontalBorder(4)

def printHorizontalBorder(width):
    border = '+ - - - '
    end = '+'
    print border * width + end

def printGap(width):
    gap = '|       '
    end = '|'
    print gap * width + end
    print gap * width + end
    print gap * width + end
    print gap * width + end

print2by2Grid()
print4by4Grid()