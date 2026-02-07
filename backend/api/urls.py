from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoriesView.as_view(), name='categories'),
    path('facts/', views.FactsView.as_view(), name='facts'),
    path('facts/<int:fact_id>/', views.FactDetailView.as_view(), name='fact-detail'),
    path('facts/add/', views.FactDetailView.as_view(), name='fact-add'),
]
