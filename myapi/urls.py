from api.views import courselist, courselistpk
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/course', courselist ),
    path('api/course/<int:pk>', courselistpk ),
    
]
