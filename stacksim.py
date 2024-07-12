import os



def prRed(skk): print("\033[91m {}\033[00m".format(skk))


def prGreen(skk): print("\033[92m {}\033[00m".format(skk))


def prYellow(skk): print("\033[93m {}\033[00m".format(skk))


def prLightPurple(skk): print("\033[94m {}\033[00m".format(skk))


def prPurple(skk): print("\033[95m {}\033[00m".format(skk))


def prCyan(skk): print("\033[96m {}\033[00m".format(skk))


def prLightGray(skk): print("\033[97m {}\033[00m".format(skk))


def prBlack(skk): print("\033[98m {}\033[00m".format(skk))



RSP = 0xFFFF0000
RBP = 0xFFFF0000

startingInput = input("Memory address of the stack?   ")

if (startingInput != ""):
    RSP = int(startingInput, 16)
    RBP = int(startingInput, 16)


stackHeight = 1

stack = {

    RBP: "RBP",
}

while (True):

    os.system('cls' if os.name == 'nt' else 'clear')

    print("\n\n\n\n\n\n\n\n\n\n")
    prYellow("    Stack\n -------------------------------")


    listOfKeys = stack.keys()

    lastKey = RBP

    for key in listOfKeys:

        if (lastKey != key - 1) and (lastKey != key + 1) and (lastKey != key):
            prPurple(" ............... ")
            prYellow("-------------------------------")
            prCyan("  " + hex(key) + "    " + stack[key])
            prYellow("-------------------------------")
        else:
            prCyan("  " + hex(key) + "    " + stack[key])
            prYellow("-------------------------------")

        lastKey = key
    command = input("Push, Pop, or Mov?  ")

    push = False
    pop = False
    mov = False

    if command[0:4] == "push" or command[0:4] == "Push" or command[0:4] == "PUSH":
        push = True

    if command[0:3] == "pop" or command[0:3] == "Pop" or command[0:3] == "POP":
        pop = True

    if command[0:3] == "mov" or command[0:3] == "Mov" or command[0:3] == "MOV":
        mov = True

    if mov or push or pop:

        if push:
            right = input("Input Value (Right)?  ")
            stack[RSP - 0x00000001] = (right)
            RSP -= 1
        if pop:
            stack.pop(RSP)
            RSP += 1
        if mov:
            right = input("Input Value (Right)?  ")
            left = input("Destination (Left)?  0x")

            '''if left == "rsp" or left == "RSP" or left == "Rsp":
                try:
                    RSP = int(right)
                except: 
                    print("RSP input was not a number.")'''
            try:
                stack[int(left, 16)] = (right)
            except:
                print("\nBad Input")
    else:
        print("Bad Input")
    #os.system('cls')
