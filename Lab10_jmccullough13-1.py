#Word Count
#Jeffrey McCullough
#
#March 6, 2023

def main():
    
    again = "Y"
    #filename = 'c:/Users/jcmc9/Documents/CSCC classwork/4. Spring 23/Python/test.txt'
    while again == "Y" or "y":
        fileRead = input("Enter the filename that you want to be counted: ")
        filename = (f'{fileRead}')
        try:
            with open(filename, 'r') as contents:
                wordList = wordFreq(contents)
                printWords(wordList)
                again = input("Do you want to try another file? Y|N: ")
                if again == "n" or "N":
                    break
            
        except FileNotFoundError:
            print(f"{filename} doesn't exist.")

def wordFreq(fptr):
    freq = dict()
    punctChars = (".", "'", '"', ",", "!", "?", ":", ";", "(", ")", "/")
    for line in fptr:
        for c in punctChars:
            line = line.replace(c, "")
        words = line.split()
        for word in words:
            tmp = word.lower()
            if tmp in freq:
                freq[tmp] += 1
            else:
                freq[tmp] = 1
    return freq

def printWords(data):
    for x, y in sorted(data.items()):
        print(f"{x}   ::\t{y}")
    return

main()