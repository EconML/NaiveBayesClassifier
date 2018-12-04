"""
Script to evaluate Naive Bayes Classifier predictions

"""
import sys

def EvaNB(predictionLabel, realLabel):
    """
    compares line by line,
    and calculates how many predictions are correct,

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
    if(not CheckInput(sys.argv)):
        sys.exit(0)
    EvaNB(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
