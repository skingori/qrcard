from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Profile(models.Model):
    service_number = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, primary_key=True)
    unit = models.CharField(max_length=200)
    rank = models.CharField(max_length=200)
    sub_unit = models.CharField(max_length=200)
    Religion = models.CharField(max_length=200)
    Date_of_birth = models.DateField()
    lsgcCount = models.CharField(max_length=200)
    ROD = models.CharField(max_length=200)
    Pension = models.CharField(max_length=200)
    civilian_id_no = models.CharField(max_length=200)
    service_id_no = models.CharField(max_length=200)
    kra_no = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)

    def __str__(self):
        return str(self.service_number)

    class Meta:
        ordering = ['service_number']
        verbose_name = 'Profile'
        verbose_name_plural = 'Service Members'
        db_table = 'Profile'


class Promotion(models.Model):
    service_number = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, primary_key=True)
    rank = models.CharField(max_length=200)
    part2order = models.CharField(max_length=200)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.service_number)

    class Meta:
        ordering = ['service_number']
        verbose_name = 'Promotion'
        verbose_name_plural = 'Promotions'
        db_table = 'Promotions'


class PayGroup(models.Model):
    service_number = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, primary_key=True)
    pay_group = models.CharField(max_length=200)
    part2order = models.CharField(max_length=200)
    from_date = models.DateTimeField(null=True, blank=True)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.service_number)

    class Meta:
        ordering = ['service_number']
        verbose_name = 'PayGroup'
        verbose_name_plural = 'PayGroup'
        db_table = 'PayGroups'


class Qualifications(models.Model):
    service_number = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, primary_key=True)
    Group = models.CharField(max_length=200)
    Class = models.CharField(max_length=200)
    part2order = models.CharField(max_length=200)

    def __str__(self):
        return str(self.service_number)

    class Meta:
        ordering = ['service_number']
        verbose_name = 'Qualification'
        verbose_name_plural = 'Qualifications'
        db_table = 'Qualifications'


class InstructionalCourses(models.Model):
    service_number = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, primary_key=True)
    course_results = models.CharField(max_length=200)
    course_type = models.CharField(max_length=200)
    course_place = models.CharField(max_length=200)
    part2order = models.CharField(max_length=200)

    def __str__(self):
        return str(self.service_number)

    class Meta:
        ordering = ['service_number']
        verbose_name = 'Instructional Courses'
        verbose_name_plural = 'Instructional Courses'
        db_table = 'InstructionalCourses'


class TribalParticulars(models.Model):
    service_number = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, primary_key=True)
    chief = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    sub_location = models.CharField(max_length=200)
    headman = models.CharField(max_length=200)

    def __str__(self):
        return str(self.service_number)

    class Meta:
        ordering = ['service_number']
        verbose_name = 'Particular'
        verbose_name_plural = 'Particulars'
        db_table = 'TribalParticulars'


class Kinship(models.Model):
    service_number = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, primary_key=True)
    name = models.CharField(max_length=200)
    relationship = models.CharField(max_length=200)
    tribe = models.CharField(max_length=200)
    chief = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return str(self.service_number)

    class Meta:
        ordering = ['service_number']
        verbose_name = 'Kinship'
        verbose_name_plural = 'Kinship'
        db_table = 'Kinship'


class WifeDetails(models.Model):
    service_number = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, primary_key=True)
    wife_name = models.CharField(max_length=200)
    date_of_marriage = models.CharField(max_length=200)
    place_of_marriage = models.CharField(max_length=200)
    part2order = models.CharField(max_length=200)
    address = models.TextField(max_length=200)

    def __str__(self):
        return str(self.service_number)

    class Meta:
        ordering = ['service_number']
        verbose_name = 'Wife Details'
        verbose_name_plural = 'Wife Details'
        db_table = 'WifeDetails'


class ChildrenDetails(models.Model):
    service_number = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, primary_key=True)
    date_of_birth = models.DateTimeField()
    sex = models.DateTimeField()
    part2order = models.CharField(max_length=200)

    def __str__(self):
        return str(self.service_number)

    class Meta:
        ordering = ['service_number']
        verbose_name = 'Children Details'
        verbose_name_plural = 'Children Details'
        db_table = 'ChildrenDetails'


class LeaveDetails(models.Model):
    service_number = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, primary_key=True)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    leave_type = models.CharField(max_length=200)
    warrant_cash = models.CharField(max_length=200)
    family_warrant = models.CharField(max_length=200)

    def __str__(self):
        return str(self.service_number)

    class Meta:
        ordering = ['service_number']
        verbose_name = 'Leave Details'
        verbose_name_plural = 'Leave Details'
        db_table = 'LeaveDetails'


class RegimentaEntries(models.Model):
    service_number = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, primary_key=True)
    date_of_trial = models.DateTimeField()
    place_of_trial = models.CharField(max_length=200)
    trial_co_or_cm = models.CharField(max_length=200)
    part2order = models.CharField(max_length=200)
    non_reconable_service = models.CharField(max_length=200)
    offence = models.TextField(max_length=200)
    award = models.TextField(max_length=200)

    def __str__(self):
        return str(self.service_number)

    class Meta:
        ordering = ['service_number']
        verbose_name = 'Regimenta Entries'
        verbose_name_plural = 'Regimenta Entries'
        db_table = 'RegimentaEntries'


class ServiceRecords(models.Model):
    service_number = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, primary_key=True)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    country = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)
    part2order = models.CharField(max_length=200)

    def __str__(self):
        return str(self.service_number)

    class Meta:
        ordering = ['service_number']
        verbose_name = 'Service Records'
        verbose_name_plural = 'Service Records'
        db_table = 'ServiceRecords'


class Ranks(models.Model):
    rank_name = models.CharField(max_length=200)


class EmploymentDetails(models.Model):
    service_number = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, primary_key=True)
    terms_of_service = models.CharField(max_length=200)
    date_of_engagement = models.DateTimeField()
    run_out_date = models.DateTimeField()

    def __str__(self):
        return str(self.service_number)

    class Meta:
        ordering = ['service_number']
        verbose_name = 'Employment Details'
        verbose_name_plural = 'Employment Details'
        db_table = 'EmploymentDetails'
