from django.contrib.auth.models import User, Group
from rest_framework import serializers
from student_report.models import Student_detail,subject,mark

class UserSerializer(serializers.ModelSerializer):
 class Meta:
  model = Student_detail
  fields = ('roll_no',)
 
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = subject
        fields = ('subject_code', 'subject_name')
class MarkSerializer(serializers.ModelSerializer):
    student = serializers.CharField(source='Student_detail.roll_no')
    subject = serializers.CharField(source='subject.subject_code')
    class Meta:
        model = mark
        fields = ('marks','student','subject')
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student_detail
#         fields = ('roll_no', 'std_gender')




# class MarkSerializer(serializers.ModelSerializer):
#     stu_detail = UserSerializer(many=True)
#     sub = SubjectSerializer(many=True)
#     class Meta:
#         model = mark
#         fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'