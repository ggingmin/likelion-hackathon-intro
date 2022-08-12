from django.views.generic import ListView, TemplateView
from django.shortcuts import render

from .models import Student


class IndexView(TemplateView):
    template_name = "students/student_index.html"

class StudentListView(ListView):
    model = Student
    template_name = "student_list.html"