from django.urls import path
from .views import home,bulk_validate,get_job_status,get_job_results

urlpatterns=[
    path("",home),
    path("v0/bulk",bulk_validate),
    path("v0/bulk/<int:job_id>",get_job_status),
    path("v0/bulk/<int:job_id>/result",get_job_results)

]