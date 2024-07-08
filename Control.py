from typing import List
from CTree import CTree
from Manager import Manager
from GPT import GPT
import re

class Control:
    MENU = ""
    
    Q_SIZ = "* Size of responses ? (4 [Faster] - 16 [Slower])"
    
    Q_INS = "* Great! Are you looking for only in-state colleges? (Y / N)"

    Q_LOC = "* Hi! What is your current / desired location?"

    Q_CAR = "* Choose one of the following careers (add / select)"

    Q_JOB = "* Choose one of the following jobs (add / select)"

    Q_COL = "* Choose one of the following colleges (add / select)"

    A_DEG = "* You will need the following degree: "

    A_PAY = "* Salary: "

    @staticmethod
    def DSH(TXT: str) -> str:
        if len(TXT) > 32:
            return "--------------------------------"

        TXT.replace(' ', '-')
        X = 32 - len(TXT)

        LIN = '-' * (X // 2) + TXT + '-' * (X // 2)
        if X % 2 == 1:
            LIN += '-'

        return LIN

    @staticmethod
    def main():
        CAREER_TREE = CTree()
        
        print(Control.Q_LOC)
        LOC = input()
        
        print(Control.Q_INS)
        INP_INS = input()
        INS = 1 if (INP_INS == "y" or INP_INS == "yes" or INP_INS == "1") else 0
        
        print(Control.MENU, end='')

        ANS = GPT.GET_ANS("I am a high school student looking for career counseling guidance, respond ONLY with a single question in the format 'Q: Question'")
        print("\n", ANS)
        CMD = ""
        while CMD.lower() not in ["quit", "exit", "q"]:
            print("\n>", end=' ')
            CMD = input()
            Q_FULL = CMD + ", respond ONLY with single question to learn more about me in the format 'Q: Question'"
            ANS = GPT.GET_ANS(CMD)
            print("\n", ANS)

if __name__ == "__main__":
    Control.main()