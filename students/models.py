from django.db import models


class Student(models.Model):
    STUDENT_TYPE = (
        ("UNDERGRADUATE", "Undergraduate"),
        ("GRADUATE", "Graduate"),
        ("EXCHANGE", "Exchange")
    )

    student_num = models.DecimalField(max_digits=10, decimal_places=0)
    name = models.CharField(max_length=50)
    college = models.CharField(max_length=30)
    major = models.CharField(max_length=30)
    student_type = models.CharField(max_length=20, choices=STUDENT_TYPE)
    entrance_date = models.DateField()

    class Meta:
        db_table = "TB_STUDENTS"

    def __str__(self):
        return f"${self.student_num}, ${self.name}"

