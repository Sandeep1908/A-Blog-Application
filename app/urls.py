from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[ 
    path('',views.home,name='home'),
    path('login/',views.login_view,name='login'),
    path('signup/',views.register_view,name='signup'),
    path('logout/',views.logout_view,name='logout')
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)