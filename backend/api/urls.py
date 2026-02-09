from django.urls import path
from . import views
from .views import facts_list

urlpatterns = [
    path('', views.ApiRootView.as_view(), name='api-root'),
    path('categories/', views.CategoriesView.as_view(), name='categories'),
    path('facts/', facts_list, name='facts-list'),
    path('facts/<int:fact_id>/', views.FactDetailView.as_view(), name='fact-detail'),
    path('facts/add/', views.AddFactView.as_view(), name='fact-add'),
]
