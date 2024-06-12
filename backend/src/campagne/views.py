from django.http import JsonResponse
from .models import Invitation
from rest_framework.response import Response
from .serializers import InvitationSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
import json
from uuid import UUID
from .serializers import CompetenceTestResultSerializer, CampagneSerializer
from rest_framework import status
from .models import CompetenceTestResult
from competence_tests.models import CompetenceDimension
from job_profiles.models import JobProfile
from job_profiles.serializers import JobProfileSerializer
from .models import ThreatSituationScore, Invitation, CompetenceTestResult, Campagne
from threats.models import ThreatVector, ThreatSituation
from competence_tests.models import CompetenceTest
import base64
import ast
import os
from collections import defaultdict
from cryptography.fernet import Fernet
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML
from django.db import transaction
from trainings.models import Training
from users.models import UserProfile
from competence_tests.models import CompetenceDimension
from .charts import  *
# Correct import path for CSRF decorators
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views import decorators
from django.db.models import Count
from django.core.exceptions import ImproperlyConfigured


def is_valid_fernet_key(key):
    """Check if the key provided is a valid fernet key. A valid Fernet key is 44 URL-safe base64-encoded characters.

    Args:
        key (fernet key): The fernet key that was generated

    Returns:
        fernet key:
    """
    try:
        base64.urlsafe_b64decode(key)
        return len(key) == 44  # Valid Fernet key is 44 URL-safe base64-encoded characters
    except Exception:
        return False

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def generate_key_view(request):
    """Generates a fernet key that is used as security key to encode and decode e-mail adresses stored in the data base

    Returns:
        fernet key:
    """
    key = Fernet.generate_key()
    return Response({'key': key.decode()})

def encrypt_message(email, key):
    """Encrypts the e-mail adresses before stored in the data base.

    Args:
        email (str): The e-mail adress to be encrypted
        key (fernet key): The fernet key that was generated

    Returns:
        The encrypted email
    """
    f = Fernet(key)
    return f.encrypt(email.encode())

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def decrypt_emails_view(request):
    """Decrypts the e-mail adresses when retrieved from the data base.

    Args:
        request (HttpRequest): A Django HttpRequest object containing the HTTP request information.

    Returns:
        JsonResponse: A Django JsonResponse object including the decrpyted e-mails. Returns a success object when the e-mail can be decrypted. Returns an error when the fernet key is invalid or is not provided.

    """
    data = request.data
    key = data.get('key')


    if not key:
        return JsonResponse({'error': 'Encryption key not provided.'}, status=400)
    
    key = key.strip()


    user = request.user
    invitations = Invitation.objects.filter(created_by_id=user)
    serializer = InvitationSerializer(invitations, many=True)
    encrypted_emails = [item['email_encrypted'] for item in serializer.data]
    try:
        # Convert the key from URL-safe base64-encoded string to bytes
        f = Fernet(key)
        decrypted_emails = []
        for email in encrypted_emails:
            # Convert string representation of bytes to actual bytes
            byte_email = ast.literal_eval(email)
            decrypted_email = f.decrypt(byte_email).decode()
            decrypted_emails.append(decrypted_email)

        return JsonResponse({'decrypted_emails': decrypted_emails})
    except Exception as e:
        return JsonResponse({'Invalid security key': str(e)}, status=400)




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_campagne(request):
    """Tries to get an existing campagne object.

    Args:
        request (HttpRequest): A Django HttpRequest object containing the HTTP request information.

    Returns:
        JsonResponse: A Django Response object including the decrpyted e-mails. 
        Returns a success object when the e-mail can be decrypted. Returns an error when the fernet key is invalid or is not provided.
        200: If succesful
        404: If campagne object was not found

    Raises:
        Campagne.DoesNotExist: If campagne object was not found
    """
    user = request.user
    try:
        campagne = Campagne.objects.get(created_by_id=user)
        serializer = CampagneSerializer(campagne)
        return Response(serializer.data, status=200)
    except Campagne.DoesNotExist:
        return Response({'error': 'Campagne not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_campagne(request):
    """
    Creates a new campagne.

    Args:
        request (HttpRequest): A Django HttpRequest object containing the HTTP request information.
        The method expects a boolean 'oneInvitationCode' to be set in request.POST parameters.

    Returns:
         Response: A Django Response object. 
        - Returns a success message and status 200 if the campagne is created successfully.
        - Returns an error message and status 400 if the campagne cannot be created due to invalid input or server errors.
    """
    try:
        data = json.loads(request.body)
        oneInvitationToken = data.get('oneInvitationToken')
        security_display_threshold = data.get('securityDisplayThreshold')
        created_by = request.user
        Campagne.objects.create(created_by=created_by, one_token_mode=oneInvitationToken, security_display_threshold = security_display_threshold)
        return Response({'message': 'Campagne created'}, status=200)
    except Exception as e:
        return Response({'error': str(e)}, status=400)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def remove_security_key(request):
    """
    Removes the usage of a security key to decrypt e-mails stored in the data base.

    Args:
        request (HttpRequest): A Django HttpRequest object containing the HTTP request information.
        The method expects the authenticated user to be set in request.POST parameters.

    Returns:
        Response: A Django Response object. 
        - Returns a success message and status 200 if the campagne is changed successfully.
        - Returns an error message and status 400 if the campagne cannot be created due to invalid input or server errors.
        - Returns an error message and status 404 if the campagne associated to the specified user is not found.

    """
    user = request.user
    try:
        campagne = Campagne.objects.get(created_by=user)
        campagne.security_key_activated = False
        serializer = CampagneSerializer(campagne, data={"security_key_activated": False}, partial=True)


        if serializer.is_valid():

            serializer.save()  # Save the instance
            return Response({'message': 'Campagne changed'}, status=200)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Campagne.DoesNotExist:
        return Response({'error': 'Campagne not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def invalidate_invitation_tokens(request):
    """
    Removes the usage of a security key to decrypt e-mails stored in the data base.

    Args:
        request (HttpRequest): A Django HttpRequest object containing the HTTP request information.
        The method expects the authenticated user to be set in request.POST parameters.

    Returns:
        Response: A Django Response object. 
        - Returns a success message and status 200 if the campagne is changed successfully.
        - Returns an error message and status 400 if the campagne cannot be created due to invalid input or server errors.
        - Returns an error message and status 404 if the campagne associated to the specified user is not found.

    """
    user = request.user
    try:
        invitations = Invitation.objects.filter(created_by_id=user)
        with transaction.atomic():
            for invitation in invitations:
                serializer = InvitationSerializer(invitation, data={'usage_active': False}, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'message': 'Invitations changed'}, status=200)

                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Invitation.DoesNotExist:
        return Response({'error': 'Invitation not found'}, status=status.HTTP_404_NOT_FOUND)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def end_campaign(request):
    """
    End the campaign.

    Args:
        request (HttpRequest): A Django HttpRequest object containing the HTTP request information.
        The method expects the authenticated user to be set in request.POST parameters.

    Returns:
        Response: A Django Response object. 
        - Returns a success message and status 200 if the campagne is changed successfully.
        - Returns an error message and status 400 if the campagne cannot be created due to invalid input or server errors.
        - Returns an error message and status 404 if the campagne associated to the specified user is not found.

    """
    user = request.user
    try:
        data = json.loads(request.body)
        campagne = Campagne.objects.get(created_by_id=user)
        campagne.campaign_ended = True
        aggregate_over_single_profiles = data.get('aggregateOverSingleProfiles')

        serializer = CampagneSerializer(campagne, data={"campaign_ended": True, "aggregate_over_single_profiles": aggregate_over_single_profiles}, partial=True)

        if serializer.is_valid():
            serializer.save()  # Save the instance
            return Response({'message': 'Campagne changed'}, status=200)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Campagne.DoesNotExist:
        return Response({'error': 'Campagne not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_invitations(request):
    """
    Gets all invitation objects associated to a user from the data base.

    Args:
        request (HttpRequest): A Django HttpRequest object containing the HTTP request information.
        The method expects the authenticated user to be set in request.POST parameters.

    Returns:
        Response: A Django Response object. 
        - Returns a success message and status 200 if invitations can be found
        - Returns an error message and status 500 if the invitations cannot be found due to invalid input or server errors.
        - Returns an error message and status 404 if invitations associated to the specified user are not found.
    """
    user = request.user
    try:
        invitations = Invitation.objects.filter(created_by_id=user)
        if invitations.exists():
            serializer = InvitationSerializer(invitations, many=True)
            return Response(serializer.data)
        else:
            # No invitations found for the user
            return Response({'message': 'No invitations found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        # Handle unexpected errors
        return Response({'error': 'An unexpected error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_invitations(request):
    """
    Posts all invitation objects associated to a user and specified in the request.POST.

    Args:
        request (HttpRequest): A Django HttpRequest object containing the HTTP request information.
        The method expects the authenticated user to be set in request.POST parameters.

    Returns:
        Response: A Django Response object. 
        - Returns a success message and status 200 if invitations can be created
        - Returns an error message and status 404 if the associated campagne cannot be found.
    """
    user = request.user
    # First try to get the campagne assicoated to the user
    try:
        campagne = Campagne.objects.get(created_by=user)
        serializer = CampagneSerializer(campagne)
    except Campagne.DoesNotExist:
        return Response({'error': 'Campagne not found'}, status=status.HTTP_404_NOT_FOUND)
    
    security_key_activated = campagne.security_key_activated

    data = json.loads(request.body)
    key = data.get('key')
    emails = data.get('emails', [])
    created_by = request.user
    invitations = []
    # Check if emails list is empty
    # This is the case if the user (campagne organizer) decided to use one invitation code that all participants use
    if not emails:
        # Create a single Invitation object
        invitation = Invitation.objects.create(created_by=created_by, reusable=True, email_encrypted="")
        invitations.append(invitation)
    # This is the case if the user (campagne organizer) decided to use an invitation code each that participants use
    else:
        if security_key_activated:
            encrypted_emails = [encrypt_message(email, key) for email in emails]
        else:
            encrypted_emails = emails

        # Create an Invitation object for each email
        for email in encrypted_emails:

            invitation = Invitation.objects.create(created_by=created_by, reusable=False, email_encrypted=email)
            invitations.append(invitation)
    
    serializer = InvitationSerializer(invitations, many=True)


    return Response({'message': 'Batch upload successful!', 'invitations': serializer.data}, status=200)


@api_view(['GET'])
@permission_classes([AllowAny])
def validate_invitation_token(request, invitation_token):
    """
    Validates the invitation token that participants can use to save the results of a competence test associated with a campagne.

    Args:
        request (HttpRequest): A Django HttpRequest object containing the HTTP request information.
        invitation_token (UUID): The invitation token specified in route URL.

    Returns:
        Response: A Django Response object. 
        - Returns a success message and status 200 if the invitation token is valid
        - Returns an error message and status 400 if the invitation token is invalid or has been used already
    """
     # Check if the token is a valid UUID
    try:
        UUID(invitation_token, version=4)
    except ValueError:
        return Response({'valid': False}, status=400)
    # Fetch the invitation from the database
    try:
        invitation = Invitation.objects.get(token=invitation_token)
        if invitation.is_participated or not invitation.usage_active:
            return Response({'valid': False}, status=400)
        else: 
            return Response({'valid': True})

    except Invitation.DoesNotExist:
        return Response({'valid': False}, status=400)

import logging

logger = logging.getLogger(__name__)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_campagne(request):
    """
    Deletes an existing campagne including all competence_test_results stored in the data base.
    Args:
        request (HttpRequest): A Django HttpRequest object containing the HTTP request information.

    Returns:
        Response: A Django Response object. 
        - Returns a success message and status 200 if the campagne including the dependencies can be deleted.
        - Returns an error message and status 405 if the campagne cannot be removed.
    """
    user = request.user
    if request.method == 'POST':
        with transaction.atomic():
        # Direct deletion for models with a `created_by` field
            Invitation.objects.filter(created_by=user).delete()
            Campagne.objects.filter(created_by=user).delete()
            competence_test_results = CompetenceTestResult.objects.filter(created_by=user)
            # Fetching `ThreatSituationScore` instances related to those `CompetenceTestResult` instances
            threat_situation_score_ids = set()

            # Iterate over each CompetenceTestResult to collect ThreatSituationScore ids
            for ctr in competence_test_results:
                ids = ctr.threat_situation_score.all().values_list('id', flat=True)
                threat_situation_score_ids.update(ids)

            ThreatSituationScore.objects.filter(id__in=threat_situation_score_ids).delete()
            CompetenceTestResult.objects.filter(created_by=user).delete()

        return Response({'status': 'success'}, status=200)

    return Response({'status': 'error'}, status=405)


@api_view(['POST'])
def create_competence_test_result(request):
    """
    Creates a competence test result instance. 

    Args:
        request (HttpRequest): A Django HttpRequest object containing the HTTP request information.
        The method expects the competence test result to be set in request.POST parameters.

    Returns:
        Response: A Django Response object. 
        - Returns a success message and status 200 if the competence test result can be created
        - Returns an error message and status 400 if the competence test result cannot be created
    """
    invitation = Invitation.objects.get(token=request.data['participant'])
    if invitation.reusable:
        invitation.is_participated = False
        invitation.tokenCounter+=1
    else:
        invitation.is_participated = True

    invitation.save()

    # Make a mutable copy of request.data
    data = request.data.copy()

    # Add the created_by field to the data
    data['created_by'] = invitation.created_by.id

    serializer = CompetenceTestResultSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        print(serializer.errors) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_competence_test_results(request, profile_id):
    """
    Gets all competence test results accociated to a user and a job profile. 

    Args:
        request (HttpRequest): A Django HttpRequest object containing the HTTP request information.
        profile_id
        The method expects the competence test result to be set in request.POST parameters.
        The method expects the authenticated user to be set in request.POST parameters.


    Returns:
        Response: A Django Response object. 
        - Returns a success message and status 200 if the competence test result can be created
        - Returns an error message and status 400 if the competence test result cannot be created
    """
    user = request.user
    aggregated_results = defaultdict(lambda: {
            'total_threat_situation_scores': defaultdict(lambda: {'total_scoredPoints': 0, 'threat_vector_name': '', 'threat_vector_description': '', 'ids': []}),
            'number_of_threats': 0,  # This will be calculated based on entries in total_threat_situation_scores
            'total_competence_dimension_scores': defaultdict(lambda: {'total_scoredPoints': 0, 'description': ''})
    })
    if profile_id != 0:
        queryset = CompetenceTestResult.objects.filter(created_by=user, job_profile=profile_id)
        serializer = CompetenceTestResultSerializer(queryset, many=True)
        serialized_data = serializer.data

    # profile_id is 0 --> aggregates competence_test results over all job profiles
    else:
        user_profile = Campagne.objects.get(created_by=user)


        queryset = CompetenceTestResult.objects.filter(created_by=user)
        

        if user_profile.aggregate_over_single_profiles:
            # Annotating each entry with the count of participants for the same job profile
            queryset = queryset.values('job_profile').annotate(participant_count=Count('id'))

            # Filtering to keep only those job profiles with at least 5 participants
            queryset = queryset.filter(participant_count__gte=user_profile.security_display_threshold)
             # Now, get the actual test results matching the job profiles with enough participants
            filtered_job_profiles = queryset.values_list('job_profile', flat=True)
            final_queryset = CompetenceTestResult.objects.filter(job_profile__in=filtered_job_profiles, created_by=user)
            # Now, get the actual test results matching the job profiles with enough participants
            filtered_job_profiles = queryset.values_list('job_profile', flat=True)
            final_queryset = CompetenceTestResult.objects.filter(job_profile__in=filtered_job_profiles, created_by=user)

        else:
            final_queryset = CompetenceTestResult.objects.filter(created_by=user)

        
        

        

           

        # Serializing the data
        serializer = CompetenceTestResultSerializer(final_queryset, many=True)
        serialized_data = serializer.data
            
            

    competence_scores = defaultdict(lambda: {'total_scoredPoints': 0, 'competence_dimension_name': ''})
    threat_competence_scores = defaultdict(lambda: {'competence_dimension_id': 0, 'competence_dimension_name': '', 'total_scoredPoints':0})
    competence_scores_per_threat = defaultdict(lambda: defaultdict(lambda: { 'competence_dimension_name': '', 'total_scoredPoints': 0}))

    for item in serialized_data:
        job_profile_id = profile_id
        job_profile_aggregate = aggregated_results[0]
        job_profile_aggregate['profile_name'] = "Alle"
        job_profile_aggregate['number_of_participants'] = len(serialized_data)

        # Aggregate CompetenceDimensionScore
        for competence_score in item['competence_dimension_score']:
            key = competence_score['competence_dimension']
            competence_dimension = CompetenceDimension.objects.get(pk=key)
            aggregate = job_profile_aggregate['total_competence_dimension_scores'][key]
          
            aggregate['total_scoredPoints'] += competence_score['scoredPoints']
            competence_scores[key]['total_scoredPoints'] += competence_score['scoredPoints']
            competence_scores[key]['competence_dimension_name'] = competence_dimension.dimension_name


            if not aggregate['description']:
                competence_dimension = CompetenceDimension.objects.get(pk=key)
                aggregate['description'] = competence_dimension.dimension_name

        
        # Aggregate ThreatSituationScore
       

        for threat_score in item['threat_situation_score']:
           
            key = threat_score['threat_situation']
            aggregate = job_profile_aggregate['total_threat_situation_scores'][key]
            aggregate['total_scoredPoints'] += threat_score['scoredPoints']

            threat_situation = ThreatSituation.objects.get(pk=threat_score['threat_situation'])
            threat_vector = ThreatVector.objects.get(pk=threat_score['threat_vector'])
            threat_vector_description = threat_vector.threat_vector_description
            threat_event_name= threat_vector.threat_event
            threat_area_name= threat_vector.threat_area
            competence_dimension_score= ThreatSituationScore.objects.get(pk=threat_score['id'])
            related_competence_scores = competence_dimension_score.related_competence_dimension_scores.all()

            # Process and aggregate related competence scores
            competence_scores_info = []

            for competence_score in related_competence_scores:
                
                score_info = {
                    "competence_dimension_id": competence_score.competence_dimension.id,  # Assuming there's a 'name' field
                    "competence_dimension_name": competence_score.competence_dimension.dimension_name,  # Assuming there's a 'name' field
                    "scoredPoints": competence_score.scoredPoints,
                }
                competence_scores_info.append(score_info)
            
            # Iterate over competence_scores_info to aggregate scores
            for score_info in competence_scores_info:
                dim_id = score_info["competence_dimension_id"]

                # Check if the competence dimension already has an entry for this threat situation
                if dim_id not in competence_scores_per_threat[threat_situation.id]:
                    # If not, initialize with the current score and name
                    competence_scores_per_threat[threat_situation.id][dim_id]['competence_dimension_name'] = score_info['competence_dimension_name']
                    competence_scores_per_threat[threat_situation.id][dim_id]['total_scoredPoints'] = score_info['scoredPoints']
                    
                else:
                    # If it does, just update the total scored points
                    competence_scores_per_threat[threat_situation.id][dim_id]['total_scoredPoints'] += score_info['scoredPoints']


                # Check if this competence_dimension_id already has an entry in the dictionary
                if dim_id in threat_competence_scores:
                    # Update existing entry
                    threat_competence_scores[dim_id]['total_scoredPoints'] += score_info["scoredPoints"]
                  
                else:
                    # Create a new entry for this competence_dimension_id
                    threat_competence_scores[dim_id] = {
                        'competence_dimension_id': dim_id, 
                        'competence_dimension_name': score_info["competence_dimension_name"], 
                        'total_scoredPoints': score_info["scoredPoints"]
                    }

   
                aggregate['job_profile'] = str(threat_situation.job_profile)
                aggregate['job_profile_id'] = threat_situation.job_profile.id
                aggregate['threat_vector_name'] = str(threat_event_name) + "/" + str(threat_area_name)
                aggregate['threat_vector_description'] = threat_vector_description
                aggregate['ids'].append(threat_score['id'])
                aggregate['related_competence_dimension_scores'] = competence_scores_per_threat
           
    for ts_id in aggregated_results:
        aggregated_results[ts_id]['number_of_threats'] = len(aggregated_results[ts_id]['total_threat_situation_scores'])

    # Convert defaultdict to regular dict for serialization
    aggregated_results = {k: dict(v) for k, v in aggregated_results.items()}
    for job_profile in aggregated_results.values():
        job_profile['total_competence_dimension_scores'] = dict(job_profile['total_competence_dimension_scores'])
        job_profile['total_threat_situation_scores'] = dict(job_profile['total_threat_situation_scores'])


    # If profile_id is 0, replace detailed scores with just the sum of total_scoredPoints
    if int(profile_id) == 0:
        for ts_id, data in aggregated_results.items():
            total_scoredPoints = sum(score['total_scoredPoints'] for score in data['total_threat_situation_scores'].values())
            # Replace old detailed dict with a new one that only contains the total sum
            aggregated_results[ts_id]['total_threat_situation_scores'] = {'total_scoredPoints': total_scoredPoints}

    return Response(aggregated_results)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_participants_per_profile(request):
    """
    Gets specific information on e.g., number of participants and number of threat situtations to each job profile associated to the competence test results. 

    Args:
        request (HttpRequest): A Django HttpRequest object containing the HTTP request information.
        profile_id
        The method expects the competence test result to be set in request.POST parameters.
        The method expects the authenticated user to be set in request.POST parameters.


    Returns:
        Response: A Django Response object. 
        - Returns a success message and status 200 if the job profiles can be fetched
    """
    job_profiles = JobProfile.objects.all()

    # Preparing a dictionary to hold the counts
    job_profile_threat_counts = {}

    for job_profile in job_profiles:
        # Get the CompetenceTest for the JobProfile
        competence_test = CompetenceTest.objects.filter(job_profile=job_profile).first()
        
        if competence_test:
            # Get ThreatVectors associated with this CompetenceTest
            threat_situations= competence_test.threat_situations.all()
            
            # Count ThreatSituations that are linked to the relevant ThreatVectors and the specific JobProfile
            threat_situations_count = len(threat_situations)

            
            job_profile_threat_counts[job_profile.id] = threat_situations_count

    
    job_profiles_queryset = JobProfile.objects.all()
    serializer_context = {'threat_counts': job_profile_threat_counts}  # Pass the counts here
    serializer = JobProfileSerializer(job_profiles_queryset, many=True, context=serializer_context)
    serialized_data = serializer.data
    
    user = request.user

    user_profile = Campagne.objects.get(created_by=user)



    job_profile_dict = {}  # Dictionary to store data keyed by profile ID
    

    participant_count_secure = 0
    num_job_profiles_secure = 0
    index = 1


    for profile in serialized_data:

                
        queryset = CompetenceTestResult.objects.filter(created_by=user, job_profile=profile["id"])
        competence_serializer = CompetenceTestResultSerializer(queryset, many=True)
        num_participants = len(competence_serializer.data)

        id = profile['id']
        job_profile_dict[index] = {
            "job_profile_id": id,
            "job_profile_name": profile['job_name'],
            "job_profile_description": profile['job_description'],
             "job_profile_tasks": profile['job_tasks'],
            "number_of_participants": num_participants,
            'number_of_threat_situations': profile['threat_count']
        }
        # Add the participant count to the list if it's greater than 4
        if num_participants >= user_profile.security_display_threshold:
            participant_count_secure += num_participants
            num_job_profiles_secure+=1
        index+=1

    index = 0
    id =0
    queryset = CompetenceTestResult.objects.filter(created_by=user)
    competence_serializer = CompetenceTestResultSerializer(queryset, many=True)
    #if num_job_profiles_secure >= user_profile.security_display_profile:
    if not user_profile.aggregate_over_single_profiles:
        job_profile_dict[index] = {
            "job_profile_id": id,
            "job_profile_name": "Alle",
            "number_of_participants": len(competence_serializer.data)
        }
    elif len(competence_serializer.data) >= user_profile.security_display_threshold and user_profile.aggregate_over_single_profiles:
        job_profile_dict[index] = {
            "job_profile_id": id,
            "job_profile_name": "Alle",
            "number_of_participants": len(competence_serializer.data)
        }


    return Response(job_profile_dict)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def generate_management_report(request):
    """
    Generates a management report that summarizes the campagne. 

    Args:
        request (HttpRequest): A Django HttpRequest object containing the HTTP request information.
        The method expects the authenticated user to be set in request.POST parameters.


    Returns:
        Response: A Django Response object. 
        - Returns a success message and status 200 including the PDF blob object.
    """
  

    invitations = get_invitations(request._request)
    trainings = Training.objects.order_by('training_name')
    competence_dimensions = list(CompetenceDimension.objects.all())

    user = request.user
    user_profile = Campagne.objects.get(created_by=user)



    # content over all participants
    job_profiles = get_participants_per_profile(request._request)




    df = pd.DataFrame.from_dict(job_profiles.data, orient='index')

    
    # Filter out entries with 'Alle' and zero participants
    if user_profile.aggregate_over_single_profiles:
        df_filtered = df[(df['number_of_participants'] >= user_profile.security_display_threshold)]
    else:
        df_filtered = df[(df['number_of_participants'] >0)]
        df_filtered =  df[df['job_profile_id'] == 0]

    total_number_of_partcipants = df_filtered.iloc[0]['number_of_participants']
    job_profile_with_data = len(df[(df['number_of_participants'] > 0)])
    df_filtered['sort_helper'] = (df_filtered['job_profile_id'] == 0).astype(int)
    df_filtered = df_filtered.sort_values(by='sort_helper', ascending=False)
    df_filtered.drop(columns='sort_helper', inplace=True)


    threat_charts = []
    competence_bar_charts = []
    competence_bar_charts_per_threat = []
    job_profile_names = []

    # Loop through each row in df_filtered using .iterrows()
    for index, row  in df_filtered.iterrows():
        threat_chart_per_profile = []

        selected_profile = row['job_profile_id']  
        job_profile_names.append({'name':row['job_profile_name'], 'description':row['job_profile_description'], 'tasks':row['job_profile_tasks'], 'participants':row['number_of_participants'] })
        competence_test_results = get_competence_test_results(request._request, selected_profile)
        df_competence_test_results = pd.DataFrame.from_dict(competence_test_results.data, orient='index')


        # Generate charts
        threat_chart = generate_threat_chart(competence_test_results.data, job_profiles.data, selected_profile)
        threat_charts.append(threat_chart)
        competence_bar_chart = generate_competence_bar_chart(competence_test_results.data, job_profiles.data, selected_profile, user_profile.security_display_threshold, user_profile.aggregate_over_single_profiles)
        competence_bar_charts.append(competence_bar_chart)
        
        if selected_profile != 0:

            for _, row in df_competence_test_results.iterrows():
                for threat in row['total_threat_situation_scores'].values():

                    threat['score'] = round((threat['total_scoredPoints'] /
                        (df_competence_test_results.iloc[0]['number_of_participants'] *
                        14)) * 100)
                    if threat['score'] >=66:
                        threat['result'] = 'good'
                    elif threat['score'] <=33:
                        threat['result'] = 'bad'
                    else: 
                        threat['result'] = 'medium'


                    values = list(threat['related_competence_dimension_scores'].values())

                    if values:  # Check if the list of values is not empty
                        first_value = values[0]  # Access the first value
                    
                    if selected_profile != 0:
                        competence_bar_chart_per_threat = generate_competence_bar_chart_per_threat(first_value, competence_test_results.data)
                        threat_chart_per_profile.append({'chart': competence_bar_chart_per_threat, 'threat': threat})

        competence_bar_charts_per_threat.append(threat_chart_per_profile)                    
    profile_distribution = generate_job_profile_distribution(job_profiles.data)

    filtered_profiles = [profile for profile in job_profile_names if profile['name'] != 'Alle']




    context = {
        'total_number_of_partcipants': total_number_of_partcipants,
        'total_number_of_trainings':len(trainings),
        'total_invited_employees':len(invitations.data),
        'job_profiles_with_data':job_profile_with_data-1,
        'profile_distribution': profile_distribution, 
        'threat_charts':threat_charts,
        'competence_bar_charts':competence_bar_charts,
        'job_profiles':filtered_profiles,
        'competence_dimensions':competence_dimensions,
        'zipped_data': list(zip(job_profile_names, threat_charts, competence_bar_charts, competence_bar_charts_per_threat))[1:]

    }
    html_string = render_to_string('management_report.html', context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="management_report.pdf"'

    # Anpassen an IP-Adresse der VM oder des virtuellen Webservers
    HTML(string=html_string, base_url=get_env_variable('API_URL')).write_pdf(response)
    return response


def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = f"Set the {var_name} environment variable"
        raise ImproperlyConfigured(error_msg)
