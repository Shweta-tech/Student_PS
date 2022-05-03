from django.shortcuts import render
import requests
from .models import Student_detail,mark
from django.db.models import Max
from django.db.models import Q


from student_data_api.urls import *
import json 
from django.core.serializers.json import DjangoJSONEncoder 
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        roll_no = request.user.roll_no
        url = 'http://127.0.0.1:8000/api/student/'+roll_no+'?format=json'
        data = requests.get(url)
        json_data = data.json()
        max_marks= mark.objects.values('subject_name').annotate(max_marks=Max('marks'))
        stu_id_subject = []
        stu_id = []
        for mm in max_marks.iterator():
            sn = mm['subject_name']
            maxm = mm['max_marks']
            objj = mark.objects.filter(Q(subject_name=sn) &  Q(marks=maxm)).values()
            stu_id_subject.append([objj[0]['student_id'],objj[0]['subject_name']])
            stu_id.append(objj[0]['student_id'])
        
        # print(stu_id_subject)
        student_info = Student_detail.objects.filter(pk__in=stu_id).values('roll_no','std_name')
        # print(student_info)
        combine = []
        for sis in stu_id_subject:
            temp = {"roll_no":sis[0],"sub_name":sis[1]}
            for sinfo in student_info:
                if(sis[0] == sinfo['roll_no']):
                    temp["std_name"] = sinfo['std_name']
            combine.append(temp)



        # print(student_info,objj)
        max_marks_json = json.dumps(list(max_marks), cls=DjangoJSONEncoder)
        return render(request, 'student_report/home.html',{'data':json_data,'max_marks':combine})
    else:
        return render(request, 'student_report/home.html')