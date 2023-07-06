from django.db import models
import uuid

class Machine(models.Model):
    machine_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    machine_name = models.CharField(max_length=40)

    
    def __str__(self):
        return f"{self.machine_id}"

class Patient(models.Model):
    patient_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    machine_id = models.ForeignKey(Machine, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.patient_id}"

class Dose(models.Model):
    dose_id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    dose = models.FloatField()
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    

# class Patients(models.Model):
#     patient_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     machine_id = models.ForeignKey(Machine, on_delete=models.CASCADE)
#     patient_name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.patient_name