from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class CustomAccountManager(BaseUserManager):
    def create_superuser(self, roll_no,password, **other_fields):
        print(other_fields)
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        # if other_fields.get('is_staff') is not True:
        #     raise ValueError(
        #         'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(roll_no,password, **other_fields)

    def create_user(self, roll_no,password, **other_fields):

      
        user = self.model(roll_no=roll_no, **other_fields)
        user.set_password(password)
        user.save()
        return user

#Student model
class Student_detail(AbstractBaseUser, PermissionsMixin):
    GENDER = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other'),
    )
    roll_no = models.CharField(max_length=10,primary_key=True)
    std_name = models.CharField(max_length=50, default='')
    std_gender = models.CharField(max_length=1, choices=GENDER, default='M')
    std_class = models.CharField(max_length=50, default='')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    objects = CustomAccountManager()

    USERNAME_FIELD = 'roll_no'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.roll_no

#Subject model
class subject(models.Model):
    subject_code = models.CharField(max_length=10,primary_key=True)
    subject_name = models.CharField(max_length=50, default='')

    def __str__(self):
        return  self.subject_name


#Marks model
class mark(models.Model):
    student = models.ForeignKey(Student_detail,on_delete=models.SET_DEFAULT,default="0000")
    subject = models.ForeignKey(subject,on_delete=models.SET_DEFAULT,default="000")
    marks = models.DecimalField(max_digits = 5,decimal_places = 2)




