sorted("This is a test string from Andrew".split(), key=str.lower)

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
sorted(student_tuples, key=lambda student: student[2])


student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
sorted(student_objects, key=lambda student: student.age)


from operator import itemgetter, attrgetter

sorted(student_tuples, key=itemgetter(2))

sorted(student_objects, key=attrgetter('age'))
#[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

sorted(student_objects, key=attrgetter('grade', 'age'))
#[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]

sorted(student_tuples, key=itemgetter(2), reverse=True)
#[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
