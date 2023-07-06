from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Dose,Patient
from api.serializer import DoseSerializer

# Create your views here.

class LastDoseView(APIView):
    
        def get(self,request,machine_id):
            print("==================1==============")
            print(machine_id)
            try:
                # last = Patient.objects.filter(machine_id=machine_id,).latest('dose_id')
                # print(last)
                last_dose = Dose.objects.filter(patient_id__machine_id__machine_id=machine_id).last()
                print("==============2==================")
                print(last_dose)
                if last_dose:
                    print("=============3===================")
                    serializer = DoseSerializer(last_dose)
                    print(serializer)
                    print(last_dose.patient_id.machine_id.machine_id)
                    print("===============4=================")
                    response_data = {
                        "Machine_id": last_dose.patient_id.machine_id.machine_id,
                        "Patient_id": last_dose.patient_id.patient_id,
                        "Patient_name": last_dose.patient_id.patient_name,
                        "Dose_id": last_dose.dose_id,
                        "Dose": last_dose.dose
                    }

                    print(response_data)
                    print("===============4=================")
                    return Response(response_data)
                else:
                    return Response({'message': 'No dose found for the given machine_id'}, status=404)

            except Dose.DoesNotExist:
                return Response({'message': 'Invalid machine id'}, status=400)
   
