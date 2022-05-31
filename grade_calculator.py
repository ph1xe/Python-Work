num_grade = int(input())

if num_grade < 0 or num_grade > 100:
    print('Invalid Grade')
elif num_grade <= 59:
    print('F')
elif num_grade >= 60 and num_grade <= 69:
    print('D')
elif num_grade >= 70 and num_grade <= 79:
    print('C')
elif num_grade >= 80 and num_grade <= 89:
    print('B')
elif num_grade >= 90 and num_grade <= 97:
    print('A')
elif num_grade >= 98 and num_grade <= 100:
    print('A+')