from rest_framework import serializers

from students.models import Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = (
            "id",
            "student_num",
            "name",
            "college",
            "major",
            "student_type",
            "entrance_date"
        )