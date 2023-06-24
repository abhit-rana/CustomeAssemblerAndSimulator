import os
import sys
import subprocess


print("\n")
print(" Assembler->")
if(len(sys.argv)<3):
    # os.popen("python3 runAssembler.py " + sys.argv[1])
    subprocess.call(["python3","runAssembler.py", sys.argv[1]])
else:
    # os.popen("python3 runAssembler.py " + sys.argv[1] + " " + sys.argv[2])
    subprocess.call(["python3","runAssembler.py", sys.argv[1], sys.argv[2]])

os.chdir("../Toucan")

testCaseDigit = sys.argv[1].split("at")[1]



# os.popen("cp TestCasesGeneratedOutput/Assembler/oat" + testCaseDigit + " TestCases/Simulator/st"+sys.argv[1].split("at")[1])
subprocess.call(["cp", "TestCasesGeneratedOutput/Assembler/oat" + testCaseDigit, "TestCases/Simulator/st"+sys.argv[1].split("at")[1]])

print("\n")
print(" System: Toucan->")
if(len(sys.argv)<4):
    # os.popen("python3 runSimulator.py " + "st" +  testCaseDigit)
    subprocess.call(["python3", "runSimulator.py", "st" +  testCaseDigit,"System"])
    # print("\033[93m {}\033[00m" .format("Solution File Not provided to match the output!"))
else:
    subprocess.call(["python3", "runSimulator.py", "st" +  testCaseDigit, sys.argv[3], "System"])


# print("\n\033[96m {}\033[00m".format("The Output file from System can be found at ../Toucan/TestCasesGeneratedOutput/Simulator/ost" + testCaseDigit))
