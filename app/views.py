from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views herefrom
def topicform(request):
    if request.method=='POST':
        tp=request.POST['tp']

        TO=Topic.objects.get_or_create(topic_name=tp)[0]
        TO.save()
        QLTO=Topic.objects.all()
        d={'topics':QLTO}
        return render(request,'dispaly_topic.html',d)
    return render(request,'topicform.html')


def Webpages(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    if request.method=="POST":
        tn=request.POST['tn']
        na=request.POST['na']
        url=request.POST['ur']
        em=request.POST['em']
        TO=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=url,email=em)[0]
        WO.save()
        QLWO=Webpage.objects.all()
        d1={'webpages':QLWO}
        return render (request,'display_webpages.html',d1)


    return render(request,'insert_webpage.html',d)


def accessrecord(request):
    QLWO=Webpage.objects.all()
    d={'webpages':QLWO}
    if request.method=='POST':
        
        na=request.POST['na']
        da=request.POST['da']
        au=request.POST['au']
        WO=Webpage.objects.get(pk=na)
        AO=AccessRecords.objects.get_or_create(name=WO,date=da,author=au)[0]
        AO.save()
        QLAO=AccessRecords.objects.all()
        d1={'accessrecords':QLAO}
        return render(request,'display_accessrecord.html',d1)
    return render(request,'insert_accessrecord.html',d)


def select_multiple_webpage(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    if request.method=='POST':
        topiclist=request.POST.getlist('tn')
        print(topiclist)
        QLWO=Webpage.objects.none()
        for i in topiclist:
            QLWO=QLWO|Webpage.objects.filter(topic_name=i)
        d1={'webpages':QLWO}
        return render (request,'display_webpages.html',d1)
    return render(request,'select_multiple_webpage.html',d)
    
def checkBox(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'checkBox.html',d)


def select_multiple_accessrecords(request):
    QLWO=Webpage.objects.all()
    d={'webpages':QLWO}
    if request.method=='POST':
        webpagelist=request.POST.getlist('pk')
        QLAO=AccessRecords.objects.none()
        for na in webpagelist:
            QLAO=QLAO|AccessRecords.objects.filter(pk=na)
        d1={'accessrecords':QLAO}
        return render (request,'display_accessrecord.html',d1)


    return render (request,'select_multiple_accessrecords.html',d)
    