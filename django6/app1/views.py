from django.shortcuts import render
from app1.forms import inputforms
# Create your views here.
def home(request):
    ip1=" "
    ip2=""
    ip3=""
    if request.method=="POST":
        form1=inputforms(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            ip1=data.get("name")
            ip2=data.get("clg")
            ip3=data.get("crs")
            import mysql.connector as mc
            conne=mc.connect(
                host="localhost",
                user="root",
                password="pass@12",
                database="db1"
            )
            cursor2=conne.cursor()
            ip0="1"
            s1="insert into registrations(id,name,college,course)values(ip0,ip1,ip2,ip3)"
            #s2=")"
            #sfinal=s1+ip0+",'"+ip1+"','"+ip2+"','"+ip3+"'"+s2
            #print(sfinal)
            cursor2.execute(s1)
            conne.commit()
            conne.close()
            return render(request,"app1/index.html",{'param1':ip1, 'param2':ip2,'param3':ip3, 'form':form1})
    else:
        
    
        form1=inputforms()

    return render(request,"app1/index.html",{'param1':ip1, 'param2':ip2,'param3':ip3, 'form':form1})