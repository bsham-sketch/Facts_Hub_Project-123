from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiRootView.as_view(), name='api-root'),
    path('categories/', views.CategoriesView.as_view(), name='categories'),
    path('facts/', views.FactsView.as_view(), name='facts'),
    path('facts/<int:fact_id>/', views.FactDetailView.as_view(), name='fact-detail'),
    path('facts/add/', views.AddFactView.as_view(), name='fact-add'),
]
