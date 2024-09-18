#!/usr/bin/python3
"""simultaneous equation calculator"""
import numpy as np

def sim():
    """calculates simultaneous equation"""
    print("----- Welcome to Math solver ------")
    get_cont = "yes"
    while get_cont == "yes":
        try:
            getNumberOfEqns = int(input("Enter number of equations: "))
            if getNumberOfEqns < 1:
                print("Error: Number of equations must be greater than 1")
                return
            getVarnum = int(input("How many number of unknowns?: "))
            holdGetVar = input("Enter your unknown variables; e.g <x,y,z>: ")
            getVar = holdGetVar.split(',')

        except (TypeError, ValueError):
            print("Syntax Error")
            return
        
        crammer = []
        equalTo = []
        
        for i in range(1, getNumberOfEqns + 1):
            get_unknown = []
            for j in range(1, getVarnum + 1):
                try:
                    coeff = int(input(f"Enter the coefficient of {getVar[j - 1]} of equation {i}: "))
                except (TypeError, ValueError):
                    print("Syntax Error")
                    return
                get_unknown.append(coeff)
            getequal = int(input("Equals to: "))
            equalTo.append(getequal)
            crammer.append(get_unknown)
        
        delta = np.linalg.det(crammer)
        if delta == 0:
            print("No solution")
            return

        if getNumberOfEqns == 2:
            # Solve for two variables
            first_var = np.linalg.det([[equalTo[0], crammer[0][1]],
                                    [equalTo[1], crammer[1][1]]])

            second_var = np.linalg.det([[crammer[0][0], equalTo[0]],
                                        [crammer[1][0], equalTo[1]]])

            first_var /= delta
            second_var /= delta
            print(f"The value of {getVar[0]} is {first_var}")
            print(f"The value of {getVar[1]} is {second_var}")
        
        elif getNumberOfEqns == 3:
            # Solve for three variables
            first_var = np.linalg.det([[equalTo[0], crammer[0][1], crammer[0][2]],
                                    [equalTo[1], crammer[1][1], crammer[1][2]],
                                    [equalTo[2], crammer[2][1], crammer[2][2]]])

            second_var = np.linalg.det([[crammer[0][0], equalTo[0], crammer[0][2]],
                                        [crammer[1][0], equalTo[1], crammer[1][2]],
                                        [crammer[2][0], equalTo[2], crammer[2][2]]])

            third_var = np.linalg.det([[crammer[0][0], crammer[0][1], equalTo[0]],
                                    [crammer[1][0], crammer[1][1], equalTo[1]],
                                    [crammer[2][0], crammer[2][1], equalTo[2]]])

            first_var /= delta
            second_var /= delta
            third_var /= delta
            print(f"The value of {getVar[0]} is {first_var}")
            print(f"The value of {getVar[1]} is {second_var}")
            print(f"The value of {getVar[2]} is {third_var}")
        get_cont = input("Do you wish to continue <Yes/No>: ")
        get_cont.lower()


if __name__ == "__main__":
    sim()
