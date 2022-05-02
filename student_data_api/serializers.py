from django.contrib.auth.models import User, Group
from rest_framework import serializers
from student_report.models import Student_detail,subject,mark

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_detail
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'