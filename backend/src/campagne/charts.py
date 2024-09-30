
from base64 import b64encode
import plotly.io as pio
import plotly.express as px
import pandas as pd


TOTAL_POSSIBLE_POINTS_PER_THREAT = 14  
MAX_POINTS_PER_COMPETENCE_DIMENSION = 2 

custom_colors = ["#1f2c5a", "#f06666", "#683d87", "#303e7a", "#EB5757"]

def generate_job_profile_distribution(job_profiles):
    """Creates a pie chart for the Job Profile Distrubution of all participants.

    Args:
        job_profiles (dict): A python dictionary inluding the job profiles

    Returns:
        str: An HTML string representing the generated pie chart image.
    """
    # Convert the dictionary to a pandas DataFrame
    df = pd.DataFrame.from_dict(job_profiles, orient='index')
    
    # Filter out entries with 'Alle' and zero participants
    df_filtered = df[(df['job_profile_name'] != 'Alle') & (df['number_of_participants'] > 0)].copy()

    if df_filtered.empty:
        return '<p>No data available for the selected criteria.</p>'

    df_filtered['percentage_number_of_participants'] = (df_filtered['number_of_participants'] / df_filtered['number_of_participants'].sum()) * 100

    # Append percentage to the Category label
    df_filtered['job_profile_name'] = df_filtered.apply(lambda row: f"{row['job_profile_name']} ({row['percentage_number_of_participants']:.2f}%)", axis=1)





    # Create the pie chart using Plotly Express
    fig = px.pie(df_filtered, names='job_profile_name', values='percentage_number_of_participants', hole=0.3,
                 color='job_profile_name', color_discrete_sequence=custom_colors )

    fig.update_layout(
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.25,
        xanchor="center",
        x=0.5,
        font=dict(
            family="Georgia, serif",  
            size=16,  
            color="black" 
        )
    ),
     font=dict(
        family="Georgia, serif",  
        size=16,  
    ),
  
    
    title_font=dict(
        size=20,  
        color="black"  
        )
    )
    # Remove the default text
    fig.update_traces(textinfo='none')
     # Convert the figure to SVG
    svg = pio.to_image(fig, format='svg')

    # Encode the SVG data to base64
    base64_string = b64encode(svg).decode()
    img_html = f"""
    <img class="centered-image" src="data:image/svg+xml;base64,{base64_string}" alt="Chart"/>
    </div>
    """

    return img_html



def generate_threat_chart(competence_test_results, job_profiles, selected_profile):
    """Creates a pie chart showing the percentage of scored points in the competence test for a specific security threat or over all security threats.

    Args:
        competence_test_results (dict): A python dictionary including the competence_test_results
        job_profiles (dict): A python dictionary inluding the job profiles
        selected_profile (int): An integer holding the current job profile ID


    Returns:
        str: An HTML string representing the generated bar chart image.
    """
    df_competence_test_results = pd.DataFrame.from_dict(competence_test_results, orient='index')
    df_job_profiles = pd.DataFrame.from_dict(job_profiles, orient='index')

    # Calculate total_points from competence test results
    if selected_profile != 0:
        number_of_threats = df_competence_test_results['total_threat_situation_scores'].apply(len).sum()
        total_points = df_competence_test_results['total_threat_situation_scores'].apply(
        lambda row: sum(item['total_scoredPoints'] for item in row.values())).sum()
    else:
        number_of_threats = df_competence_test_results['number_of_threats']
        total_points = df_competence_test_results['total_threat_situation_scores'][0]['total_scoredPoints']


    # If 0 job_profile = Alle
    if selected_profile != 0:
        max_points = (
            df_competence_test_results.iloc[0]['number_of_participants'] *
            (TOTAL_POSSIBLE_POINTS_PER_THREAT * number_of_threats)
        )
    else:
        max_points = 0
        for index, row in df_job_profiles.iterrows():
            if row['job_profile_id'] != 0:
                max_points += (
                    row['number_of_participants'] *
                    TOTAL_POSSIBLE_POINTS_PER_THREAT *
                    row['number_of_threat_situations']
                )

    names = ["Korrekt beantwortet", "Falsch beantwortet"]


    data = {
        'threat_data': [total_points, max_points - total_points],
        'threat_names': names
    }
    df_new_rows = pd.DataFrame(data)

    df_new_rows['Percentage'] = (df_new_rows['threat_data'] / max_points) * 100

    df_new_rows['threat_names'] =  df_new_rows.apply(lambda row: f"{row['threat_names']} ({row['Percentage']:.2f}%)", axis=1)

    fig = px.pie(df_new_rows, names='threat_names', values='Percentage', hole=0.3,
                 color=["Korrekt beantwortet", "Falsch beantwortet"], color_discrete_sequence=custom_colors)

    fig.update_layout(

    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.25,
        xanchor="center",
        x=0.5,
        font=dict(
            size=16,  
            color="black" 
        )
    ),
    font=dict(
        family="Georgia, serif",
        size=16,
    ),
 
    
    title_font=dict(
        size=20, 
        color="black" 
        )
    )
    fig.update_traces(
    textinfo='none',
   
   
    )


    svg = pio.to_image(fig, format='svg')

    base64_string = b64encode(svg).decode()

    img_html = f"""
    <img class="centered-image" src="data:image/svg+xml;base64,{base64_string}" alt="Chart"/>
    </div>
    """

    return img_html
    
def generate_competence_bar_chart(competence_test_results, job_profiles, selected_profile_id, security_display_threshold, aggregate_over_single_profiles):
    """Creates a bar chart showing the percentage of scored points per competence dimension over all security threats related to a job profile.

    Args:
        competence_test_results (dict): A python dictionary including the competence_test_results
        job_profiles (dict): A python dictionary inluding the job profiles
        selected_profile_id (int): An integer holding the current job profile ID


    Returns:
        str: An HTML string representing the generated bar chart image.
    """
    # Convert dictionaries to pandas DataFrames
    df_competence_test_results = pd.DataFrame.from_dict(competence_test_results, orient='index')
    df_job_profiles = pd.DataFrame.from_dict(job_profiles, orient='index')
    if aggregate_over_single_profiles:
        df_job_profiles = df_job_profiles[(df_job_profiles['number_of_participants'] >= security_display_threshold)]

    

    NUMBER_OF_THREATS = df_competence_test_results['number_of_threats'].iloc[0]


    competenceScoreData = []
    competenceDimensionData = []
    maxPoints = 0

    # Calculate maxPoints based on selected profile
    if selected_profile_id == 0:
        for _, row in df_job_profiles.iterrows():
            if row['job_profile_id'] != 0:
                maxPoints += (
                    row['number_of_participants'] * MAX_POINTS_PER_COMPETENCE_DIMENSION * row['number_of_threat_situations']
                )

    # Loop through competence test results to calculate scores
    for _, row in df_competence_test_results.iterrows():
        for element in row['total_competence_dimension_scores'].values():
            if selected_profile_id != 0:
                participants = df_competence_test_results.iloc[0]['number_of_participants']
                score = round(
                    (element['total_scoredPoints'] /
                     (NUMBER_OF_THREATS * MAX_POINTS_PER_COMPETENCE_DIMENSION * participants)) * 100
                )
            else:
                score = round((element['total_scoredPoints'] / maxPoints) * 100) if maxPoints else 0
            competenceScoreData.append(score)
            competenceDimensionData.append(element['description'])
    
      

    df_for_plotting = pd.DataFrame({
    'CompetenceDimension': competenceDimensionData,
    'CompetenceScore': competenceScoreData
    })

    fig = px.bar(df_for_plotting, x='CompetenceDimension', y='CompetenceScore', text=competenceScoreData, labels={'competenceDimensionData': 'Kompetenzdimension', 'competenceScoreData':'Erzielte Punkte in %'},
                  color_discrete_sequence=custom_colors,template="simple_white")

    fig.update_layout(xaxis_title="ITS-Kompetenzdimension", xaxis_title_standoff=25,
    yaxis_title="Erzielte Punkte in %",
    yaxis=dict(ticksuffix="%", range=[0, 110]),
    margin=dict(t=5, b=100),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.25,
        xanchor="center",
        x=0.5,
        font=dict(
            size=20,  
            color="black" 
        )
    ),
     font=dict(
        family="Georgia, serif",  
        size=16, 
    ),
    uniformtext_minsize=20,  
    uniformtext_mode='hide',
    title_font=dict(
        size=20, 
        color="black"
        )
    )
    fig.update_traces(textangle=-45, textposition='inside')
    fig.add_shape( 
    type="line", line_color="salmon", line_width=3, opacity=1, line_dash="dot",
    x0=0, x1=1, xref="paper", y0=50, y1=51, yref="y"
    )
    fig.add_shape( 
    type="line", line_color="green", line_width=3, opacity=1, line_dash="dot",
    x0=0, x1=1, xref="paper", y0=66, y1=67, yref="y"
    ) 

    svg = pio.to_image(fig, format='svg')

    base64_string = b64encode(svg).decode()

    

    img_html = f"""
    <img class="centered-image" src="data:image/svg+xml;base64,{base64_string}" alt="Chart"/>
    </div>
    """

    return img_html



def generate_competence_bar_chart_per_threat(threat, competence_test_results):
    """Creates a bar chart showing the percentage of scored points per competence dimension for a specific security threat related to a job profile.

    Args:
        threat (obj): A python object including the current security threat
        competence_test_results (dict): A python dictionary including the competence_test_results
        


    Returns:
        str: An HTML string representing the generated bar chart image.
    """
    df_competence_test_results = pd.DataFrame.from_dict(competence_test_results, orient='index')


    competenceScoreData = []
    competenceDimensionData = []


    for competence_dimension in threat.values():
                    participants = df_competence_test_results.iloc[0]['number_of_participants']
                    score = round(
                        (competence_dimension['total_scoredPoints'] /
                        ( MAX_POINTS_PER_COMPETENCE_DIMENSION * participants)) * 100
                    )
                    
                    competenceScoreData.append(score)
                    competenceDimensionData.append(competence_dimension['competence_dimension_name'])

    df_for_plotting = pd.DataFrame({
    'CompetenceDimension': competenceDimensionData,
    'CompetenceScore': competenceScoreData
    })
    

    fig = px.bar(df_for_plotting, x='CompetenceDimension', y='CompetenceScore', text=competenceScoreData, labels={'competenceDimensionData': 'Kompetenzdimension', 'competenceScoreData':'Erzielte Punkte in %'},
                  color_discrete_sequence=custom_colors,template="simple_white")

    fig.update_layout(xaxis_title="Kompetenzdimension", xaxis_title_standoff=50,
    yaxis_title="Erzielte Punkte in %",
    yaxis=dict(ticksuffix="%", range=[0, 110]),
    margin=dict(b=100),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.25,
        xanchor="center",
        x=0.5,
        font=dict(
            size=20, 
            color="black" 
        )
    ),
     font=dict(
        family="Georgia, serif",  
        size=16,
    ),
    uniformtext_minsize=20, 
    uniformtext_mode='hide',
    title_font=dict(
        size=20,
        color="black" 
        )
    )
    fig.update_traces(textangle=-45, textposition='inside')

    fig.add_shape( 
    type="line", line_color="salmon", line_width=3, opacity=1, line_dash="dot",
    x0=0, x1=1, xref="paper", y0=50, y1=51, yref="y"
    )  

    fig.add_shape( 
    type="line", line_color="green", line_width=3, opacity=1, line_dash="dot",
    x0=0, x1=1, xref="paper", y0=66, y1=67, yref="y"
    )  

    svg = pio.to_image(fig, format='svg')

    base64_string = b64encode(svg).decode()

    img_html = f"""
    <img class="centered-image" src="data:image/svg+xml;base64,{base64_string}" alt="Chart"/>
    </div>
    """

    return img_html

