"""
 Name: Your Name
 Assignment: Lab 3
 Course: CS 330
 Semester: Fall 2018
 Instructor: Dr. Cao
 Date: the current date
 Sources consulted: any books, individuals, etc consulted

 Known Bugs: description of known bugs and other program imperfections

 Creativity: anything extra that you added to the lab

 Instructions: special instructions to user on how to execute your program

"""
import sys

def EvaNB(predictionLabel, realLabel):
    """
    This is the main function you need to implement.
    You should compare line by line,
    and calculate how many predictions are correct,
    how many predictions are not correct. The output could be:

    In total, there are ??? predictions. ??? are correct, and ??? are not correct.

    """
    pred = 0
    correct = 0
    incorrect = 0

    fReal = open(realLabel, 'r')
    with open(predictionLabel, 'r') as f:
        for line in f:
            pred += 1
            if int(line) == int(fReal.readline()):
                correct += 1
            else:
                incorrect += 1
    print('In total, there are ' + str(pred) + ' predictions. ' + str(correct) + ' are correct, and ' + str(incorrect) + ' are incorrect.')


def CheckInput(argvs):
    """
    This function will check the input. This program is going to evaluate the accuracy of your prediction. You should compare two files: LabelPrediction.txt which is predicted by your model, and LabelForTest.txt is the true label, caculate the precision.
    """
    if len(sys.argv) < 3:
        print("You should give at least two parameters for path of prediction and real labels. For example:\n")
        print("python "+sys.argv[0]+" LabelPrediction.txt LabelForTest.txt")
        return False
    return True

def main():
    # hint, the following codes are for your testing.
    if(not CheckInput(sys.argv)):
        sys.exit(0)
    EvaNB(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
