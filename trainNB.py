"""
Trains the Naive Bayes Classifier

"""
import sys

def train(data, model):
    """
    Reads TrainingData.txt, and calculates all probablities,
    then saves them as a model file.
    """

    play = 0
    total = 0
    r,c = 10,2
    outlook = [0] * r
    temp = [0] * r
    humidity = [0] * r
    wind = [0] * r
    for i in range(r):
        outlook[i] = [0] * c
        temp[i] = [0] * c
        humidity[i] = [0] * c
        wind[i] = [0] * c


    with open(data) as f:
        f.readline()
        for line in f:
            total +=1
            curTrainingExample = [int(i) for i in line.split()]
            cur_play = curTrainingExample.pop(0)
            cur_outlook = curTrainingExample.pop(0)
            cur_temp = curTrainingExample.pop(0)
            cur_humidity = curTrainingExample.pop(0)
            cur_wind = curTrainingExample.pop(0)
            if(cur_play):
                play +=1
                outlook[cur_outlook-1][0]+=1
                temp[cur_temp-1][0]+=1
                humidity[cur_humidity-1][0]+=1
                wind[cur_wind-1][0]+=1
            else:
                outlook[cur_outlook-1][1]+=1
                temp[cur_temp-1][1]+=1
                humidity[cur_humidity-1][1]+=1
                wind[cur_wind-1][1]+=1

        print(play, outlook, temp, humidity, wind)

    with open(model, 'w') as f:
        f.write(str(total)+'\n')
        f.write(str(play)+'\n')
        for i in range (r):
            for j in range(c):
                f.write(str(outlook[i][j])+' ')
            f.write('\n')

        for i in range (r):
            for j in range(c):
                f.write(str(temp[i][j])+' ')
            f.write('\n')
        for i in range (r):
            for j in range(c):
                f.write(str(humidity[i][j])+' ')
            f.write('\n')
        for i in range (r):
            for j in range(c):
                f.write(str(wind[i][j])+' ')




def CheckInput(argvs):
    """
    This function will check the input. This program trains a Naive Bayesian Model from data TrainingData.txt. There should be two parameters for training data and output model
    """
    if len(sys.argv) < 3:
        print("You should give at least two parameters for path of input training file and output model. For example:\n")
        print("python "+sys.argv[0]+" TrainingData.txt NB.model")
        return False

    return True

def main():
    if(not CheckInput(sys.argv)):
        sys.exit(0)
    train(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
