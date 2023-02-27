from django.shortcuts import render
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.http import HttpResponse
import csv

# Create your views here.

def check_single_mail(email):
    url=f'http://103.134.217.133:8080/v0/check_email'
    payload={
        "to_email":email
    }
    res=requests.post(url=url,json=payload)
    return res.json()


@csrf_exempt
@api_view(['GET', 'POST'])
def bulk_validate(req):
    if req.method == "POST":
        emails=req.data["emails"]
        res=requests.post("http://103.134.217.133:8080/v0/bulk",json={
                    "input_type": "array",            
                    "input": emails
        })
        print(res.text)
        data = res.json()
        return JsonResponse({
            "job_id":data["job_id"]
        })

def get_job_status(req,job_id):
    res=requests.get(f"http://103.134.217.133:8080/v0/bulk/{job_id}")
    return JsonResponse(res.json())

def get_job_results(req,job_id):
    res=requests.get(f"http://103.134.217.133:8080/v0/bulk/{job_id}/results?format=csv")

    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="filename.csv"'},
    )
    response.write(res.content)
    return response
def home(request):
    if request.method=="POST":
        email=request.POST["email"]
        print(email)
        response=check_single_mail(email)
        print(response)
        return render(request,"home.html",context={
            "data":response,
            "email":response["input"],
            "is_reachable":response["is_reachable"],
            "mx":response["mx"]["records"]
        })
    return render(request,"home.html")