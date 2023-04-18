#!/usr/bin/python3

def main():
    num = input()

    for i in range(len(num)):
        firstChoice = int(num[i])
        secondChoice = 9 - int(num[i])

        # print(firstChoice, secondChoice)

        if firstChoice == 0:
            num[i] = str(secondChoice)
        elif secondChoice == 0:
            num[i] = str(firstChoice)
        else:
            num[i] = str(min(firstChoice, secondChoice))
        print(num)





if __name__ == '__main__':
    main()
