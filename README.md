# Graph-Algorithim

5. (12 points) Suppose there are two sides of a football "civil war": “Beavers” (“good guys”) and
“Ducks” (“bad guys”). Between any pair of teams, there may or may not be a rivalry. Suppose we 
have n players and we have a list of r pairs of rivalries.

(a) Give pseudocode for an efficient algorithm that determines whether it is possible to designate 
some of the team members as Beavers and the remainder as Ducks such that each rivalry is between a 
Beaver and a Duck. If it is possible to perform such a designation, your algorithm should produce it.

(b) What is the running time of your algorithm?

(c) Implement: Beavers vs. Ducks.
Input: Input is read in from a file specified in the command line at run time. The file contains the 
number of players, n, followed by their names, the number of rivalries r and rivalries listed in pairs. 

Note: The file only contains one list of rivalries 

Output: Results are outputted to the terminal. 

• Yes, if possible followed by a list of the Beaver players and a list of the Ducks.

• No, if impossible.

Sample Input file: 

5 

Ace 

Duke 

Jax 

Biggs 

Stone 

6 

Ace Duke 

Ace Biggs 

Jax Duke 

Stone Biggs 

Stone Duke 

Biggs Jax 

Sample Output: 

Yes 

Beavers: Ace Jax Stone 

Ducks: Biggs Duke
