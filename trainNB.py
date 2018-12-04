"""
 Name: Max Staples
 Assignment: Lab 3
 Course: CS 330
 Semester: Fall 2018
 Instructor: Dr. Cao
 Date: 10/15/2018
 Sources consulted: Kasey Johnson, Connor Whyte

 Known Bugs: None

 Creativity: anything extra that you added to the lab

 Instructions: special instructions to user on how to execute your program

"""
import sys

def train(data, model):
    """
    This is the main function you need to implement.
    It is going to read TrainingData.txt, and calculate all probablities,
    save them as a model file.
    You should design what kind of data format to save the model,
    and make sure you could read them back when you do the prediction.
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
    This function will check the input. This program is supposed to train a Naive Bayesian Model from data downloaded in course website: TrainingData.txt. There should be two parameters for training data and output model
    """
    if len(sys.argv) < 3:
        print("You should give at least two parameters for path of input training file and output model. For example:\n")
        print("python "+sys.argv[0]+" TrainingData.txt NB.model")
        return False

    return True

def main():
    # hint, the following codes are for your testing.
    if(not CheckInput(sys.argv)):
        sys.exit(0)
    train(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
