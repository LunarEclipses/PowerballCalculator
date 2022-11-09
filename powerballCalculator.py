#powerball calculator
#imports
import random
#global variables

#classes

#methods

#main
def main():
    print('running')
    timeslost = 0
    guess = []
    winningNum = [69, 55, 23, 47, 9, 19]
    winningNum.sort()
    while winningNum != guess:
        guess=[]
        for i  in range(5):
            potentialNums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69]
            if i < 5:
                addNum = random.randint(1, 69)
                guess.insert(i, addNum)
                try:
                    potentialNums.remove(addNum)
                except:
                    continue
                else:
                    pballnum = random.randint(1, 30)
                    guess.insert(5, pballnum)
        guess.sort()
        timeslost += 1
    print("you lost the powerball", timeslost, "times. your winning numbers are", winningNum)
    quit()
    return 0
if __name__ == '__main__':
    main()