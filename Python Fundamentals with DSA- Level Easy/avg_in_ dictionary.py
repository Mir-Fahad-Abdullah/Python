"""
# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of 
# students. Print the average of the marks array for the student name provided, showing 2 places after the 
# decimal.[cite: 2]
# 
# Example[cite: 2]
# marks key:value pairs are[cite: 2]
# 'alpha': [20, 30, 40][cite: 2]
# 'beta': [30, 50, 70][cite: 2]
# query_name = 'beta'[cite: 2]
# 
# The query_name is 'beta'. beta's average score is (30 + 50 + 70)/3 = 50.0.[cite: 2]
# 
# Input Format[cite: 2]
# The first line contains the integer n, the number of students' records. The next n lines contain the names 
# and marks obtained by a student, each value separated by a space. The final line contains query_name, 
# the name of a student to query.[cite: 2]
# 
# Constraints[cite: 2]
# 2 <= n <= 10[cite: 2]
# 0 <= marks[i] <= 100[cite: 2]
# length of marks arrays = 3[cite: 2]

"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    marks = student_marks[query_name]
    
    sum = 0
    for item in marks:
        sum+=item
    
    average = sum/len(marks)
    print(f"{average:.2f}")