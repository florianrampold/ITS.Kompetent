from rest_framework import serializers
from .models import CompetenceDimensionScorePerThreat, Invitation
from rest_framework import serializers
from .models import ThreatSituationScore, CompetenceDimensionScore, CompetenceTestResult, Campagne
from django.db import transaction

class InvitationSerializer(serializers.ModelSerializer):
    """
    Serializer for Invitation model.

    Serializes Invitation objects.

    """
    class Meta:
        model = Invitation
        fields = '__all__'

class CampagneSerializer(serializers.ModelSerializer):
    """
    Serializer for Campagne model.

    Serializes Campagne objects.

    """
    class Meta:
        model = Campagne
        fields = '__all__'
class CompetenceDimensionScorePerThreatSerializer(serializers.ModelSerializer):
    """
    Serializer for CompetenceDimensionScorePerThreat model.

    Serializes CompetenceDimensionScorePerThreat objects.

    """
    class Meta:
        model = CompetenceDimensionScorePerThreat
        fields = '__all__'



class ThreatSituationScoreSerializer(serializers.ModelSerializer):
    """
    Serializer for ThreatSituationScore model.

    Serializes ThreatSituationScore objects.

    """
    related_competence_dimension_scores = CompetenceDimensionScorePerThreatSerializer(many=True, required=False)

    class Meta:
        model = ThreatSituationScore
        fields = '__all__'

    def create(self, validated_data):
        """
        Calculates each aggregated threat situation score and also builds an array including the related scores for each threat on each competence dimension.

        Args:
            validated_data (HttpRequest): A Django HttpRequest object containing the HTTP request information.
           

        Returns:
            Response: A Django Response object. 
            - Returns the threat situation score
        """
        with transaction.atomic():
            # Separate 'competence_dimension_score' data from other fields
            competence_dimension_scores_data = validated_data.pop('related_competence_dimension_scores', [])
            
            
            # Create the ThreatSituationScore instance without 'competence_dimension_score'
            threat_situation_score = ThreatSituationScore.objects.create(**validated_data)
            
            # Now handle the 'competence_dimension_score' ManyToManyField
            for score_data in competence_dimension_scores_data:
                # 'score_data' is an OrderedDict; ensure 'competence_dimension' is handled correctly
                competence_dimension = score_data.get('competence_dimension')
                scored_points = score_data.get('scoredPoints')
                
                # Create or retrieve CompetenceDimensionScorePerThreat instance
                # Assuming CompetenceDimensionScorePerThreat model has fields 'scoredPoints' and 'competence_dimension'
                competence_score_instance, created = CompetenceDimensionScorePerThreat.objects.get_or_create(
                    competence_dimension=competence_dimension,
                    defaults={'scoredPoints': scored_points}
                )
                
                # Associate the CompetenceDimensionScorePerThreat instance with the ThreatSituationScore instance
                threat_situation_score.related_competence_dimension_scores.add(competence_score_instance)

        return threat_situation_score


class CompetenceDimensionScoreSerializer(serializers.ModelSerializer):
    """
    Serializer for CompetenceDimensionScore model.

    Serializes CompetenceDimensionScore objects.

    """
    class Meta:
        model = CompetenceDimensionScore
        fields = '__all__'

class CompetenceTestResultSerializer(serializers.ModelSerializer):
    """
    Serializer for CompetenceTestResult model.

    Serializes CompetenceTestResult objects.

    """

    threat_situation_score = ThreatSituationScoreSerializer(many=True)
    competence_dimension_score = CompetenceDimensionScoreSerializer(many=True)

    class Meta:
        model = CompetenceTestResult
        fields = '__all__'

    def create(self, validated_data):
        threat_situation_score_data = validated_data.pop('threat_situation_score')
        print(threat_situation_score_data, " scored data")
        competence_dimension_score_data = validated_data.pop('competence_dimension_score')

        competence_test_result = CompetenceTestResult.objects.create(**validated_data)

        for threat_data in threat_situation_score_data:
            # Pop 'competence_dimension_score' data to handle separately
            cds_data = threat_data.pop('related_competence_dimension_scores', [])
            print(cds_data, "CDSSSS")
            # Convert model instances to their PKs for serialization
            threat_data['threat_situation'] = threat_data['threat_situation'].pk
            threat_data['threat_vector'] = threat_data['threat_vector'].pk
            
            # Create ThreatSituationScore instance
            threat_score_serializer = ThreatSituationScoreSerializer(data=threat_data)
           # print("before looop")
            if not threat_score_serializer.is_valid():
                print(threat_score_serializer.errors)
            else:
                threat_score = threat_score_serializer.save()
                print(threat_score, "score")

               

                # For each CompetenceDimensionScorePerThreat data, create and associate with ThreatSituationScore
                for cds in cds_data:
                    cds['competence_dimension'] = cds['competence_dimension'].pk
                    cds_serializer = CompetenceDimensionScorePerThreatSerializer(data=cds)
                    if not cds_serializer.is_valid():
                        print(cds_serializer.errors)
                    else:
                        cds_instance = cds_serializer.save()
                        print(cds_instance, " ins")
                        threat_score.related_competence_dimension_scores.add(cds_instance)
           


                competence_test_result.threat_situation_score.add(threat_score)

        for competence_data in competence_dimension_score_data:
            competence_score = CompetenceDimensionScore.objects.create(**competence_data)
            competence_test_result.competence_dimension_score.add(competence_score)
        
      #  print(competence_test_result)

        return competence_test_result



    

            




