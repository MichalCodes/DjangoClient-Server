from django.db import models

class Person(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    birthdate = models.DateField('birthdate')
    sex = models.CharField(max_length=1)
    address = models.CharField(max_length=300)
    def __str__(self):
        return f'{self.pk}, {self.fname} {self.lname}, {self.birthdate}, {self.sex}, {self.address}'
    
class CriminalHistory(models.Model):
    crime = models.CharField(max_length=30)
    trest_type = models.CharField(max_length=30)
    start_date = models.DateField('start_date')
    end_date = models.DateField('end_date')
    person_id = models.ForeignKey('Person', blank=True, null=True, on_delete=models.SET_NULL)
    case_id = models.ForeignKey('Case', blank=True, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return f'{self.pk}, {self.crime}, {self.trest_type}, {self.start_date}, {self.end_date}, {self.person_id}, {self.case_id}'
    
class Witnes(models.Model):
    statement = models.CharField(max_length=500)
    protection = models.BooleanField()
    person_id = models.ForeignKey('Person', blank=True, null=True, on_delete=models.SET_NULL)
    case_id = models.ForeignKey('Case', blank=True, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return f'{self.pk}, {self.person_id},{self.case_id}, {self.protection}, {self.statement}'

    
class Case(models.Model):
    name = models.CharField(max_length=30)
    case_type = models.CharField(max_length=30)
    detective = models.CharField(max_length=30)
    judge = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length=500)
    criminal_history_id = models.ForeignKey('CriminalHistory', blank=True, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return f"{self.name}, {self.case_type}, {self.detective}, {self.judge}, {self.start_date}, {self.end_date}, {self.description}"
    
class Defendant(models.Model):
    person = models.ForeignKey('Person', null=True, on_delete=models.SET_NULL)
    case = models.ForeignKey('Case', null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return f'{self.pk}, {self.person}, {self.case}'
    
class Evidence(models.Model):
    e_type = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    case_id = models.ForeignKey('Case', null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return f"{self.pk}, {self.e_type}, {self.description}, {self.case_id}"
    
