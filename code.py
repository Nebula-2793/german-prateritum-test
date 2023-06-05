import random
import sys

from colorama import Fore, Style
cyan = Fore.CYAN
red = Fore.RED 
green = Fore.GREEN
reset = Style.RESET_ALL
magenta = Fore.MAGENTA
yel = Fore.YELLOW

wrong = []

def data():
    file = open(r"C:\Users\Amey\Desktop\coding\python\Prateritum\backBook.txt", mode='r')
    lines = file.read().splitlines()
    file.close()

    x = int(len(lines))

    prasens = [lines[n+4] for n in range(0, x-3, 4)]
    perfekt = [lines[n+4] for n in range(1, x-2, 4)]
    prateritum = [lines[n+4] for n in range(2, x-1, 4)]

    return prasens, perfekt, prateritum
  
def quiz_init(prasens, perfekt, prateritum):
    if len(prasens) != len(perfekt) or len(prasens) != len(prateritum):
        print(red + "Error: Number of Prasens, Perfekt, Prateritum not same")
        sys.exit()

    pop = input(cyan + "Type 1 or 2: \n 1.Perfekt  \n 2.Prateritum \n" + reset)
    if pop == '1':
        mode = "Perfekt"
        modeList = perfekt
        print('\n\n')
    elif pop == "2":
        mode = "Prateritum"
        print('\n\n')
        modeList = prateritum
    else:
        quiz_init(prasens, perfekt, prateritum)

    questionOrder = list(range(0, len(prasens)))
    random.shuffle(questionOrder)
    return questionOrder, mode, modeList
   
def quiz_result(questionOrder, answer, modeList, wrong):
    if answer == modeList[questionOrder[0]]:
        print(green + "Correct")
        del questionOrder[0]
        return questionOrder, wrong        
    else:
        if prasens[questionOrder[0]] not in wrong: wrong.append(prasens[questionOrder[0]])
        new_ans = '0'
        while new_ans != modeList[questionOrder[0]]:
            print(red + f"Wrong! The answer is {reset + modeList[questionOrder[0]]}")
            new_ans = input(red + f"Try Again: {reset}  \b")
        random.shuffle(questionOrder)
        return questionOrder, wrong   
  
def quiz_ask(mode, modeList):
        answer = input(cyan + f"What is the {reset + mode + cyan} form of {reset + prasens[questionOrder[0]]}? \b  {green}")
        return answer

print('\n\n' + cyan)
prasens, perfekt, prateritum = data()
questionOrder, mode, modeList = quiz_init(prasens, perfekt, prateritum)

while len(questionOrder) != 0:
    answer = quiz_ask(mode, modeList)
    questionOrder, wrong = quiz_result(questionOrder, answer, modeList, wrong)

print(f'\n {wrong}')
