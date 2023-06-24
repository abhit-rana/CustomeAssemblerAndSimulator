import os
import sys
import subprocess


SIM_RUN_DIR = "Simulator"
os.chdir(SIM_RUN_DIR)


def diff(lines1, lines2):
    lines1Clean = []
    lines2Clean = []

    for l in lines1:
        if l.strip() != "":
            lines1Clean.append(l.strip())

    for l in lines2:
        if l.strip() != "":
            lines2Clean.append(l.strip())

    match = True

    # Match Size
    if(len(lines1Clean) > len(lines2Clean)):
        lines2Clean += [""] * (len(lines1Clean) - len(lines2Clean))
    elif(len(lines2Clean) > len(lines1Clean)):
        lines1Clean += [""] * (len(lines2Clean) - len(lines1Clean))

    for lineNum, lines in enumerate(zip(lines1Clean, lines2Clean), 1):
        if(lines[0] != lines[1]):
            print("Mismatch at line " + str(lineNum) +  ".")
            match &= False

    # print(match)
    return match


# subprocess.run(["javac", "ToucanAssembler.java"], shell=True)
os.system('javac ToucanSimulator.java')
# os.system('javac -d . ToucanSimulator.java')
generatedBin = os.popen("./run < " + "../TestCases/Simulator/" + sys.argv[1]).readlines()
# os.popen("./run < " + "../TestCases/Simulator/" + sys.argv[1] + " > " + "../TestCasesGeneratedOutput/Simulator/o" + f"{sys.argv[1]}")
# generatedBin = os.popen("cat " + "../TestCasesGeneratedOutput/Simulator/o" + f"{sys.argv[1]}").readlines()

word = 'Simulator'
if('System' in sys.argv):
    word = 'System'


print('\n')
if(len(sys.argv)<3):
    print("\033[93m {}\033[00m" .format("Solution File Not provided to match the output!"))
else:
    expectedBin = os.popen("cat " + "../TestCasesSolutions/Simulator/" + sys.argv[2]).readlines()
    if diff(generatedBin, expectedBin):
        print("\033[92m {}\033[00m".format(f"Output from {word} Matched with the Solution File!"))
    else:
        print("\033[91m {}\033[00m".format(f"Output from {word} Does not Match with the Solution File!"))

with open("../TestCasesGeneratedOutput/Simulator/o" + sys.argv[1], 'w') as file:
    for i in range(len(generatedBin)):
        file.write(generatedBin[i])
            

print("\n\033[96m {}\033[00m".format(f"The Output file from {word} can be found at ../Toucan/TestCasesGeneratedOutput/Simulator/o" + sys.argv[1]))

print("\n\033[96m {}\033[00m".format(f'A Scatter Plot depicting which memory address is accessed at what time while {word} executes the Instructions is available under "Simulator/" as Plot.png'))