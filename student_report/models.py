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




#Marks model
class mark(models.Model):
    Sub_code = (
        ('001', '001'),
        ('002', '002'),
        ('003', '003'),
        ('004', '004'),
        ('005', '005'),
    )
    Sub_name = (
        ('Physics', 'Physics'),
        ('Chemistry', 'Chemistry'),
        ('Maths', 'Maths'),
        ('Music', 'Music'),
        ('Computers', 'Computers'),
    )
    student = models.ForeignKey(Student_detail,related_name='marks',on_delete=models.CASCADE)
    subject_code = models.CharField(max_length=10,choices=Sub_code, default='0')
    subject_name = models.CharField(max_length=50, choices=Sub_name, default='0')
    marks = models.DecimalField(max_digits = 5,decimal_places = 2)


    @property
    def roll_no(self):
        return self.student.roll_no
     
    @property
    def student_name(self):
        return self.student.student_name



