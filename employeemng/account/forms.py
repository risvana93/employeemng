from django import forms
from .models import DeptModel,Manager

class RegForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter your name","class":"form-control"}))
    age=forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"Enter your age","class":"form-control"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Enter your mail","class":"form-control"}))
    experience=forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"Enter your experience","class":"form-control"}))
    def clean(self):
          cleaned_data=super().clean()
          ex=cleaned_data.get('experience')
          if ex<0:
            msg="experience invalid"
            self.add_error('experience',msg)

# class DeptForm(forms.Form):
#   dept_name=forms.CharField(label="Department Name")
#   description=forms.CharField(label="Department discription")
#   office_no=forms.IntegerField(label="Office Number")

class DeptForm(forms.ModelForm):
  class Meta:
    model=DeptModel
    fields="__all__"
    widgets={
      'department_name':forms.TextInput(attrs={"placeholder":"Enter department name","class":"form-control"}),
      'description':forms.TextInput(attrs={"placeholder":"Enter department description","class":"form-control"}),
      'office_number':forms.NumberInput(attrs={"placeholder":"Enter department room no","class":"form-control"})
    }

class ManagerForm(forms.ModelForm):
  class Meta:
    model=Manager
    fields="__all__" 
    widgets={
      'first_name':forms.TextInput(attrs={"placeholder":"Enter first name","class":"form-control"}),
      'last_name':forms.TextInput(attrs={"placeholder":"Enter last name","class":"form-control"}),
      'email':forms.EmailInput(attrs={"placeholder":"Enter email","class":"form-control"}),
      'phone':forms.NumberInput(attrs={"placeholder":"Enter phoneno","class":"form-control"}),
      'pic':forms.FileInput(attrs={"placeholder":"select profilepic","class":"form-control"})
   }
