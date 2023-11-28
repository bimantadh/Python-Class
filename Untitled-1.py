class StudentMark:
    def __init__(self):
        self.math_mark = 0
        self.science_mark = 0

    def set_marks(self, math_mark, science_mark):
        self.math_mark =   math_mark
        self.science_mark = science_mark
    
    def get_total_marks(self, total):
        self.total = self.math_mark + self.science_mark
        return total
    
class Student:
    @staticmethod
    def main():
        sd = StudentDetail()
        sd.set_attribute("ram" , 22)

        sm = StudentMark()
        sm.set_marks(99, 85)

        total = sm.get_total_marks()
        print (f"""
               Name : {sd.get_name()},
               Age : {sd.get_age()},
               Marks :{total}
               """)



students =[
    {"name": "ram", "age": 22, "math_mark": 99, "science_mark": 85}
    {"name": "hari", "age":23, "math_mark": 87, "science_mark": 55}
]


for student in students:
    Student.main(
        student['name'],
        student['age'],
        student['math_mark'],
        student['science_mark'],
    )