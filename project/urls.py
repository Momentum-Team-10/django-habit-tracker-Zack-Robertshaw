"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from core import views
from api import views as api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('', views.home, name='home'),
    # path('tracker/<int:pk>/add_record/', views.add_record, name='add_record'),
    path('tracker/<int:pk>/habit_records/', views.habit_records, name='habit_records'),
    path('tracker/<int:pk>/delete_habit/', views.delete_habit, name='delete_habit'),
    path('tracker/<int:pk>/delete_record/', views.delete_record, name='delete_record'),
    # path('api', api_views.api_root.as_view(), name="api_home"),
    path('api/', api_views.api_root),
    path('api-auth/', include('rest_framework.urls')),
    path('api/users/', api_views.UserViewSet.as_view(), name="users_list"),
    path('api/habits/', api_views.HabitListView.as_view(), name="habits_list"),
    path('api/habits/<int:pk>/', api_views.HabitDetailView.as_view(), name="habits_detail"),
    path('api/records/', api_views.RecordListView.as_view(), name="records_list"),
    path('api/records/<int:pk>/', api_views.RecordDetailView.as_view(), name="records_detail"),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),


]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
