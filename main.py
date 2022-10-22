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

from re import fullmatch
import regex as re

lines = []

with open('test.py', 'r') as file:
    for line in file:
        words = re.split('(\s+|\(|\))', line) #Split by spaces, and parentheses
        words = [word for word in words if word != ''] #Remove empty strings
        print(words)
        currentLine = []
        for word in words:
            if word == '=':
                currentLine.append('←')
            elif word == 'print':
                currentLine.append('DISPLAY')
            elif word == 'input':
                currentLine.append('INPUT')
            elif word == '%':
                currentLine.append('MOD')
            elif word == 'random.randint':
                currentLine.append('RANDOM')
            elif word == '!=':
                currentLine.append('≠')
            elif word == '>=':
                currentLine.append('≥')
            elif word == '<=':
                currentLine.append('≤')
            elif word == 'not':
                currentLine.append('NOT')
            elif word == 'and':
                currentLine.append('AND')
            elif word == 'or':
                currentLine.append('OR')
            elif word == 'if':
                #Use regex to split by just colons
                split = re.split('(\s+|:)', line)
                split = [word for word in split if word != '']
                #Find the index of the colon
                colonIndex = split.index(':')
                ifIndex = split.index('if')
                
                tempList = ['IF(', *split[ifIndex+2:colonIndex], ') {\n']
                for x in tempList:
                    currentLine.append(x)
                print(currentLine)
                break
            elif word == 'def':
                currentLine.append('PROCEDURE')
            elif word == 'return':
                currentLine.append('RETURN')
            else:
                currentLine.append(word)
        currentLine = ''.join(currentLine)
        lines.append(currentLine)

with open('output.txt', 'w', encoding='utf-8') as file:
    for line in lines:
        file.write(line)
