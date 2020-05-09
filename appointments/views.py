from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
import json
from datetime import datetime

def index(request,hospitalId = None):

    #Load GET parameters
    start_date = request.GET.get('start')
    end_date = request.GET.get('end')

    try:
        #get appointments code to be written
        # d = datetime.strptime('2020-04-01T10:00:00.000', '%Y-%m-%dT%H:%M:%S.%f')

        #success
        api_reponse = {
            "data": 
            [
                {"start": "2020-04-01T10:00:00.000",
                "end": "2020-04-01T10:30:00.000"
                },
                {
                "start": "2020-04-01T10:30:00.000",
                "end": "2020-04-01T11:00:00.000"
                },
                {
                "start": "2020-04-01T1:00:00.000",
                "end": "2020-04-01T10:30:00.000"
                }
            ]
        } 
    except Exception as e:
        print(f"Error in fetching appointments: {e}")
        api_reponse = {
            "error": {
                "message": "Error in fetching appointments"
                }
        }

    return JsonResponse(api_reponse)

    

    