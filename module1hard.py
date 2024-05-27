grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
res = list(students)
res.sort()
print(res)
a = grades[0]
b = grades[1]
j = grades[2]
k = grades[3]
s = grades[4]
average_a = sum(a) / len(a)
average_b = sum(b) / len(b)
average_j = sum(j) / len(j)
average_k = sum(k) / len(k)
average_s = sum(s) / len(s)
grades = [average_a, average_b, average_j, average_k, average_s]
students_and_grades = dict(zip(students, grades))
print(students_and_grades)
