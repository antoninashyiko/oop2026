from  abc import ABC, abstractmethod
# visitor pattern
class Visitor(ABC):
    @abstractmethod
    def visit(self, student):
        pass
class Credits(Visitor):
    def __init__(self, credit):
        self.credit = credit
    def visit(self, student):
        student.credits+=self.credit
class ScholarShip(Visitor):
    def __init__(self, scholarship):
        self.scholarship = scholarship
    def visit(self, student):
        student.money+=self.scholarship
class ParentMoney(Visitor):
    def __init__(self, amount):
        self.amount = amount
    def visit(self, student):
        student.money+=self.amount
class Pay(Visitor):
    def __init__(self, pay_needed):
        self.pay_needed = pay_needed
    def visit(self, student):
        if student.money >= self.pay_needed:
            student.money -= self.pay_needed
        else:
            student.expelled = True
class TeacherVisitor(Visitor):
    def __init__(self, discipline, credit):
        self.discipline = discipline
        self.credit = credit
    def visit(self, student):
        if student.discipline==self.discipline or student.discipline == "natural-humanitarian":
            student.credits+=self.credit
# student classes
class Student:
    def __init__(self, discipline, money):
        self.discipline = discipline
        self.money = money
        self.credits = 0
        self.expelled = False

    def accept(self, visitor):
        if not self.expelled:
            visitor.visit(self)
    def __str__(self):
        status = "expelled" if self.expelled else "in school"
        return f"{self.discipline}, money: {self.money}, credits: {self.credits}, status: {status}"
class Humanitarian_student(Student):
    def __init__(self, money):
        super().__init__("humanitarian", money)
class Natural_student(Student):
    def __init__(self, money):
        super().__init__("natural", money)
class Natural_Humanitarian_student(Student):
    def __init__(self, money):
        super().__init__("natural-humanitarian", money)

##main
def student_file(filename):
    with open(filename) as f:
        lines=f.readlines()
        discipline = lines[0].strip()
        credits = int(lines[1])
        money = int(lines[2])
        if discipline == "humanitarian":
            student = Humanitarian_student(money)
        elif discipline == "natural":
            student = Natural_student(money)
        else:
            student = Natural_Humanitarian_student(money)
        for l in lines[3::]:
            if student.expelled or student.credits >= credits:
                break
            d=l.strip().split()
            command=d[0]
            if command=="teach":
                teacher=TeacherVisitor(d[1], int(d[2]))
                student.accept(teacher)
            elif command=="pay":
                pay=Pay(int(d[2]))
                student.accept(pay)
            elif command=="obtain":
                if d[1]=="scholarship":
                    scholarship=ScholarShip(int(d[2]))
                    student.accept(scholarship)
                elif d[1]=="help":
                    help=ParentMoney(int(d[2]))
                    student.accept(help)
        if student.expelled:
            diploma="no diploma"
        elif student.credits >=credits:
            diploma="graduated"
        else:
            diploma="no diploma"
    return student, diploma

files=["input01.txt","input02.txt","input03.txt", "input04.txt", "input05.txt",
       "input06.txt", "input07.txt", "input08.txt", "input09.txt", "input10.txt",
       "input11.txt", "input12.txt", "input13.txt", "input14.txt"]
for filename in files:
    student, diploma = student_file(filename)
    print(filename)
    print(student, ",",  diploma)
