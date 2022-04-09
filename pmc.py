stack = [''] * 50
accumulator = 0
pos = 0
state = 'on'
exitCode = 0

def LOAD(oper, val):
    global accumulator
    if oper == '$':
        accumulator = int(stack[val])

def STORE(oper, val):
    global stack
    if oper == '@':
        stack[val] = str(accumulator)

def JUMP(oper, val):
    global pos
    pos = val

def JNEG(oper, val):
    print(val)
    global pos
    if(accumulator < 0):
        pos = val

def SUB(oper, val):
    global accumulator
    accumulator = int(accumulator) - int(stack[val])


def ADD(oper, val):
    global accumulator
    accumulator = accumulator + int(stack[val])

def CLOG(oper, val):
    if val != -1:
        print("out: " + stack[val])
    else:
        print("out: " + str(accumulator))

def CIN(oper, val):
    global accumulator
    accumulator = input(": ")

def STOP(oper, val):
    global exitCode
    global state
    exitCode = str(val)
    state = 'off'

instructions = {
                'LOAD' : LOAD,
                'STORE' : STORE,
                'JUMP' : JUMP,
                'JNEG' : JNEG,
                'SUB' : SUB,
                'ADD' : ADD,
                'CLOG' : CLOG,
                'CIN' : CIN,
                'STOP' : STOP,
                }

def _generateMachine(path):
    with open(path, 'r') as file: data = file.read()
    data = data.split("\n")
    data.pop()
    if len(data) > 50:
        print("Too much data in input file!")
        return 1

    for index, element in enumerate(stack):
        stack[index] = data[index]

_generateMachine("text.txt")

def _loopMachine():
    global pos
    while state == "on":

        element = stack[pos]
        element = element.split(" ")
        if element[0] in instructions:
            oper = element[1]
            val = element[2]
            instructions[element[0]](oper, int(val))
            if exitCode != 0:
                return exitCode

        if pos >= 49: return "0"
        pos = pos + 1

if __name__ == "__main__":
    path = input("File to load: ")
    _generateMachine(path)
    print("\nFinished with exit code: " + _loopMachine())
