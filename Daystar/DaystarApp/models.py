from django.db import models
from django.utils import timezone

# Create your models here.
class Categorystay(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)
    def __str__(self):
        return self.name
    

class Sitter(models.Model):
    RELIGION_CHOICES = (
        ('Christian', 'Christian'),
        ('Muslim', 'Muslim'),
        ('Other', 'Other'),
    )
    EDUCATION_LEVEL_CHOICES = (
        ('Primary', 'Primary'),
        ('Secondary', 'Secondary'),
        ('University', 'University'),
    )
    S_name = models.CharField(max_length=200,null=True,blank=True)
    gender = models.CharField(choices=[('female', 'female'),('male','male')], max_length=100, null=False)
    dob = models.DateTimeField()
    location = models.CharField(max_length=200, default="Kabalaga")
    next_of_kin = models.CharField(max_length=200)
    recommenders_name = models.CharField(max_length=200)
    religion = models.CharField(max_length=100, choices=RELIGION_CHOICES, blank=True)
    NIN = models.CharField(max_length=30, unique=True)
    education_level = models.CharField(max_length=200, choices=EDUCATION_LEVEL_CHOICES)
    sitter_number = models.CharField(max_length=200, unique=True)
    contact = models.IntegerField(null= True)
    def __str__(self):
        return self.S_name
    

    
class BabyReg(models.Model):
    B_name = models.CharField(max_length=100,null=True, blank=True)
    age = models.CharField(max_length=100,null=True, blank=True)
    gender = models.CharField(choices=[('female', 'female'),('male','male')], max_length=100, null=False)
    location = models.CharField(max_length=100,null=True,)
    mothers_name = models.CharField(max_length=100, null=True, blank=True)
    fathers_name = models.CharField(max_length=100, null=True, blank=True)
    mothers_phone = models.IntegerField(null=True, blank=True)
    fathers_phone = models.IntegerField(null=True, blank=True)
    B_number = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.B_name
    
class BabyAttendance(models.Model):
    B_name = models.ForeignKey(BabyReg, on_delete=models.CASCADE,null=True, blank=True)
    c_stay = models.ForeignKey(Categorystay, on_delete=models.CASCADE,null=True, blank=True)
    brought_by = models.CharField(max_length=100, null=True, blank=True)
    timeIn = models.DateTimeField(auto_now_add=True)
    timeOut = models.DateTimeField(null=True,blank=True)
    assignSitter = models.ForeignKey(Sitter, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
       return str(self.B_name)   

class SitterAttendance(models.Model):
    S_name = models.ForeignKey(Sitter, on_delete=models.CASCADE,null=True, blank=True)
    assign_baby =  models.ForeignKey(BabyReg, on_delete=models.CASCADE,null=True, blank=True) 
    timeIn = models.DateTimeField()
    timeOut = models.DateTimeField()
   
    def __str__(self):
        return str(self.S_name)


class Category_doll(models.Model):  
     name = models.CharField(max_length=100,null=True, blank=True)
     def __str__(self):
         return str(self.name)
       
class Doll(models.Model):
    c_doll=models.ForeignKey(Category_doll, on_delete=models.CASCADE,null=True, blank=True)
    doll_name =models.CharField(max_length=200,null=True, blank=True)
    doll_number = models.CharField(max_length=200,null=True, blank=True)
    quantity=models.IntegerField(default=0)
    issued_quantity=models.IntegerField(default=0,blank=True,null=True) 
    received_quantity=models.IntegerField(default=0,null=True,blank=True)
    unit_price=models.IntegerField(default=0,null=True, blank=True)
    date=models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return self.doll_name
    
class Salesrecord(models.Model):    
    doll=models.ForeignKey(Doll, on_delete=models.CASCADE,null=False, blank=False)
    payee = models.ForeignKey(BabyReg, on_delete=models.SET_NULL, null=True, blank=True)
    quantity_sold=models.IntegerField(default=0)
    amount_received=models.IntegerField(default=0)
    sale_date=models.DateTimeField(null=True,blank=True)
    unit_price=models.IntegerField(default=0)
    def __str__(self):
        return str(self.payee)

    def get_total(self):
        total= self.quantity_sold * self.unit_price
        return int( total)
#here we are getting change.(money to be given to the parent)    
    def get_change(self):
        change= self.get_total() - self.amount_received
        return int(change)

class Payment(models.Model):
    S_name = models.ForeignKey(Sitter, on_delete=models.CASCADE,null=True, blank=True)
    HALF_DAY = 'half_day'
    FULL_DAY = 'full_day'
    PAYMENT_CHOICES = [
        (HALF_DAY, 'Half Day Payment (10,000 UGX)'),
        (FULL_DAY, 'Full Day Payment (15,000 UGX)'),
    ]
    payment_type = models.CharField(max_length=10, choices=PAYMENT_CHOICES)
    date = models.DateTimeField(null=True,blank=True)
    babies_assigned = models.IntegerField(default=0) 
    amount = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return f"{self.S_name} - {self.get_payment_type_display()}"
    
    def total(self):
        total = self.babies_assigned * self.amount
        return int(total)
