from rest_framework import serializers
from student_report.models import Student_detail,mark

class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = mark
        fields = ['subject_name', 'marks','student']
        
class StudentSerializer(serializers.ModelSerializer):
    marks = MarkSerializer(read_only=True,many=True)
    class Meta:
        model = Student_detail
        fields = ['roll_no','std_gender','marks']
