from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_proposal, name='create_proposal'),
    path('edit/<int:proposal_id>/', views.edit_proposal, name='edit_proposal'),
    path('manage/', views.manage_proposals, name='manage_proposals'),
]
