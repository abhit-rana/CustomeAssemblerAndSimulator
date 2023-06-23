## Introduction

Implemented a custom [Assembler](https://www.techtarget.com/searchdatacenter/definition/assembler#:~:text=An%20assembler%20is%20a%20program,use%20the%20term%20assembly%20language.)(a computer program that takes basic computer instructions and converts them into a pattern of bits) and [Simulator](https://www.google.com/search?q=what+is+an+Simulator&rlz=1C1GCEU_enIN969IN969&ei=4zeVZPDSAs2KhwP_2ouACw&ved=0ahUKEwiw0JCg3tj_AhVNxWEKHX_tArAQ4dUDCA8&uact=5&oq=what+is+an+Simulator&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjoKCAAQRxDWBBCwAzoKCAAQigUQsAMQQzoFCAAQgAQ6CAgAEIoFEJECSgQIQRgAUK8CWM0MYMoNaAFwAXgAgAGPAogB0AySAQUwLjEuNpgBAKABAcABAcgBCg&sclient=gws-wiz-serp)(a program enabling a computer to execute programs written for a different operating system) for the Instruction Set Architecture(ISA). A Scatter Plot is also plotted with the cycle number on the x-axis and the memory address on the y-axis depicting which memory address is accessed at what time.

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
