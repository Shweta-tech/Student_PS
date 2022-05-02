# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# # Create your views here.
# from rest_framework import permissions
# from django.contrib.auth.models import User, Group
from rest_framework import viewsets
# from rest_framework import permissions
from student_report.models import Student_detail,subject,mark
from .serializers import UserSerializer, GroupSerializer,MarkSerializer


class StudentAPI(viewsets.ModelViewSet):
    queryset=Student_detail.objects.all()
    serializer_class = UserSerializer


class MarksAPI(viewsets.ModelViewSet):
    queryset=mark.objects.all()
    serializer_class = MarkSerializer   
# class UserViewSet(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # def get_object(self, roll_no):
    #     '''
    #     Helper method to get the object with given roll_no
    #     '''
    #     try:
    #         print(mark.objects.all()[0])
    #         return mark.objects.filter(roll_no=roll_no)
    #     except mark.DoesNotExist:
    #         return None

    # # 3. Retrieve
    # def get(self, request, roll_no, *args, **kwargs):
    #     '''
    #     Retrieves the Student_detail with given roll_no
    #     '''
    #     todo_instance = self.get_object(roll_no)
    #     serializer = MarkSerializer(todo_instance)
    #     print(serializer)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    # # 4. Update
    # def put(self, request, roll_no, *args, **kwargs):
    #     '''
    #     Updates the todo item with given roll_no if exists
    #     '''
    #     todo_instance = self.get_object(roll_no, request.user.id)
    #     if not todo_instance:
    #         return Response(
    #             {"res": "Object with todo id does not exists"}, 
    #             status=status.HTTP_400_BAD_REQUEST
    #         )
    #     data = {
    #         'task': request.data.get('task'), 
    #         'completed': request.data.get('completed'), 
    #         'user': request.user.id
    #     }
    #     serializer = UserSerializer(instance = todo_instance, data=data, partial = True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # # 5. Delete
    # def delete(self, request, roll_no, *args, **kwargs):
    #     '''
    #     Deletes the todo item with given roll_no if exists
    #     '''
    #     todo_instance = self.get_object(roll_no, request.user.id)
    #     if not todo_instance:
    #         return Response(
    #             {"res": "Object with todo id does not exists"}, 
    #             status=status.HTTP_400_BAD_REQUEST
    #         )
    #     todo_instance.delete()
    #     return Response(
    #         {"res": "Object deleted!"},
    #         status=status.HTTP_200_OK
    #     )
# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Student_detail.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]

