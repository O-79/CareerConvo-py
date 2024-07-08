from typing import List
from CTree import CTree
from Manager import Manager
import re

class Control:
    MENU = ""
    
    Q_SIZ = "* Size of responses ? (4 [Faster] - 16 [Slower])"
    
    Q_INS = "* In-state colleges only? (0 [No] / 1 [Yes])"

    Q_LOC = "* Enter your current / desired location"

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
        MGR = Manager()
        CAREER_TREE = CTree()
        COLLEGE_INFO: List[Manager.College_Info] = []

        X = 0
        print(Control.Q_SIZ)
        try:
            X = int(input())
            if X < 4:
                X = 4
            if X > 16:
                X = 16
        except ValueError:
            X = 10
        
        INS = -1 # 0: OOS , 1: INS
        print(Control.Q_INS)
        try:
            INS = int(input())
            if INS != 0 and INS != 1:
                INS = 1
        except ValueError:
            INS = 1
        
        MGR.INIT(X, INS)

        print(Control.MENU, end='')

        CMD = "loc"
        while CMD.lower() not in ["quit", "exit", "q"]:
            INF = None

            if CMD.lower() in ["loc", "location", "l"]:
                INF = Control.CMD_LOC(CAREER_TREE, X, MGR)

            if CMD.lower() in ["car", "career", "c"]:
                INF = Control.CMD_CAR(CAREER_TREE, X, MGR)

            if CMD.lower() in ["job", "position", "j"]:
                INF = Control.CMD_JOB(CAREER_TREE, X, MGR)

            if CMD.lower() in ["col", "college", "uni", "university", "u"]:
                INF = Control.CMD_COL(CAREER_TREE, X, MGR)

            if INF:
                COLLEGE_INFO.append(INF)

            print("\n>", end=" ")
            CMD = input()

        print(f"\n{Control.DSH('TREE')}\n{CAREER_TREE.LST()}\n{Control.DSH('')}")

        print(f"\n{Control.DSH('COLLEGE REPORT')}")
        if not COLLEGE_INFO:
            print("no colleges\n" + Control.DSH(''))
        for I in COLLEGE_INFO:
            print(f"NAME:       {I.GET_COL()}")
            print(f"LOCATION:   {I.GET_LOC()}")
            print(f"DEGREE:     {I.GET_DEG()}")
            print(f"CAREER:     {I.GET_CAR()}")
            print(f"JOB:        {I.GET_JOB()}")
            print(f"TUITION:    {I.GET_TUT()}") # include total expenses
            print(f"LOAN:       {I.GET_LON()} (avg.)") # WIP
            print(f"REPAY IN:   {I.GET_MTH_PAY()} months (est.)") # WIP
            # print(f"PROGRAMS:   {I.GET_LON_OPP()}") # WIP
            print(Control.DSH(''))

if __name__ == "__main__":
    Control.main()