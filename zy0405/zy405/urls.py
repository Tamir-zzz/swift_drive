from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from . import views
# from zy0405.zy405.views import Home

app_name = 'zy405'

urlpatterns = [
    # path(r'a/', views.aaa, name="aaa"),

    # path(r'a/', views.a , name="login"),
    path('login/', views.login , name="login"),
    path('logincheck/', views.loginCheck, name='logincheck'),
    path('loginout/', views.loginout, name='loginout'),
    
    path('index/', views.index, name='index'),
    
    path('signup/', views.sign_up , name="signup"),
    path('signupaction/', views.sign_up_action, name='signupaction'),
    
    path('chagepwd/', views.change_password , name="changepwd"),
    path('chagepwdaction/', views.change_password_action , name="changepwdaction"),


    path('getcon/', views.get_counters_web, name='getcon'),
    path('addcon/', views.add_counter, name='addcon'),
    path('delcon/<conname>', views.del_counter, name='delcon'),

    path('getobjs/<conname>/', views.get_objects_web, name='getobjs'),

    path('getallobjs/', views.get_all_objects_web, name='getallobjs'),
    path('getsearchobjs/', views.get_search_objects, name='getsearchobjs'),
    path('getimgobjs/', views.get_img_objects, name='getimgobjs'),
    path('getvideoobjs/', views.get_video_objects, name='getvideoobjs'),
    path('getdocobjs/', views.get_doc_objects, name='getdocobjs'),
    path('getotherobjs/', views.get_other_objects, name='getotherobjs'),
    path('getrecentlyobjs/', views.get_recently_objects, name='getrecentlyobjs'),

    path('getobj/<conname>/<objname>/', views.get_object, name='getobj'),

    path('addobj/<conname>/', views.add_object, name='addobj'),
    path('copyobj/<conname>/', views.copy_object_action, name='copyobj'),
    path('getshareobj/<conname>/', views.get_share_object_action, name='getshareobj'),
    path('delobj/<conname>/<objname>/', views.del_object, name='delobj'),
    path('downobj/<conname>/<objname>/', views.down_object, name='downobj'),
    

]
