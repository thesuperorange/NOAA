from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView
from django.conf import settings
import os
import sys
import subprocess

def media_metadata(request):
    path = settings.MEDIA_ROOT #"/Users/peggy/PycharmProjects/NOAA/myapp/static/media"  # insert the path to your directory
    media_date_list = []
    for filename in os.listdir(path):
        module_name, ext =os.path.splitext(filename)
        if ext == '.mp4':
            try:
                media_date_list.append(module_name)
            except Exception as e:
                sys.stderr.write('error: %s: %s\n' % (filename, e))



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
