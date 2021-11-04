# Backtrack-Backjumping
## Context
The problem to solve is about an event that takes place at the Universidad Catolica Boliviana in which national and international conferences will be held to give lectures on areas related to Informatics.

For this event three areas will be discussed which are: Information Security (IS), Software Engineering (SI) and Artificial Intelligence (AI).

The schedule for the talks is Monday through Friday from 9 a.m. to 12 p.m. and from 15 p.m. to 18 p.m. 
## Propose the problem as a CSP

## Implementation
For this particular problem we first established what our variables were going to be:

- **Nodes** were defined as the rooms available at each available time, in this case we have three rooms available at each time slot.
- **Constrains** are the connection of a room to its adjacent rooms. 
- **Domain** is a list of the talks to be given in a specific room and for this we have some limitations.
  - A speaker can have 5 talks in the same area but they can not give 2 talks in a row.
  - Two speakers of the same area will not have assigned one same hour for their talks.
  - Two international guests should not have a talk at the same hour.
  
 
 ## Experiments

 ### Forward checking 

 ### Minimum remaining values algorithm

 ### Least Constrained value

 ### Running the program
