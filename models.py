from django.db import models

from django.contrib import admin

class School(models.Model):
    TYPE_OF_SCHOOL =(
                     ("basic", "basic"),
                     ("secondary","secondary"),
                     ("secondary_technical", "secondary_techinical"),
                     ("techincal", "techinical"),
                     ("college","college") 
)    

    school_id = models.IntegerField(primary_key=True,max_length = 20)
    school_name = models.CharField(max_length = 100)
    type_of_school = models.CharField(choices = TYPE_OF_SCHOOL,max_length = 20)
    location = models.CharField(max_length = 100)
    population = models.IntegerField(blank = True)
    conctact = models.IntegerField(max_length = 14)
    email = models.EmailField(max_length = 75, blank = True) 
    url = models.URLField(max_length = 200,blank = True,verify_exists=False)

    def __unicode__ (self):
        return (self.school_name)

    class Meta:
        db_table = 'school'
        
'''     
    
class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length = 100)
    hall = models.CharField(max_length = 100)
    course = models.CharField(max_length = 100)
    bill = models.IntegerField(max_length =10)
    guardian_name = models.CharField(max_length= 100)
    class_name = models.CharField(max_length= 20)
    guardian_contact = models.CharField(max_length= 100)
   
    def __unicode__(self):
        return (self.student_name)

    class Meta:
        db_table = 'student'
    ordering = ['student_name'] #odering by student_name ascending

class Report(models.Model):
    student_name = models.CharField(max_length=100)
    #subject = will work on that latter
    class_score = models.IntegerField(max_length= 2)
    exams_score = models.IntegerField(max_length =2)
    total_score = models.IntegerField(max_length =3)
    grade = models.CharField(max_length =1)
    aggregate = models.IntegerField(max_length=2)

    def __uncode__ (self):
        return (self.grade)


    class Meta:
        db_table = 'report'

        
class Bill(models.Model):
    amnt_paid = models.IntegerField(max_length=10)
    amnt_due =models.IntegerField(max_length=10)
    balance = models.IntegerField(max_length=10)
    message = models.TextField(max_length= 60)

    def __unicode__(self):
        return self.amnt_paid


    class Meta:
        db_table = 'bill'
        
class Teacher(models.Model):
    name = models.CharField(max_length= 100)
    classes = models.CharField(max_length = 20)
    course = models.CharField(max_length = 100)


    def __unicode__(self):
        return (self.name)


    class Meta:
        db_table = 'teacher'
        
class Course(models.Model):
    name = models.CharField(max_length = 100)
    num_of_subj = models.IntegerField(max_length= 10)
    electives = models.CharField(max_length =4)
    cores = models.CharField(max_length=4)


    def __unicode__(self):
        return (self.name)


    class Meta:
        db_table = 'course'
        
    
'''
