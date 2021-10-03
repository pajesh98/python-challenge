# Python Homework - Py Me Up, Charlie

## Background

It's time to put away the Excel sheet and join the big leagues. Welcome to the world of programming with Python. In this homework assignment, you'll be using the concepts you've learned to complete the **two** Python Challenges, PyBank and PyPoll.


## PyBank

![Revenue](Images/revenue-per-lead.png)
* Create a python script which will analyze the financial records of a company that is provided in a data set called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`.

* The Python script will analyze the financials records provided in csv dataset to calculate below listed points. 

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in profits (date and amount) over the entire period

* As an example, the analysis should look like one below:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```

* In addition, The script should both print the analysis to the terminal and export a text file with the results.

## PyPoll

![Vote Counting](Images/Vote_counting.png)

* In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

* The Python script will analyze the poll data provided in a data set called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 

The Python script analyzes the votes and calculates each of the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

* As an example,  the analysis should look like one below:

  ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```

* In addition, your final script should both print the analysis to the terminal and export a text file with the results.

