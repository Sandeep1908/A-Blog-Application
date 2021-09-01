from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[ 
    path('',views.home,name='home'),
    path('login/',views.login_view,name='login'),
    path('signup/',views.register_view,name='signup'),
    path('logout/',views.logout_view,name='logout'),
    path('see_detail/<slug>/',views.see_blog,name='see_blog'),
    path('addpost/',views.addpost,name='addpost'),
    path('edit/',views.edit,name='edit'),
    path('update/<slug>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)