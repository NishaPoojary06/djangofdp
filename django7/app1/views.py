from django.shortcuts import render
from app1.forms import inputforms
# Create your views here.
def home(request):
    
    form1=inputforms(request.POST)
    num1=1
    num2=1
    res=[]
    if request.method=="POST" and form1.is_valid():
        
        data=form1.cleaned_data
        num1=data.get("input1")
        num2=data.get("input2")
        res=tables(num1,num2)
        return render(request,'app1/index.html',{'param1':res,'form':form1})
    else:
        res=tables(num1,num2)
        print(tables(num1,num2))
        return render(request,'app1/index.html',{'form':form1})
    

def tables(n1,n2):
    l1=[]
    str1='x'
    str2='='
    str4="--------      "
    if n1>n2:
        n1,n2=n2,n1
    for i in range(n1,n2+1):
        for j in range(1,11):
            pr=i*j
            str3=str(i)+str1+str(j)+str2+str(pr)
            l1.append(str3)
        l1.append(str4)
    print(l1)
    return l1