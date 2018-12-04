"""
 Script to test trained Naive Bayes Classifier

"""
import sys

def NBtest(data, model, prediction):
    """
    Loads saved model file, and also loads testing data TestDataNoLabel.txt,
    then applies the trained model to make predictions.
    Finally, saves predictions in prediction file,
    ...
    """
    r,c = 10,2
    train_outlook = [0] * r
    train_temp = [0] * r
    train_humidity = [0] * r
    train_wind = [0] * r
    for i in range(r):
        train_outlook[i] = [0] * c
        train_temp[i] = [0] * c
        train_humidity[i] = [0] * c
        train_wind[i] = [0] * c
    with open(model) as f:
        train_total = float(f.readline())
        train_play = float(f.readline())
        for i in range(r):
            curTrainingExample = [int(k) for k in f.readline().split()]
            for j in range(c):
                train_outlook[i][j] = curTrainingExample.pop(0)
        for i in range(r):
            curTrainingExample = [int(k) for k in f.readline().split()]
            for j in range(c):
                train_temp[i][j] = curTrainingExample.pop(0)
        for i in range(r):
            curTrainingExample = [int(k) for k in f.readline().split()]
            for j in range(c):
                train_humidity[i][j] = curTrainingExample.pop(0)
        for i in range(r):
            curTrainingExample = [int(k) for k in f.readline().split()]
            for j in range(c):
                train_wind[i][j] = curTrainingExample.pop(0)
        # print(str(train_outlook)+'\n')
        # print(str(train_temp)+'\n')
        # print(str(train_humidity)+'\n')
        # print(str(train_wind)+'\n')

    with open(data, 'r') as fdata:
        with open(prediction, 'w') as fpred:
            for line in fdata:
                curTestingExample = [int(i) for i in line.split()]
                cur_play = curTestingExample.pop(0)
                cur_outlook = curTestingExample.pop(0)
                cur_temp = curTestingExample.pop(0)
                cur_humidity = curTestingExample.pop(0)
                cur_wind = curTestingExample.pop(0)

                #calculate the probabilities of yes and no
                prob_yes = (train_outlook[cur_outlook-1][0]/train_total)*(train_temp[cur_temp-1][0]/train_total)*(train_humidity[cur_humidity-1][0]/train_total)*(train_wind[cur_wind-1][0]/train_total)*(train_play/train_total)
                prob_no = (train_outlook[cur_outlook-1][1]/train_total)*(train_temp[cur_temp-1][1]/train_total)*(train_humidity[cur_humidity-1][1]/train_total)*(train_wind[cur_wind-1][1]/train_total)*(1-(train_play/train_total))
                print(str(prob_yes) + ' ' + str(prob_no) + '\n')

                if(prob_yes>prob_no):
                    fpred.write(str(1)+'\n')
                else:
                    fpred.write(str(0)+'\n')



def CheckInput(argvs):
    """
    This function will check the input. This program tests the Naive Bayesian Model on data TestDataNoLabel.txt. There should be two parameters for testing data and saved model
    """
    if len(sys.argv) < 4:
        print("You should give at least three parameters for path of input testing file and trained NB model. For example:\n")
        print("python "+sys.argv[0]+" TestDataNoLabel.txt NB.model LabelPrediction.txt")
        return False
    return True

def main():
    if(not CheckInput(sys.argv)):
        sys.exit(0)
    NBtest(sys.argv[1], sys.argv[2], sys.argv[3])


if __name__ == "__main__":
    main()
