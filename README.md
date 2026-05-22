
1.Title:
Design and Analysis of Matrix Chain
Multiplication using Dynamic Programming.
     

2.Introduction:
Matrix Chain Multiplication (MCM)is a classic
problem in dynamic programming.It deals with
finding the most efficient way to multiply a
sequence of matrices.
Matrix multiplication is associative:
(A×B)×C=A×(B×C) 


3.Problem Statement:
Given a sequence of matrices,find the optimal
way to parenthesize them so that the total number
of multiplications is minimized.
lIf matrices are:
·A₁,A₂,A₃,…,An
Then dimensions are represented as:
·p=[po,P₁,P₂,…,Pn]
Where:
·Matrix Ai has dimension pi-1×p



4.Mathematical Formulation:
m[i,j]=mini≤k<i{m[i,k]+m[k+1,j]+pi-1Pkp;}
This formula calculates the minimum cost of
multiplying matrices from i to j.



5.Methodology (Dynamic
Programming Approach):
Steps:
1.Create a table to store minimum
multiplication cost
2.Initialize diagonal elements as 0 (single
matrix cost =0)
3.Compute costs for chains of length 2 to n
4.Choose minimum cost for each combination
5.Store and return final result



6.Example:
Consider matrices with dimensions:
p=[10,20,30,40,30]
Matrices:
·A1=10×20
·A2 =20×30
·A3 =30×40
·A4=40×30
Optimal Parenthesization:
((A1×A2)×(A3×A4))



7.Python Program:
Python
def matrix_chain_multiplication(p):
n =len(p)
#Create DP table
m=[[0 for _in range(n)]for _in
range(n)]
#Chain length
for L in range(2,n):
for i in range(1,n -L+1):
j=i +L-1
m[i][j]=float('inf')
p[j])
for k in range(i,j):
cost =(m[i][k]+
m[k+1][j]+
p[i-1]*p[k]*
if cost<m[i][j]:
m[i][j]=cost
return m[1][n-1]
#Example usage
p =[10,20,30,40,30]
result =matrix_chain_multiplication(p)
print("Minimum number of
multiplications:",result)



8.Output:
Minimum number of multiplications:30000



9.Complexity Analysis:
·Time Complexity:O(n³)
·Space Complexity:O(n²)



10.Applications:
·Computer graphics (transformations)
·Database query optimization
·Scientific computing
·Chain operations in Al/ML models



11.Conclusion:
Matrix Chain Multiplication shows how dynamic
programming avoids repeated calculations and
finds the most efficient solution.It is a powerful method for solving optimization problems involving multiple choices.
