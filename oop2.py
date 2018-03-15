class SchoolMember:
    '''Represents any scool member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        '''Tell my details.'''
        print('Name: "{}" Age: "{}"'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))

class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))

#t = Teacher('Mrs. Shrividya', 40, 30000)
#s = Student('Swaroop', 25, 75)

#print()

#members = [t, s]

#for member in members:
#    member.tell()

def print_attributes(obj):
    for attr in obj.__dict__:
        print(attr, getattr(obj, attr))

#s = Student('Mark', 29, 5)
#print(s)
#print(hasattr(s, 'age'))
#print(hasattr(s, 'ages'))
#print(s.__dict__)
#print_attributes(s)


class Kangaroo(object):
    """a Kangaroo is a marsupial"""
    
    def __init__(self, contents=[]):
        """initialize the pouch contents; the default value is
        an empty list"""
        self.pouch_contents = contents

    def __init__(self, contents=None):
        """initialize the pouch contents; the default value is
        an empty list"""
        if contents == None:
            contents = []
        self.pouch_contents = contents

    def __str__(self):
        """return a string representaion of this Kangaroo and
        the contents of the pouch, with one item per line"""
        t = [ object.__str__(self) + ' with pouch contents:' ]
#        print('DEBUG: [' + str(self.pouch_contents) + ']')
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        """add a new item to the pouch contents"""
        self.pouch_contents.append(item)

kanga = Kangaroo()
roo = Kangaroo()

kanga.put_in_pouch(roo)

#print(kanga)
#print()
#print(roo)
#
#for i in range(0, 256, 51):
#    print(i)
#
