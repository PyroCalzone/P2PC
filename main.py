#Python 2 Pseudo-Code:
#    A python script to convert another file of Python to Pseudo-code based on CSP Exam Reference Sheet.
#    https://apcentral.collegeboard.org/media/pdf/ap-computer-science-principles-exam-reference-sheet.pdf

#Assignment, Display, and Input
    # a ← expression
    # DISPLAY(expression)
    # INPUT()

#Arithmetic Operators and Numeric Procedures
    # +, -, *, /, MOD
    # RANDOM(a, b) a, b inclusive

#Rational and Boolean Operators
    # Operators
        # =, ≠, >, <, ≥, ≤
    # Conditional Keywords
        # NOT, AND, OR, 

#Selection
    # IF(condition){}
    # ELSE{}

#Iteration
    # REPEAT n TIMES{}
    # REPEAT UNTIL(condition){}

#List Operations (Index at 1)
    # aList ← [Value1, Value2, ...]
    # INSERT(list, index, value)
    # APPEND(list, value)
    # REMOVE(list, index)
    # LENGTH(list)
    # FOR EACH item IN list{}

#Procedures and Procedure Calls
    # PROCEDURE name(parameter, ...) {}
    # RETURN(expression)

import regex as re

def addIndentation(level):
    return (' '*(4*level))

def conversion(word):
    if word == '=':
        return ('←')
    elif word == 'print':
        return ('DISPLAY')
    elif word == 'input':
        return ('INPUT')
    elif word == '%':
        return ('MOD')
    elif word == 'random.randint' or word == 'randint':
        return ('RANDOM')
    elif word == '==':
        return ('=')
    elif word == '!=':
        return ('≠')
    elif word == '>=':
        return ('≥')
    elif word == '<=':
        return ('≤')
    elif word == 'not':
        return ('NOT')
    elif word == 'and':
        return ('AND')
    elif word == 'or':
        return ('OR')
    elif word == 'return':
        return ('RETURN')
    else:
        return (word)

def newIndentWords(specialWord, line):
    #Use regex to split by just colons
    split = re.split('(\s+|:)', line)
    split = [word for word in split if word != '']
    #Find the index of the colon
    colonIndex = split.index(':')
    ifIndex = split.index(specialWord)
    conditional = split[ifIndex+2:colonIndex]
    for index, word in enumerate(conditional):
        conditional[index] = conversion(word)
    
    return conditional

def elifHandler(line):
    global newIndentLevel
    #Write ELSE, then create a new line with a higher indentation level, with the IF statement.
    elifIndent = newIndentWords('elif', line)
    tempList2 = ['ELSE\n', addIndentation(newIndentLevel) + '{\n']
    newIndentLevel += 0
    tempList = [addIndentation(newIndentLevel+1) + 'IF(', *elifIndent, ')']
    for x in tempList:
        tempList2.append(x)
    return (tempList2)
    
def indentHandler(oldIndent, newIndent):
    global newIndentLevel
    if oldIndent < newIndent:
        return (['\n' + addIndentation(newIndent-1) + '{\n'])
    elif oldIndent > newIndent:
        indent = []
        while oldIndent > newIndent:
            indent.append(addIndentation(oldIndent-1) + '}\n')
            oldIndent -= 1
        return(indent)
    else:
        return ([''])

lines = []

with open('test.py', 'r', encoding='utf-8') as file:
    #Remove any empty lines or if the line starts with a #
    file = [line for line in file if line.strip() != '' and line[0] != '#']
    #file = [re.sub('^\s*', '', line) for line in file] #remove leading whitespace
    oldIndentLevel = 0
    newIndentLevel = 0
    for line in file:
        #use regex to find indentation
        indent = re.search('^\s*', line)
        indent = indent.group(0)
        newIndentLevel = len(indent) // 4
        print(newIndentLevel)


        words = re.split('(\s+|\(|\))', line) #Split by spaces, and parentheses
        words = [word for word in words if word != ''] #Remove empty strings
        words = [conversion(word) for word in words] #Convert words

        currentLine = []
        #Check the indentation level
        indentations = indentHandler(oldIndentLevel, newIndentLevel)
        for indent in indentations:
            currentLine.append(indent)

        for word in words:
            if word == 'if':
                conditional = newIndentWords('if', line)                
                tempList = ['IF(', *conditional, ')']
                for x in tempList:
                    currentLine.append(x)
                break
            elif word == 'elif':
                print(newIndentLevel)
                handler = elifHandler(line)
                for x in handler:
                    currentLine.append(x)
                break
            elif word == 'def':
                procedure = newIndentWords('def', line)
                tempList = ['PROCEDURE ', *procedure, '']
                for x in tempList:
                    currentLine.append(x)
                break
            else:
                currentLine.append(word)
        print(currentLine)
        currentLine = ''.join(currentLine)
        lines.append(currentLine)
        oldIndentLevel = newIndentLevel
    
    indentations = indentHandler(oldIndentLevel, 0)
    alreadyIndented = False
    for indent in indentations:
        check = re.search('^\s*', indent)
        check = check.group(0)
        check = len(check) // 4
        if check != 0 and alreadyIndented == False:
            indent = '\n' + indent
            alreadyIndented = True
        lines.append(indent)

with open('output.txt', 'w', encoding='utf-8') as file:
    for line in lines:
        file.write(line)
