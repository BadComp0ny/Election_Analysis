# Election_Analysis

## Project Overview
A Board of Elections employee has tasked me with auditing the recent election results for a local election.  

The task included identifying the following
1. The total number of votes casts.
2. The total votes casts by county and the percentage of votes from each county.
3. Identify which county had the most voters
5. A list of all candidates that received votes.
6. The total number of votes each candidate received
7. the percentage of votes each candidate received
8. The winner of the election based on the popular vote.

## Research
In conducting our research through both a count of total votes in the script and an initial review of the CSV document we were able to confirm that there were 369,711 votes casts between the three counties for this precinct.

![Image 1](/Terminal_output.png)

we were able to utilize some scripting in order to quickly parse through the data and return the results below.

1. Total votes and percentage of total votes per county.
  1. Denver - 306,055 - 82.8%
  2. Jefferson - 38,855 - 10.5%
  3. Arapahoe - 24,801 - 6.7%

2. Total votes and percentage of total votes per candidate.
  1. Diana Degette - 272,892 - 73.8%
  2. Charles Casper Stockham - 85,213 - 23.0%
  3. Raymon Anthony Doane - 11,606, 3.1%



## Summary
 In summary I feel that the scripting developed has performed extremely well and can quickly be utilized to identify similar results for any election going forward.  If we had the number of registered voters per county we could add those into the code as a dictionary then use that along with actual votes to get a true count of voter participation results per county.
 
 
