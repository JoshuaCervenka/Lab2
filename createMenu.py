def createMenu(optionList):
    output = "" 
    ct = 0
    for el in optionList:
        ct += 1
        output += '\n'
        output += str(ct)
        output += ".) "
        output += el
        output += '\n'
    return output
