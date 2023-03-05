from future.moves import tkinter
import tkinter as tk
import traceback
import random

##Creating Agent class
class BinaryAgent:
    ##Constructor for binary
    def __init__(self):
        self.binary = None

    ##When the function is called randomly select 0 or 1
    ##This function is used more than one time in the program
    def act(self):
        self.binary = random.choice([0, 1])
        return self.binary

##Class to generate the random binary number given the random choice given by BinaryAgent
class GenerateBinaryNumber:
    ##Function to create a binary number between 5 and 25 digits long
    def GenerateRandomBinary(self):
        numIterations = random.randint(5, 25)
        agent = BinaryAgent()
        binaryString = ""
        ##for the length of the random number return
        for i in range(numIterations):
            binaryString += str(agent.act())
        return binaryString

##Class to convert the binary String to its Twos Complement
class Converter:
    def __init__(self, binaryString):
        self.binaryString = binaryString

    def Twoscomplement(self):
        # We find the length and break the string into char array
        binaryLength = len(self.binaryString)
        flipdex = 0
        ##Split the String into an array for looping
        binaryCharArray = [char for char in self.binaryString]
        ##For the length of the list if the first 1 is found, declare that index as the flipping point
        ##While stepping through the list in reverse order
        for x in range(binaryLength-1,-1,-1):
            if binaryCharArray[x] == "1":
                flipdex = x
                break
        ##now for the sublist when seperated from the copied part of the string
        ##
        subChar = binaryCharArray[:flipdex + 1]
        for j in range(len(subChar)):
            if subChar[j] == "1":
                subChar[j] = "0"
            elif subChar[j] == "0":
                subChar[j] = "1"
        ##Create the half of the array for the copy then combine
        copy = binaryCharArray = binaryCharArray[flipdex + 1:]
        TwosCompChar = subChar + copy
        TwosComplement = ''.join(TwosCompChar)
        ##Return the Two's Complement
        return TwosComplement

##Create Title
root = tk.Tk()
#Size and Title
root.geometry("500x500")
root.title("2's Complement Agent")
##Test code
binaryString = GenerateBinaryNumber().GenerateRandomBinary()
print(binaryString)
twosComp = Converter(binaryString).Twoscomplement()
print(twosComp)


##Function to update the TwosComplement, as well as generating the binary String
def updateTwosComplement():
    binaryString = GenerateBinaryNumber().GenerateRandomBinary()
    twosComp = Converter(binaryString).Twoscomplement()
    binary_number_label.config(text=binaryString)
    twos_complement_label.config(text=twosComp)


##Create line for Binary String
generate_button = tk.Button(root, text="Generate Random Binary Number", command=updateTwosComplement)
generate_button.pack()
binary_number_label = tk.Label(root, text=binaryString)
binary_number_label.pack()
#Create line for 2's Complement
twos_complement_label = tk.Label(root, text=twosComp)
twos_complement_label.pack()

root.mainloop()