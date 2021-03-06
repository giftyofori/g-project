from django.db import models
from django.contrib import admin


        
class Teacher(models.Model):
    name = models.CharField(max_length= 100)
    classes = models.CharField(max_length = 20)
    course = models.CharField('Subject',max_length = 100)
    #school = models.ForeignKey(School)
    #student = models.ManyToManyField(Student,related_name = 'teachers')
    

    def __unicode__(self):
        return (self.name)


    class Meta:
        db_table = 'teacher'

class Bill(models.Model):
    amnt_paid = models.IntegerField(max_length=10)
    amnt_due =models.IntegerField(max_length=10)
    balance = models.IntegerField(max_length=10)
    message = models.TextField(max_length= 60)
    #student = models.ManyToManyField(Student)


    def __unicode__(self):
        return self.amnt_paid


    class Meta:
        db_table = 'bill'

       
class Course(models.Model):
    # calculates the number of course entered
    def cal_courses():
        if elective1:
            number_of_subj = 5
        if elective2:
            number_of_subj = 6
        if elective3:
            number_of_subj = 7
        if elective4:
            number_of_subj = 8
    pass 


    #to_student = models.ForeignKey(Student, related_name = 'for_couses')
    name = models.CharField(max_length = 100)
    num_of_subj = models.IntegerField(max_length= 10)
    elective1 = models.CharField(max_length =4)
    elective2 = models.CharField(max_length =4)
    elective3 = models.CharField(max_length =4)
    elective4 = models.CharField(max_length =4)
    core1 = models.CharField(max_length=4)
    core2 = models.CharField(max_length=4)
    core3 = models.CharField(max_length=4)
    core4 = models.CharField(max_length=4)
    #student = models.ForeignKey(Student, related_name = 'courses')
    teachers = models.ManyToManyField(Teacher, related_name = 'courses')



    def __unicode__(self):
        return (self.name)


    class Meta:
        db_table = 'course'

   
    
class Student(models.Model):
    
    
    first_Name = models.CharField("Surname" ,max_length = 100 , help_text = "Enter Your Surname")
    last_Name = models.CharField(max_length = 100, help_text ="Enter Your Last Name And Any Other Name")
    guardian_name = models.CharField(max_length= 100)
    class_name = models.CharField(max_length= 20)
    guardian_contact = models.CharField(max_length= 100)
    to_courses = models.ForeignKey(Course, related_name = 'for_couses')
    bill = models.ForeignKey(Bill, related_name = 'bill')
    
    
   
    def __unicode__(self):
        return (self.first_Name)

    class Meta:
        db_table = 'student'
        ordering = ['first_Name'] #odering by student_name ascending



class School(models.Model):
    TYPE_OF_SCHOOL =(
                     ("basic", "basic"),
                     ("secondary","secondary"),
                     ("secondary_technical", "secondary_techinical"),
                     ("techincal", "techinical"),
                     ("college","college") 
)    
    #student = models.ForeignKey(Student)
    school_id = models.IntegerField(primary_key=True,max_length = 20)
    school_name = models.CharField(max_length = 100)
    type_of_school = models.CharField(choices = TYPE_OF_SCHOOL,max_length = 20)
    location = models.CharField(max_length = 100)
    population = models.IntegerField(blank = True)
    conctact = models.IntegerField(max_length = 14)
    email = models.EmailField(max_length = 75, blank = True) 
    url = models.URLField(max_length = 200,blank = True)


    def __unicode__ (self):
        return (self.school_name)

    class Meta:
        db_table = 'school'



        

class Teacher(models.Model):
    name = models.CharField(max_length= 100)
    classes = models.CharField(max_length = 20)
    course = models.CharField(max_length = 100)
    #school = models.ForeignKey(School)
    #student = models.ManyToManyField(Student,related_name = 'teachers')
    

    def __unicode__(self):
        return (self.name)


    class Meta:
        db_table = 'teacher'

class Report(models.Model):
    #student = models.ForeignKey(Student, unique = True)
    #teacher = models.ManyToManyField(Teacher, related_name= 'report')
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

        

class Hall(models.Model):
    name = models.CharField(max_length = 30)
    hall_teacher = models.CharField(max_length = 30)
    population = models.IntegerField(max_length = 124)
    #student = models.ForeignKey(Student, related_name = 'halls')
    #school = models.ForeignKey(School, related_name = 'halls')
    

admin.site.register(School)
admin.site.register(Student)
admin.site.register(Report)
admin.site.register(Bill)
admin.site.register(Teacher)
admin.site.register(Course)
