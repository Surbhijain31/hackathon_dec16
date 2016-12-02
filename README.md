# hackathon_dec16

SECTION - A

PROBLEM - 1 (TWO PARTS) : 

(i) Write a function which accepts 2 params - a string and a word and computes the following:

A. Count occurrences of the word in the string
B. Remove that word from string
C. Append same word equal to number of occurrences in string.


(ii) Write a program that reads a json file , performs following edits and store json back to the same file. update following fields - 

A. Change firewall - protocol - from tcp to udp
B. Change 3rd vnics- portgroup name to EXT_VLAN_201b
C. Change ospf- enabled = false to true 
D. Update holddowntimer = holddowntimer +keepalivetimer

-------------------------------------------------------------------------------------------------------------------------
SECTION : B

PROBLEM - 2 : 

A BOY FELL DOWN FROM 2ND FLOOR AND SUFFERED SERIOUS BRAIN DAMAGE. NOW HE'S GONE CRAZY. HE CAN ONLY WALK 2X STEP FORWARD OR 1 STEP BACKWARD WHERE X IS HIS CURRENT POSITION. SO IF HE IS AT 5TH POSITION AND HE HAS TO REACH 8TH POSITION, HE WILL GO 1 STEP BACKWARD TO 4TH POSITION AND THEN HE WILL JUMP 2*4 STEP FORWARD TO REACH 8TH POSITION.

Example:

Input
First line will contain an integer T denoting the number of test cases ,
Next T lines will contain 2 integers st and dt denoting the starting and destination point.
Output
Output the minimum steps required to reach destination in a new line.
Constraints
1<=t<=10
1<=st,dt<=1000
SAMPLE INPUT   		SAMPLE OUTPUT
2
1 3				3
3 1				2

Explanation
For First Test case: He can jump to 2nd position and again to 4th position, now he can move to 3rd position by taking a step backward.
For Second Test case: He can directly take 1 step backward, twice to reach his destination.
-------------------------------------------------------------------------------------------------------------------------


PROBLEM - 3

SONAM GUPTA KYU BEWAFA HAI ?
OUR SPECIAL DETECTIVE MASHOOR GULATI HAS FOUND OUT THAT SONAM GUPTA IS "BEWAFA" BECAUSE SHE IS MARRYING CHITVAN BY BETRAYING HER BOYFRIEND . SEEING THIS HER BOYFRIEND JUMPED FROM THE BUILDING IN PREVIOUS QUESTION .

NOW ... CHITVAN LIVES IN SPECIAL CITY WHERE IF YOU TRAVEL IN PAIR IT IS FREE BUT IF YOU TRAVEL SINGLE YOU HAVE TO PAY ACCORDING TO DISTANCE TRAVELED (1 UNIT DISTANCE = 1 UNIT MONEY). CHITVAN HAS INVITED N PEOPLE (N IS EVEN) TO HIS WEDDING . THEY MAY OR MAY NOT BE LOCATED AT DIFFERENT PLACES. CHITVAN IS PAYING ALL OF THERE TRAVEL EXPENSES.

NOW CHITVAN IS BUSY IN PREPARATION OF WEDDING SO HE NEED YOUR HELP. HE WANT TO PAY MINIMUM TRAVEL EXPENSE, SO HE WANT TO MAKE PAIR OF EVERYONE.

HELP CHITVAN TO FIND MINIMUM EXPENSE IN MAKING PAIR. POSITION OF EVERY PERSON IS GIVEN ACCORDING IN 2-D CARTESIAN PLANE .

 
Hard
Input:
First line contain integer N denoting number of people.
Next N lines contain two integer Xi and Yi denoting position of ith person.
Output:
Output the MINIMUM amount rounded to 2 decimal places CHITVAN have to pay.
Constraints:
2<=N<=16
1<=Xi,Yi <= 1000
Example :
Input:
4
10 3
2 7
5 8
6 7
Output:
8.82
Explanation:
The pair formed is of (1st,4th) and (2nd,3rd) .
The distance traveled by 1st person to go to 4th person or vice-versa = 5.6568
The distance traveled by 2nd person to go to 3rd person or vice-versa = 3.1622
Total distance or Total money = 5.6568 + 3.1622 = 8.81907
Rounded to 8.82
SAMPLE INPUT 
4
10 3
2 7
5 8
6 7

SAMPLE OUTPUT
8.82
-------------------------------------------------------------------------------------------------------------------------

<<<<END>>>>
