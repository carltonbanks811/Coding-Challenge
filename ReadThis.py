"""
This project uses the MVC software architecture pattern.
Model is Game.py
View is technically the Command Line
Controller is Controller.py
This uses Python 2.7.11
"""
"""
If a tie-breaker occurs it first compares the total scores of each player in question,
then if both players have the same score it
goes back to the game played against the two players
who are tied and decides the winner based on who won their original game and the winner of
that game wins the tournament.
There is a spin mechanic to subtract the spin percentage from the return skill percentage
The winning player must win by two points and cannot win on his own serve.
If it is his serve and he will win the final point the serve automatically switches to his opponent
"""
