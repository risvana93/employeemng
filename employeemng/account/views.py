from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib import messages
from .forms import RegForm,DeptForm,ManagerForm
from .models import RegModel,DeptModel,Manager

# Create your views here.


class RegView(View):
    def get(self,request):
        form=RegForm()
        return render(request,"reg.html",{'form':form})
    def post(self,request):
        form_data=RegForm(request.POST)
        if form_data.is_valid():
            print(form_data.cleaned_data)
            name=form_data.cleaned_data.get('name')
            age=form_data.cleaned_data.get('age')
            em=form_data.cleaned_data.get('email')
            ex=form_data.cleaned_data.get('experience')
            RegModel.objects.create(name=name,age=age,email=em,experience=ex)
            messages.success(request,"Registration completed successfully")
            return redirect('reg') 
        else:
            messages.error(request,"Registration failed")
            return render(request,"reg.html",{'form':form_data})
              


class Home(View):
    def get(self,request):
        return render(request,"home.html") 



class ViewEmp(View):
    def get(self,req):
        emp=RegModel.objects.all()
        return render(req,"viewemp.html",{'data':emp})                    



class DelEmp(View):
    def get(self,req,*args,**kwargs):
        id=kwargs.get("id")
        eob=RegModel.objects.get(eid=id)
        eob.delete()
        return redirect('vemp')        



class EditEmp(View):
    def get(self,req,*args,**kwargs):
        id=kwargs.get('id')
        emp=RegModel.objects.get(eid=id)
        form=RegForm(initial={'name':emp.name,'age':emp.age,'email':emp.email,'experienece':emp.experience})
        return render(req,"editemp.html",{'form':form})
    def post(self,req,*args,**kwargs):
        form=RegForm(req.POST)
        id=kwargs.get("id")
        if form.is_valid():
            name=form.cleaned_data.get('name') 
            age=form.cleaned_data.get('age') 
            em=form.cleaned_data.get('email') 
            ex=form.cleaned_data.get('experience')  
            RegModel.objects.filter(eid=id).update(name=name,age=age,email=em,experience=ex) 
            return redirect('vemp')
        else:
            return redirect('editemp')             


class DeptView(View):
    def get(self,req,*args,**kwargs):
        form=DeptForm()
        return render(req,"dept.html",{'form':form})
    def post(self,req,*args,**kwargs):
        form_data=DeptForm(req.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(req,"Department Added")
            return redirect('h')
        else:
            messages.error(req,"Department Adding failed")
            return redirect('dept')

class DepRet(View):
    def get(self,req):
        data=DeptModel.objects.all()
        return render(req,"viewdept.html",{'data':data})
class DeptDelete(View):
    def get(self,req,*args,**kwargs):
        dept=DeptModel.objects.all()
        did=kwargs.get('did')
        dept=DeptModel.objects.get(id=did)
        dept.delete()
        return redirect('deptview')


class EditDept(View):
    def get(self,req,*args,**kwargs):
        d_id=kwargs.get('did')
        dept=DeptModel.objects.get(id=d_id)
        form=DeptForm(instance=dept)
        return render(req,"editdept.html",{'form':form})  
    def post(self,req,*args,**kwargs):
        d_id=kwargs.get('did')
        dept=DeptModel.objects.get(id=d_id)
        form_data=DeptForm(req.POST,instance=dept)  
        if form_data.is_valid():
            form_data.save()
            return redirect('deptview') 
        else:
            return redirect('editdept')  



class ManagerReg(View):
    def get(self,req):
        form=ManagerForm()
        return render(req,"addman.html",{'form':form})
    def post(self,req):
        form_data=ManagerForm(req.POST,files=req.FILES)
        if form_data.is_valid():
            form_data.save()
            return redirect('h')
        else:
            return redirect('addman') 


class ManagerList(View):
    def get(self,req):
        data=Manager.objects.all()
        return render(req,"viewmanager.html",{"data":data})               
class DeleteMan(View):
    def get(self,req,*args,**kwargs):
        manag=Manager.objects.all()
        mid=kwargs.get('mid')
        manag=Manager.objects.get(id=mid)
        manag.delete()
        return redirect('viewman')

class EditMan(View):
    def get(self,req,*args,**kwargs):
        m_id=kwargs.get('mid')
        manag=Manager.objects.get(id=m_id)
        form=ManagerForm(instance=manag)
        return render(req,"editmanger.html",{'form':form})
    def post(self,req,*args,**kwargs):
        m_id=kwargs.get('mid')
        manag=Manager.objects.get(id=m_id)
        form_data=ManagerForm(req.POST,files=req.FILES,instance=manag)  
        if form_data.is_valid():
            form_data.save()
            return redirect('viewman') 
        else:
            return redirect('edtman')  
    
        
class Index(View):
    def get(self,req) :
        return render(req,"index.html")      
