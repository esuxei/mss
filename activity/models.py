from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db.models import Sum
from django.contrib import admin

# Create your models here.

class Province(models.Model):
    name = models.CharField(max_length=31)
    zipcode = models.CharField(max_length=6, blank = True)
    created_date = models.DateTimeField(auto_now_add = True, blank = True)
    modified_date = models.DateTimeField(auto_now = True, blank = True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return '%s' % self.name

class Soum(models.Model):
    name = models.CharField(max_length=31)
    zipcode = models.CharField(max_length=6, blank = True)
    province = models.OneToOneField(Province, related_name="soum_province")
    created_date = models.DateTimeField(auto_now_add = True, blank = True)
    modified_date = models.DateTimeField(auto_now = True, blank = True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return '%s' % self.name

class Bag(models.Model):
    number = models.IntegeerField(blank = True)
    name = models.CharField(max_length=31)
    soum = models.OneToOneField(Soum, related_name="bag_soum")
    zipcode = models.CharField(max_length=6, blank = True)
    created_date = models.DateTimeField(auto_now_add = True, blank = True)
    modified_date = models.DateTimeField(auto_now = True, blank = True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return '%s' % self.name

class OfficeType(models.Model):
    name = models.CharField(max_length=31)
    description = models.CharField(max_length=61)
    created_date = models.DateTimeField(auto_now_add = True, blank = True)
    modified_date = models.DateTimeField(auto_now = True, blank = True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return '%s' % self.name

class Position(models.Model):
    office_type = models.OneToOneField(OfficeType, related_name="position_office_type")
    name = models.CharField(max_length=31)
    description = models.CharField(max_length=61)
    created_date = models.DateTimeField(auto_now_add = True, blank = True)
    modified_date = models.DateTimeField(auto_now = True, blank = True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return '%s' % self.name

class Office(models.Model):
    name = models.CharField(max_length=127)
    province = models.ManyToManyField(Province, related_name="office_province", blank = True)
    soum = models.ManyToManyField(Soum, related_name="office_soum", blank = True)
    bag = models.ManyToManyField(Bag, related_name="office_bag", blank = True)
    t0 = models.CharField(max_length=15)
    t1 = models.CharField(max_length=15)
    telephone = models.CharField(max_length=63,blank=True)
    address = models.TextField(blank=True)
#    office_types = (
#        ('AP', 'AP office'),
#        ('PRJ', 'Project office'),
#        ('CLR', 'Cluster office'),
#        ('NO', 'National office'),
#    )
#    type = models.CharField(max_length=15, choices=office_types, default='ADP')
    type = models.OneToOneField(OfficeType, related_name="office_province", blank = True)
    created_date = models.DateTimeField(auto_now_add = True, blank = True)
    modified_date = models.DateTimeField(auto_now = True, blank = True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ManyToManyField(Office, related_name="profile_department")
    position = models.ManyToManyField(Position, related_name="profile_position")
    created_date = models.DateTimeField(auto_now_add = True, blank = True)
    modified_date = models.DateTimeField(auto_now = True, blank = True)
    def __str__(self):
        return '%s' % self.user.username

class Target(models.Model):
    name = models.CharField(max_length=63)
    description = models.CharField(max_length=127)
    created_date = models.DateTimeField(auto_now_add = True, blank = True)
    modified_date = models.DateTimeField(auto_now = True, blank = True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

class Indicator(models.Model):
    target = models.OneToOneField(Target)
    code = models.CharField(max_length=9, blank=True)
    logframe_code = models.CharField(max_length=8, blank=True)
    name = models.CharField(max_length=255)
    hint = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    groups = (
        ('CESP', 'CESP'),
        ('CPTP', 'CPTP'),
        ('RLTP', 'RLTP'),
    )
    group = models.CharField(max_length=4, choices=groups, default='CESP')
    order = models.IntegerField(default=0)
    enabled = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add = True, blank = True)
    modified_date = models.DateTimeField(auto_now = True, blank = True)

#    class Meta:
#        permissions = (
#            ('view_Indicator', 'Can view indicator'),
#            ('edit_Indicator', 'Can edit indicator'),
#            ('delete_Indicator', 'Can delete indicator'),
#            ('import_Indicator', 'Can import indicator'),
#            ('export_indicator', 'Can export indicator'),
#        )

    def __str__(self):
        return self.name

def increment_objective_number():
    last_objective = Objective.objects.all().order_by('id').last()
    if not last_objective:
        return 'OBJ00001'
    objective_no = last_objective.number
    objective_int = int(objective_no.split('OBJ')[-1])
    width = 5
    new_objective_int = objective_int + 1
    formatted = (width - len(str(new_objective_int))) * "0" + str(new_objective_int)
    new_objective_no = 'OBJ' + str(formatted)
    return new_objective_no

class Objective(models.Model):
    number = models.CharField(max_length=15, default=increment_objective_number, null=True, blank=True, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    name = models.CharField(max_length=127)
    office = models.OneToOneField(Office)
    enabled = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add = True, blank = True)
    modified_date = models.DateTimeField(auto_now = True, blank = True)

    def __str__(self):
        return self.name

class ObjectiveJournal(models.Model):
    objective = models.OneToOneField(Objective)
    indicator = models.OneToOneField(Indicator)
    target = models.IntegerField()
    order = models.IntegerField(default=0)
    enabled = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add = True, blank = True)
    modified_date = models.DateTimeField(auto_now = True, blank = True)

    def __str__(self):
        return self.name

class ActivityJournal(models.Model):
    objective = models.OneToOneField(Objective)
    indicator = models.OneToOneField(Indicator)
    target = models.IntegerField()
    order = models.IntegerField(default=0)
    enabled = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add = True, blank = True)
    modified_date = models.DateTimeField(auto_now = True, blank = True)

    def __str__(self):
        return self.name