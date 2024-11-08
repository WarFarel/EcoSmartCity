# EcoSmartCity
# Date: 08/11/2024
# StudentID - 22001027
---
# This project will be about making a simulator to model and optimise different aspects of the futuristic, environmentally-friendly city. It will help the city planners and policymakers to make informed decisions about the different urban sustainability developement.
# The specifics are to make a module for the simulation that manages and optimises the city's renawable energy energy distribution system. I made this as much user-friendly as well as efficient as I could have from my abilities.
# This projects code and the program is entirely done in Python. Version Python 3.9 64bit and should run with newer versions.

----------
 Algorithm
----------
 The algorithm will have different types of the energy sources, those will be the solar power and wind as well as grid. They will have different maximum energy that they can produce. This will be in kW as this is more widely used scale.
 It will have a status which will either indicate that it is active or inactive when the source of this will be turned off,  this will help to defuse any confusion, another aspect will be the effectiveness of the energy being convered from the inputs to the outputs.
 After that the demand which will be able to be compared with the current production levels will be available. The algorith will also help to optimise the energy that will be distribiuted in order to meet the demand,efficient and availability.
 After all of this is done there will be statistics available to have things such as Total energy produced, total energy consumption and remaining energy surplus.


![DIAGRAM FOR ALGORITHM](https://github.com/user-attachments/assets/a1616771-c73c-40fe-a3e5-a52df6b14502)


# Use of IDE and debugging
# Coding#1
![image](https://github.com/user-attachments/assets/f85926f8-647d-4522-be64-93cc17f994b0)
In this image I have started the code by making the basic adding and removing of the sources of the energy.
# Spelling Mistake
![image](https://github.com/user-attachments/assets/46ddb50d-feb6-44ad-9983-6b564ed88a9c)
This shows how there was a missspeling done in the deactivation of energy source. I have sinced fixed that by looking back over my code as an error was being displayed.
# Error 1
![Error #1](https://github.com/user-attachments/assets/e5757187-c94c-4352-bd2b-022256a87e05)
This error came up after trying to launch the final version, this was a simple mistake of miss-spelling the word 'source_type"
![Error#1 Fix](https://github.com/user-attachments/assets/90d15838-dbc2-49f1-9749-8dbd2d09bea8)
# Error 2
Second error that I have encountered was another simple spelling mistake which I have fixed.
![Error#2](https://github.com/user-attachments/assets/16193c86-161c-4964-b79f-7e596a6b12f1)
![Error#2 Fix](https://github.com/user-attachments/assets/e4bd802b-8042-47de-83a8-592ba2ee57db)

# Error 3

![Error#3](https://github.com/user-attachments/assets/c78cdabe-9b3f-4338-9db8-2e46c6fa2f26)
![Error#3 Fix](https://github.com/user-attachments/assets/133affa8-01a9-4725-9e77-3ec5012b634e)

After testing the UI I concluded that I have coded one too many labels to do with the demand, as a result I had to enter demand twice, I fixed it by deleting one.


# Testing
I have tested the input box with various input to see whether the program will handle these exceptions correctly and as a result it did handle them correctly.

![Test 2](https://github.com/user-attachments/assets/93a9224e-00c8-4c2e-9cbd-21b0276c85ac)

![TEST 1](https://github.com/user-attachments/assets/43dd6eb4-4d18-4705-8833-c0247ba2bf35)
![TEST 3](https://github.com/user-attachments/assets/ba08b3d0-bf3a-48af-a9fc-9fe69c2c81da)


# Code Structure
The code I have written has three claseses, energy_source which manages the individual energy sources, distribution_grid which handles multiple of the sources and the production and the energy_distribution_program which
has the tkinter GUI which the user can interact with, the structure is object-oriented with parts of procedural programing as well as even driven due to the butttons which make this code easy to manage overall.
I used a random in order to simulate the randomness of the cloud coverage as well as the wind in order to make this simulation more realistic.


# Learning Outcomes.
Having the procedural programming paradigms that I have included means that the focus on the functions and the procedures is much more significant as well as it helps to execute the tasks in a sequence,
it helps to make the approach top-down which means that the code is in a structure around a set of instructions, this is usually managed by global procedures, whereas the object oriented programming 
that I have used has classes which have encapsulation for both the data as well as bahaviours. It focuses on encapuslation, inheritance and polymorphism which is effective at making the code more reusabble 
especially helpful in large codes. The event driven paradigms I have included focus on events as the name suggests this is things such as the buttons I included when pressed they make a decision
or make something appear on the screen, this helps as I made the program much more interactive however this can be difficult as it might be problematic to debug the issues if some arrise.


The coding standards I followed while developing this was the PEP-8 standard in order to maintain the essential clarity as well as to stay consistent and not make the code confusing, in my program
 I used consistent naming convention as well as indentations in order for the code to be easy to read, however it can still be imrpoved by making more detailed comments that would explain the program as whole
 and implement better error handling as this could improve the user expierience.  I chose these standards as they are the most widely known and the naming conventions were most convenient for me.


Overall I feel like this project was sucessful as it servers its purpose and is working correctly, this being said i believe further developement could be an option as this is only a basic version with no advanced features.




# FILE LIST
Alorightm StepbyStep.odt
DIAGRAM FOR ALGORITHM.png
Error #1.png
Error#1 Fix.png
Error#2 Fix.png
Error#2.png
Error#3 Fix.png
Error#3.png
TEST 1- bad input.png
TEST 3- Characters Input.png
Test 2.- Normal Input.png
