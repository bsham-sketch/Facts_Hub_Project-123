from django.urls import path
from . import views
from .views import facts_list, categories_list, facts_by_category

urlpatterns = [
    path('', views.ApiRootView.as_view(), name='api-root'),
    path('categories/', categories_list, name='categories-list'),
    path('facts/', facts_list, name='facts-list'),
    path('facts/category/<str:category>/', facts_by_category, name='facts-by-category'),
    path('facts/<int:fact_id>/', views.FactDetailView.as_view(), name='fact-detail'),
    path('facts/add/', views.AddFactView.as_view(), name='fact-add'),
]
