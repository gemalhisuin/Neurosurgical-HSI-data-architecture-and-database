from django.contrib import admin
from .models import *

 

# Register your models here.
admin.site.register(Patient)
admin.site.register(Diagnosis_history)
admin.site.register(Category)
admin.site.register(spectralImage)
admin.site.register(Address)
admin.site.register(Metadata)
admin.site.register(Imaging)
admin.site.register(Hospital)
admin.site.register(Environment)
admin.site.register(Software)
admin.site.register(Device)
admin.site.register(Light_source)
admin.site.register(Mask)
admin.site.register(Examiner)
admin.site.register(Annot_file_type)
admin.site.register(Tissue_class)
admin.site.register(Class_feature)
admin.site.register(Label_library)
admin.site.register(Annot_rate)
admin.site.register(Diagnosis)
admin.site.register(Notes)
