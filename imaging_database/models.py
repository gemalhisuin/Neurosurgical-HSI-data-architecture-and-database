from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.urls import reverse


####
## Add slug to all the classess for better linking 
####
####
class Patient(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    # def __str__(self):
    #     return self.

class Diagnosis_history(models.Model):
    patient = models.ManyToManyField(Patient, blank= True)
    diagnosis = models.CharField(max_length=50)

    def __str__(self):
        return self.diagnosis

class Category(models.Model):
    title = models.CharField(null=True, blank=True, max_length=200)

    #utility Variable
    uniqueId = models.CharField(null=True, blank=True, max_length=200)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.title, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.title, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        super(Category, self).save(*args, **kwargs)

class spectralImage(models.Model):
    patient = models.ForeignKey(Patient, blank= True, null=True, on_delete=models.CASCADE)
    spectralimage = models.ImageField(upload_to='hsi_images/')
    rgb = models.ImageField(upload_to='RGB/')
    gray = models.ImageField(upload_to='gray/')
    description = models.TextField(null=True, blank=True)

    ##Related Fiels
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)

    

    #Utility Variable
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    # def __str__(self):
    #     return self.patient.gender
    
class Metadata(models.Model):
    spectral_image = models.OneToOneField(spectralImage, blank= True, null=True, on_delete=models.CASCADE)
    filesize = models.IntegerField()
    resolution =  models.FloatField()
    band = models.IntegerField()
    bandpassrange = models.CharField(max_length=100)
    frame = models.IntegerField()

    def __str__(self):
        return Patient.age

class Microscope(models.Model):
    image = models.ImageField(upload_to='Microscope/')

# class RGB(models.Model):
#     spectral_image = models.OneToOneField(spectralImage, blank= True, null=True, on_delete=models.CASCADE)
#     # rgb = models.ImageField(upload_to='RGB/')
#     # gray = models.ImageField(upload_to='gray/')
#     description = models.TextField(null=True, blank=True)
#     # altText = models.TextField(null=True, blank=True)

#     ##Related Fiels
#     category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)

#     #Utility Variable
#     uniqueId = models.CharField(null=True, blank=True, max_length=100)
#     slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
#     date_created = models.DateTimeField(blank=True, null=True)
#     last_updated = models.DateTimeField(blank=True, null=True)

#     def __str__(self):
#         return self.category.title

class Imaging(models.Model):
    spectral_image = models.ForeignKey(spectralImage, blank= True, null=True, on_delete=models.CASCADE)
    acquisition_type = models.CharField(max_length=100)
    light_intensity = models.FloatField()
    magnification = models.FloatField()
    focal_length = models.FloatField()

    # def __str__(self):
    #     return Patient.last_name


class Environment(models.Model):
    imaging = models.ForeignKey(Imaging, blank= True, null=True, on_delete=models.CASCADE)
    environment = models.CharField(max_length=100)

    def __str__(self):
        return Patient.last_name

class Software(models.Model):
    imaging = models.ForeignKey(Imaging, blank= True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    version = models.FloatField()

    def __str__(self):
        return Patient.last_name 

class Device(models.Model):
    imaging = models.ForeignKey(Imaging, blank= True, null=True, on_delete=models.CASCADE)
    camera_name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)

class Light_source(models.Model):
    imaging = models.ForeignKey(Imaging, blank= True, null=True, on_delete=models.CASCADE)
    light_source = models.CharField(max_length=100)

    def __str__(self):
        return self.light_source

class Mask(models.Model):
    spectral_image = models.OneToOneField(spectralImage, blank= True, null=True, on_delete=models.CASCADE) 
    mask = models.ImageField(upload_to='MASK/')
    # classImage = MultiImageField(min_num=1, max_num=20)

class Examiner(models.Model):
    annot_mask = models.ForeignKey(Mask, blank= True, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    professional_title = models.CharField(max_length=100)

    def __str__(self):
        return self.last_name

class Annot_file_type(models.Model):
    annot_mask = models.ForeignKey(Mask, blank= True, null=True, on_delete=models.CASCADE)
    software_name = models.CharField(max_length=100)
    software_version = models.CharField(max_length=100)      
    
    def __str__(self):
        return self.software_name   

class Tissue_class(models.Model):
    annot_mask = models.ForeignKey(Mask, blank= True, null=True, on_delete=models.CASCADE)
    class_type = models.CharField(max_length=100)
    classImage = models.ImageField(upload_to='classType/')
    def __str__(self):
        return self.class_type

class Class_feature(models.Model):
    tissue_class = models.ManyToManyField(Tissue_class, blank=True)
    feature_type = models.CharField(max_length=100)

    def __str__(self):
        return self.feature_type

class Label_library(models.Model):
    tissue_class = models.ForeignKey(Tissue_class, blank=True, on_delete=models.CASCADE)
    name =  models.CharField(max_length=100)
    version = models.CharField(max_length=100)   

    def __str__(self):
        return self.name

class Annot_rate(models.Model):
    annot_mask = models.OneToOneField(Mask, blank= True, on_delete=models.CASCADE)
    rate = models.FloatField()

    def __str__(self):
        return self.rate

class Diagnosis(models.Model):
    annot_mask = models.ManyToManyField(Mask, blank= True)
    patient = models.ManyToManyField(Patient, blank=True)   
    diag_type = models.CharField(max_length=100)
    level = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.diag_type

class Notes(models.Model):
    annot_mask = models.ManyToManyField(Mask, blank= True)
    notes = models.TextField()

    def __str__(self):
        return self.notes

class Hospital(models.Model):
    spectral_image = models.ForeignKey(spectralImage, blank= True, null=True, on_delete=models.CASCADE)
    examiner = models.ForeignKey(Examiner, blank= True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name     

class Address(models.Model):
    patient = models.OneToOneField(Patient, blank= True, null=True, on_delete=models.CASCADE)
    examiner = models.OneToOneField(Examiner, blank= True, null=True, on_delete=models.CASCADE)
    hospital = models.OneToOneField(Hospital, blank= True, null=True, on_delete=models.PROTECT)
    street_address = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.city   

