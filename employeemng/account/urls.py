from django.urls import path
# from .views import RegView,ViewEmp,DelEmp,EditEmp,DeptView,DepRet,DeptDelete,EditDept\
from .views import *


urlpatterns=[
    path('ind/',Index.as_view(),name='ind'),
    path('reg/',RegView.as_view(),name='reg'),
    path('vemp/',ViewEmp.as_view(),name='vemp'),
    path('delemp/<int:id>',DelEmp.as_view(),name='delemp'),
    path('editemp/<int:id>',EditEmp.as_view(),name='editemp'),
    path('dept/',DeptView.as_view(),name='dept'),
    path('deptview/',DepRet.as_view(),name='deptview'),
    path('deptdlt/<int:did>',DeptDelete.as_view(),name='deptdlt'),
    path('editdept/<int:did>',EditDept.as_view(),name='editdept'),
    path('addman/',ManagerReg.as_view(),name="addman"),
    path('viewman/',ManagerList.as_view(),name="viewman"),
    path('dltman/<int:mid>',DeleteMan.as_view(),name='dltman'),
    path('edtman/<int:mid>',EditMan.as_view(),name='edtman')
]