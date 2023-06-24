import os
import sys
import subprocess


ASM_RUN_DIR = "Assembler"
os.chdir(ASM_RUN_DIR)


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
os.system('javac ToucanAssembler.java')
generatedBin = os.popen("./run < " + "../TestCases/Assembler/" + sys.argv[1]).readlines()

print('\n')
if(len(sys.argv)<3):
    print("\033[93m {}\033[00m" .format("Solution File Not provided to match the output!"))
else:
    expectedBin = os.popen("cat " + "../TestCasesSolutions/Assembler/" + sys.argv[2]).readlines()
    if diff(generatedBin, expectedBin):
        print("\033[92m {}\033[00m".format("Output from Assembler Matched with the Solution File!"))
    else:
        print("\033[91m {}\033[00m".format("Output from Assembler Does not Match with the Solution File!"))

with open('../TestCasesGeneratedOutput/Assembler/o' + sys.argv[1], 'w') as file:
    for i in range(len(generatedBin)):
        if(i==len(generatedBin)-1):
            file.write(generatedBin[i].split('\n')[0])
        else:
            file.write(generatedBin[i])

print("\n\033[96m {}\033[00m".format("The Output file from Assembler can be found at ../Toucan/TestCasesGeneratedOutput/Assembler/o" + sys.argv[1]))

