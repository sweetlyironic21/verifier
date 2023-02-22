from django.shortcuts import render
import requests
# Create your views here.

def check_single_mail(email):
    url=f'http://103.134.217.133:8080/v0/check_email'
    payload={
        "to_email":email
    }
    res=requests.post(url=url,json=payload)
    return res.json()
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