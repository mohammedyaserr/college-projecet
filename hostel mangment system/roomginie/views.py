from django.shortcuts import render,redirect,HttpResponse
from .models import studentregister,parentregister
from django.contrib.auth import logout
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,'index.html')

def admindash(request):
    if 'us' in request.session:
        try:
            scount=studentregister.objects.count()
            print(scount)
            return render(request,'admindash.html',{'scount':scount})
        except:
            return redirect('adminlogin')
    else:
        return redirect('adminlogin')

def studentreg(request):
    if request.method=='POST':
        name=request.POST.get('sname')
        email=request.POST.get('email')
        phoneno=request.POST.get('phno')
        image=request.FILES.get('img')
        studentid=request.POST.get('stid')
        password=request.POST.get('paswrd')
        DOB=request.POST.get('dob')
        age=request.POST.get('age')
        fathername=request.POST.get('fname')
        mothername=request.POST.get('mname')
        parentno=request.POST.get('parentno')
        admissionno=request.POST.get('admno')
        joindate=request.POST.get('jdate')
        department=request.POST.get('dpt')
        bloodgroup=request.POST.get('bloodgrp')
        gender=request.POST.get('gender')
        address=request.POST.get('adrs')
        if studentregister.objects.filter(email=email,stid=studentid).exists(): 
            alert="<script>alert('This user already exists');window.location.href='/index/' ;</script>"  #change this when login page gets created(index)
            return HttpResponse(alert)
        object=studentregister(sname=name,
                               email=email,
                               phno=phoneno,
                               img=image,
                               stid=studentid,
                               paswrd=password,
                               dob=DOB,
                               adrs=address,
                               age=age,
                               fname=fathername,
                               mname=mothername,
                               admno=admissionno,
                               jdate=joindate,
                               dpt=department,
                               bloodgrp=bloodgroup,
                               gender=gender,
                               parentno=parentno,
                               )
        object.save()
        return redirect('parentregister')   #change index when login 
    return render(request,'studentregister.html')

def studentlog(request):
    if request.method == "POST":
        studentid=request.POST.get("stid")
        password=request.POST.get("paswrd")
        st=studentregister.objects.filter(stid=studentid,paswrd=password)
        if st:
            st1=studentregister.objects.get(stid=studentid,paswrd=password)
            id=st1.id
            studentid=st1.stid
            password=st1.paswrd
            request.session["id"]=id
            request.session["stid"]=studentid
            request.session["paswrd"]=password
            return redirect('index') 
        return render(request,'studentlogin.html',{'error':'incorrect studentid or password'})
    return render(request,'studentlogin.html')

def adminlog(request):
    if request.method == 'POST':
        username=request.POST.get("usrn")
        password=request.POST.get("paswrd")
        u="admin"
        p="12345678"
        if username==u and password==p:
            request.session['us']=username
            request.session['pw']=password
            return redirect("admindash")
        return render(request,'adminlogin.html',{'error':'incorrect username or password'})
    return render(request,'adminlogin.html')
        
def parentreg(request):
    if request.method == 'POST':
        parentname=request.POST.get('pname')
        studentname=request.POST.get('sname')
        phoneno=request.POST.get('phno')
        address=request.POST.get('adrs')
        parentid=request.POST.get('pid')
        password=request.POST.get('pas')

        object=parentregister(pname=parentname,
                              phno=phoneno,
                              pid=parentid,
                              pas=password,
                              adrs=address,
                              sname=studentname,
                              )
        object.save()
        return redirect('admindash')   #change index when login 
    return render(request,'parentregister.html')

def parentlog(request):
    if request.method == "POST":
        parentid=request.POST.get("pid")
        password=request.POST.get("pas")
        p=parentregister.objects.filter(pid=parentid,pas=password)
        if p:
            p1=parentregister.objects.get(pid=parentid,pas=password)
            id=p1.id
            parentid=p1.pid
            password=p1.pas
            request.session["id"]=id
            request.session["pid"]=parentid
            request.session["pas"]=password
            return redirect('index') 
        return render(request,'parentlogin.html',{'error':'incorrect parentid or password'})
    return render(request,'parentlogin.html')

def matronlog(request):
    if request.method == 'POST':
        username=request.POST.get("usrn")
        password=request.POST.get("paswrd")
        u="warden"
        p="12345678"
        if username==u and password==p:
            request.session["u"]=username
            request.session["p"]=password
            return redirect("matrondash")
        return render(request,'matronlogin.html',{'error':'incorrect username or password'})
    return render(request,'matronlogin.html')
        
def liststudents(request):
    st=studentregister.objects.all()
    return render(request,'studentlist.html',{'std':st})

def delstudent(request,sid):
    try:
        dl=studentregister.objects.get(id=sid)
        dl.delete()
        alert="<script>alert('Student deleted successfully'); window.location.href='/studentlist/' ;</script>"  #change this when login page gets created(index)
        return HttpResponse(alert)
    except:
        alert="<script>alert('Unexpected error occured'); window.location.href='/studentlist/' ;</script>"  #change this when login page gets created(index)
        return HttpResponse(alert)

def editstudent(request,sid):
    try:
        dl=studentregister.objects.get(id=sid)
    except:
        alert="<script>alert('Unexpected error occured'); window.location.href='/studentlist/' ;</script>"  #change this when login page gets created(index)
        return HttpResponse(alert)
    if request.method=='POST':
        name=request.POST.get('sname')
        email=request.POST.get('email')
        phoneno=request.POST.get('phno')
        image=request.FILES.get('img')
        studentid=request.POST.get('stid')
        password=request.POST.get('paswrd')
        DOB=request.POST.get('dob')
        age=request.POST.get('age')
        fathername=request.POST.get('fname')
        mothername=request.POST.get('mname')
        parentno=request.POST.get('parentno')
        admissionno=request.POST.get('admno')
        joindate=request.POST.get('jdate')
        department=request.POST.get('dpt')
        bloodgroup=request.POST.get('bloodgrp')
        gender=request.POST.get('gender')
        address=request.POST.get('adrs')
        if email!=dl.email and  studentregister.objects.filter(email=email).exists(): 
            alert="<script>alert('This user already exists');window.location.href='/studentlist/' ;</script>"  #change this when login page gets created(index)
            return HttpResponse(alert)
        dl.sname=name
        dl.email=email
        dl.phno=phoneno
        if image:
            dl.img=image
        dl.stid=studentid
        dl.paswrd=password
        dl.dob=DOB
        dl.age=age
        dl.fname=fathername
        dl.mname=mothername
        dl.parentno=parentno
        dl.admno=admissionno
        dl.jdate=joindate
        dl.dpt=department
        dl.bloodgrp=bloodgroup
        dl.gender=gender
        dl.adrs=address
        dl.save()
        alert="<script>alert('Profile updated successfully');window.location.href='/studentlist/' ;</script>"  #change this when login page gets created(index)
        return HttpResponse(alert)
    else:
        return render(request,'editprofile.html',{'std':dl})

def editparent(request,pid):
    try:
        dl=parentregister.objects.get(id=pid)
    except:
        alert="<script>alert('Unexpected error occured'); window.location.href='/studentlist/' ;</script>"  #change this when login page gets created(index)
        return HttpResponse(alert)
    if request.method=='POST':
        parentname=request.POST.get('pname')
        phoneno=request.POST.get('phno')
        address=request.POST.get('adrs')
        parentid=request.POST.get('pid')
        password=request.POST.get('pas')

        
        dl.pname=parentname
        dl.phno=phoneno
        dl.adrs=address
        dl.pid=parentid
        dl.pas=password
        dl.save()
        alert="<script>alert('Parent updated successfully');window.location.href='/parentlist/' ;</script>"  #change this when login page gets created(index)
        return HttpResponse(alert)
    else:
        return render(request,'editparentprofile.html',{'std':dl})

def about(request):
    return render(request,'about.html')

def matrondash(request):
    if 'u' in request.session:
        try:
            scount=studentregister.objects.count()
            print(scount)
            return render(request,'matrondash.html',{'scount':scount})
        except:
            return redirect('matronlogin')
    else:
        return redirect('matronlogin')

def liststudentsmatron(request):
    st=studentregister.objects.all()
    return render(request,'studentlistmatron.html',{'std':st})

def userlogout(request):
    return render(request,'logout.html')
def logout(request):
    request.session.flush()
    return redirect('index')

def listparents(request):
    st=parentregister.objects.all()
    return render(request,'parentlist.html',{'std':st})

def listparentsmatron(request):
    st=parentregister.objects.all()
    return render(request,'parentlistmatron.html',{'std':st})

# def assignroom(request):
#     if request.method='POST':
#         roomno=request.POST.get('rmno')
#         stname=request.POST.get('sname')
#         status=request.POST.get('status')
#         stcount=request.POST.get('scount')





    
    



    

    
            
    

