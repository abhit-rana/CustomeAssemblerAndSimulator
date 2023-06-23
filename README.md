## Introduction

Implemented a custom [Assembler](https://www.techtarget.com/searchdatacenter/definition/assembler#:~:text=An%20assembler%20is%20a%20program,use%20the%20term%20assembly%20language.)(a computer program that takes basic computer instructions and converts them into a pattern of bits) and [Simulator](https://www.dictionary.com/browse/simulator)(any device or system that simulates specific conditions or the characteristics of a real process or machine. Here, the Simulator would imitate the working of the Computer System by showing the execution of Instructions or bits given to the computer.) for the Instruction Set Architecture(ISA). A Scatter Plot is also plotted with the cycle number on the x-axis and the memory address on the y-axis, depicting which memory address is accessed at what time while Simulator executes the Instructions.

## Demo

* Assembler


* Simulator


* Scatter Plot


## Contents of the Repo

* [Assembler](https://github.com/abhit-rana/Toucan/tree/main/Assembler): Contains the code for the Assembler: ToucanAssembler.java
* [Simulator](https://github.com/abhit-rana/Toucan/tree/main/Assembler): Contains the code for the Simulator: ToucanSimulator.java and for plotting the scatter plot: makeGraph.py
* [ISA-DESCRIPTION](https://github.com/abhit-rana/Toucan/blob/main/ISA-DESCRIPTION.pdf): Information regarding the Instruction Set Architecture(ISA) used in the Assembler and Simulator
* [Project_Components_Description](https://github.com/abhit-rana/Toucan/blob/main/Porject_Components_Description.pdf): Information regarding the working of the Assembler, Simulator, and Scatter Plot.

## Installing the System

1. Downloading the Repo

* Go to the Homepage of this Repo. Download the ZIP FILE from the "<> Code" button there.
* Extract the ZIP file where you want
* Rename the Downloaded folder(Toucan-main) to be - Toucan

2. Setting up a virtual environment
```
pip3 install virtualenv
virtualenv DaargiBot
```

**3. Opening up the Repo**
```
cd DaargiBot
```

**4. Activating Virtual Environment**
```
source bin/activate
```

**5. Downloading the Required Python Packages**
```
pip3 install -r requirements.txt
```

Hurray, we are all set up!!

## Running the Assembler
```
python3 runAssembler.py test_file_name solution_file_name
```

**Note:**

* If you don't have the solution file, leave the solution_file_name argument empty.
* **Add the new test cases and their solution to the assigned folders, TestCases, and TestCasesSolutions, inside the Assembler Directory**.

The Output file of the test case would be inside Assembler/TestCasesGeneratedOutput with the same name as the test file. If the Solution file were provided, the result of whether the output file matched the solution file would be provided in the output.

## Running the Simulator

**Since the Simulator would imitate the working of the Computer. So, to show whether the Instructions given to the computer are being executed or not, the output of the Simulator would be the Program Counter, Values of 8 Registers, and Flags after executing each instruction.**
