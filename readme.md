# Backtrack-Backjumping
## Context
The problem to solve is about an event that takes place at the Universidad Catolica Boliviana in which national and international conferences will be held to give lectures on areas related to Informatics.

For this event three areas will be discussed which are: Information Security (IS), Software Engineering (SI) and Artificial Intelligence (AI).

The schedule for the talks is Monday through Friday from 9 a.m. to 12 p.m. and from 15 p.m. to 18 p.m. 
## Propose the problem as a CSP

For this particular problem we first established what our variables were going to be:

- **Nodes** were defined as the rooms available at each available time, in this case we have three rooms available at each time slot.
- **Constrains** are the connection of a room to its adjacent rooms. 
- **Domain** is a list of the talks to be given in a specific room and for this we have some limitations.
  - A speaker can have 5 talks in the same area but they can not give 2 talks in a row.
  - Two speakers of the same area will not have assigned one same hour for their talks.
  - Two international guests should not have a talk at the same hour.
  
## Implementation
For the implementation of the problem we first defined how each node was going to be identified by taking the following aspects and formulating a code which was assigned to each node:

- first we took the initial of each day of the week.
 
- Each hour in which the talks will be given was assigned a number, for example if the talk is from 9 am to 10 am the number 1 was assigned and so on.

- And finally a letter is assigned to each available room which in this case are three which go from letter A to C.

And as a result we would have the identifiers: L_1_A, L_1_B, L_1_C, etc. 

Subsequently, identifiers were defined for each speaker:

We added the initial of the day of the week, the identifier of the time it was available and some information about the speaker, such as whether he/she was a national or international speaker, his/her name and in which area he/she was going to give the talk.

and we were left with an identifier with the following format: L_1_I_Mario_SI

In order to understand the graph used for this practice, it is presented as a 3D graph which is formed by a series of floors and in each floor there are three nodes which are interlinked with all the nodes of the same floor and with the nodes of the floors above and below.
 
as shown in the diagram 

![2021-11-03_23h26_29](https://user-images.githubusercontent.com/73244043/140253011-e573aa34-4103-44ef-9376-8b83e4142243.png)
![2021-11-03_23h22_22](https://user-images.githubusercontent.com/73244043/140253052-cce19e97-1848-4f97-8650-dbb5150c767c.png)

 ## Experiments
 
 In the experience part there is a json file with some data of some speakers.
 
 ![2021-11-03_23h29_30](https://user-images.githubusercontent.com/73244043/140253275-d61800ed-12cc-4374-b29b-f5ea7b310c55.png)

When running the program, the json file is automatically loaded and the Arc-Consistency algorithm is executed and the backtracking algorithm could not be successfully implemented. 

While saving the data in the domain variable, a filtering of some restrictions mentioned above is made, for example that there are not two speakers from the same area in the same schedule or that there are not two international speakers in the same schedule.

After that the variables are sent to the Arc-Consistency in which first a dictionary is created in which is the schedule and the specific room with all its neighboring rooms, then it is entered in a while cycle where in each iteration is sent to a Domain_Touched function for each room only has one speaker and removes the other speakers that had the possibility of using that room and once you have a room with only one speaker values are copied to a dictionary.

The following is what the result would look like after running the program

![2021-11-03_23h41_16](https://user-images.githubusercontent.com/73244043/140254325-fbef1b6b-0d31-408d-837a-127cf6fb5c42.png)

Graphical view of the solution.

![2021-11-03_23h43_19](https://user-images.githubusercontent.com/73244043/140254474-7a219818-5631-4143-b7a7-0293661547ab.png)


 ### Forward checking 

 ### Minimum remaining values algorithm

 ### Least Constrained value

 ### Running the program
