from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView
import os
import subprocess

def media_metadata(request):
    path = "/Users/peggy/PycharmProjects/NOAA/myapp/static/media"  # insert the path to your directory
    media_date_list = os.listdir(path)
    #media_date_list=['20170105_00','20170115_06','20170205_00']
    date = None
    if request.method == 'POST':
            date = request.POST['select_date']



    return render(request, 'metalist.html',
                  {
                      'video_date': date,
                      'mlist':media_date_list,
                  })



def download(request):
    serverIP = "165.124.33.147"
    serverUser = "peggy"
    script="NCHC_NOAA/waitrequest.py"
    datetime = request.POST['video_date'].split("_")
    date=datetime[0]
    time = datetime[1]

    pipe =subprocess.Popen("ssh "+serverUser+"@"+serverIP+" 'python "+script+" "+date+" "+time+"'",shell=True, stdout=subprocess.PIPE)
    result = pipe.stdout.read()

    return render(request, 'download.html',
                  {
                      'video_date': date,
                      'result': result
                  })
