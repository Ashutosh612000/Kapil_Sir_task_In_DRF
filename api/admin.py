from django.contrib import admin
from api.models import Machine,Patient,Dose

# Register your models here.
class MachineAdmin(admin.ModelAdmin):
    list_display = ['machine_id','machine_name']

class PatientAdmin(admin.ModelAdmin):
    list_display = ['patient_id','machine_id','patient_name']

class DoseAdmin(admin.ModelAdmin):
    list_display = ['dose_id','dose','patient_id']

# class PatientsAdmin(admin.ModelAdmin):
#     list_display = ['patient_id','machine_id','patient_name']


admin.site.register(Machine,MachineAdmin)
admin.site.register(Patient,PatientAdmin)
admin.site.register(Dose,DoseAdmin)