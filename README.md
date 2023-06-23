## Introduction

Implemented a system that takes input as Instructions in the form of Assembly Language and then outputs the values of the components(Registers and Flags) used in the execution of Instructions inside the Processor based on the Custom Instruction Set Architecture(ISA). The system consists of [Assembler](https://www.techtarget.com/searchdatacenter/definition/assembler#:~:text=An%20assembler%20is%20a%20program,use%20the%20term%20assembly%20language.)(a computer program that takes basic computer instructions as input and converts them into a pattern of bits as output) and [Simulator](https://www.dictionary.com/browse/simulator)(a computer program that simulates specific conditions or the characteristics of a real process or machine. Here, the Simulator would imitate the working of the Computer System by taking input as instructions as bits and outputting the state of Registers and Flags). A Scatter Plot is also plotted along with Simulator output depicting which memory address is accessed at what time while Simulator executes the Instructions.

## Flow Diagram

![dfdf - Page 14](https://github.com/abhit-rana/Toucan/assets/88608893/c7fb9a5d-8705-4d10-a760-e82a272264e4)

## Demo

* Assembler


* Simulator and Scatter Plot




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

INPUT - INSTRUCTIONS IN THE FORM OF ASSEMBLY LANGUAGE

OUTPUT - INSTRUCTIONS IN THE FORM OF BITS

**FORMAT:**

python3 runAssembler.py assembler_test_file_name assembler_solution_file_name


**Example:**
```
python3 runSimulator.py at4 sat4
```

**Note:**

* If you don't have the solution file, leave the assembler_solution_file_name argument empty.
* **Add the new test cases and their solution to the assigned folders, TestCases, and TestCasesSolutions, inside the Assembler Directory**.

The Output file of the test case would be inside "Assembler/TestCasesGeneratedOutput/" with the same name as the test file. If the Solution file were provided, the result of whether the output file matched the solution file would be provided in the output.

## Running the Simulator

INPUT - INSTRUCTIONS IN THE FORM OF BITS

OUTPUT - VALUE OF PROGRAM COUNTER, REGISTERS, AND FLAGS AFTER EXECUTING EACH INSTRUCTION


**FORMAT:**

python3 runSimulator.py simulator_test_file_name simulator_solution_file_name


**Example:**
```
python3 runSimulator.py st5 sst5
```

**Note:**

* If you don't have the solution file, leave the simulator_solution_file_name argument empty.
* **Add the new test cases and their solution to the assigned folders, TestCases, and TestCasesSolutions, inside the Simulator Directory**.

The Output file of the test case would be inside "Simulator/TestCasesGeneratedOutput/" with the same name as the test file. If the Solution file were provided, the result of whether the output file matched the solution file would be provided in the output.

## Running the Entire System

INPUT - INSTRUCTIONS IN THE FORM OF ASSEMBLY LANGUAGE

OUTPUT - VALUE OF PROGRAM COUNTER, REGISTERS, AND FLAGS AFTER EXECUTING EACH INSTRUCTION

**FORMAT:**

python3 runToucan.py toucan_test_file_name=assembler_test_file_name assembler_solution_file_name toucan_solution_file_name=simulator_solution_file_name


**Example:**
```
python3 runToucan.py at5 sat5 sst5
```
