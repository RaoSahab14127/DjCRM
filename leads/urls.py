from django.urls import path
from .views import LeadListView, LeadCreateView, LeadDeleteView, LeadUpdateView, LeadDetailView
urlpatterns = [
    path("", LeadListView.as_view(),name='getlead'),
    path("<int:pk>/", LeadDetailView.as_view(),name='detaillead'),
    path('update/<int:pk>/',LeadUpdateView.as_view(),name="updatelead" ),
    path('create/',LeadCreateView.as_view(),name="createlead" ),
    path('delete/<int:pk>/',LeadDeleteView.as_view(),name="deleteform" ),
]