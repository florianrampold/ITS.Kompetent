from django.urls import path
from . import views

urlpatterns = [
    path('post_invitations/', views.create_invitations, name='create_invitations'),
    path('get_invitations/', views.get_invitations, name='get_invitations'),
   # path('modify_invitations/', views.modify_all_invitations, name='modify_all_invitations'),
   # path('invitations/<str:invitationToken>/', views.modify_invitation, name='modify_invitation'),
    path('invitation_token/<str:invitation_token>/', views.validate_invitation_token, name='invitation_token'),
    path('competence_test_result/', views.create_competence_test_result, name='create_competence_test_result'),
    path('competence_test_results/<int:profile_id>/', views.get_competence_test_results, name='create_competence_test_results'),
    path('participants_per_profile/', views.get_participants_per_profile, name='get_participants_per_profile'),
    path('delete_campagne/', views.delete_campagne),
    path('create_campagne/', views.create_campagne),
    path('get_campagne/', views.get_campagne),
    path('remove_security_key/', views.remove_security_key),
    path('generate_key/', views.generate_key_view),
    path('decrypt_emails/', views.decrypt_emails_view),
   # path('generate_invitation_email/', views.generate_invitation_email, name='generate_invitation_email'),
    path('generate_management_report/', views.generate_management_report, name='generate_management_report'),
]
