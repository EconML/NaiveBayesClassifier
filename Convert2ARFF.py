"""
 Name: Max Staples
 Assignment: Lab 3
 Course: CS 330
 Semester: Fall 2018
 Instructor: Dr. Cao
 Date: 10/15/2018
 Sources consulted: Kasey Johnson, Connor Whyte

 Known Bugs: It seems be wrong format because I had trouble loading it into Weka

 Creativity: anything extra that you added to the lab

 Instructions: special instructions to user on how to execute your program

"""
import sys

def ARFFConvert(data, output):
    """
    This is the main function you need to implement.
    Load the data from course website and convert it to ARFF format,
    so that Weka could accept them and load them.
    Check Weka Manual and examples of ARFF format.
    """
    with open(data, 'r') as f:
        with open(output, 'w') as fout:
            cur_line = f.readline()
            fout.write('@relation Play_tennis\n\n')
            fout.write('@attribute ' + 'play' + ' {0,1}\n')
            fout.write('@attribute ' + 'outlook' + ' {1,2,3,4,5,6,7,8,9,10}\n')
            fout.write('@attribute ' + 'temperature' + ' {1,2,3,4,5,6,7,8,9,10}\n')
            fout.write('@attribute ' + 'humidity' + ' {1,2,3,4,5,6,7,8,9,10}\n')
            fout.write('@attribute ' + 'wind' + ' {1,2,3,4,5,6,7,8,9,10}\n')
            fout.write('\n@data\n')
            for line in f:
                data_line = [int(i) for i in line.split()]
                print(str(data_line))
                fout.write(str(data_line.pop(0)) + ',')
                fout.write(str(data_line.pop(0)) + ',')
                fout.write(str(data_line.pop(0)) + ',')
                fout.write(str(data_line.pop(0)) + ',')
                fout.write(str(data_line.pop(0)) + '\n')

def CheckInput(argvs):
    """
    This function will check the input. It's going to
    """
    if len(sys.argv) < 3:
        print("You should give at least two parameters for path of input data and output ARFF format. Read Weka Manual for ARFF format. For example:\n")
        print("python "+sys.argv[0]+" TestDataNoLabel.txt TestDataNoLabel.arff")
        print("python "+sys.argv[0]+" TrainingData.txt TrainingData.arff")
        return False
    return True

def main():
    # hint, the following codes are for your testing.
    if(not CheckInput(sys.argv)):
        sys.exit(0)
    ARFFConvert(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
