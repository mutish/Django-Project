from django.contrib import admin
from django.urls import path
from catalogue import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cat', views.cat),
    path('show', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('destroy/<int:id>', views.destroy),
]
