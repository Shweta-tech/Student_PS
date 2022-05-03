from rest_framework import viewsets
from student_report.models import Student_detail,mark
from .serializers import MarkSerializer, StudentSerializer


class StudentAPI(viewsets.ModelViewSet):
    queryset=Student_detail.objects.all()
    serializer_class = StudentSerializer


class MarksAPI(viewsets.ModelViewSet):
    queryset=mark.objects.all()

    serializer_class = MarkSerializer   

