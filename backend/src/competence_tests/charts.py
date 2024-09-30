
from base64 import b64encode
import plotly.io as pio
import plotly.express as px
import pandas as pd




TOTAL_POSSIBLE_POINTS_PER_THREAT = 14  # Maximum points per threat
MAX_POINTS_PER_COMPETENCE_DIMENSION = 2 # Maximum points per Competence Dimension

custom_colors = ["#1f2c5a", "#f06666", "#683d87", "#303e7a", "#EB5757"]

def generate_threat_chart(threat_vectors, total_points_scored):
    """Creates a pie chart showing the percentage of scored points in the competence test for a specific security threat or over all security threats.

    Args:
        threat_vectors (list): A list of threat vectors for each job profile
        total_points_scored (int): A python dictionary inluding the total scored points


    Returns:
        str: An HTML string representing the generated pie chart image.
    """
    number_of_threats = len(threat_vectors)

    names = ["Korrekt beantwortet", "Falsch beantwortet"]
    max_points = TOTAL_POSSIBLE_POINTS_PER_THREAT * number_of_threats


    # Data to be added
    data = {
        'threat_data': [total_points_scored, max_points - total_points_scored],
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
def generate_competence_bar_chart(competence_dimension_scores, threat_vectors):
    """Creates a bar chart showing the percentage of scored points per competence dimension over all security threats related to a job profile.

    Args:
        competence_dimension_scores (dict): A python dictionary including the competence_dimension_scores that the participant achieved.
        threat_vectors (list): A list of threat vectors for each job profile


    Returns:
        str: An HTML string representing the generated bar chart image.
    """
    number_of_threats = len(threat_vectors)

    competenceScoreData = competence_dimension_scores['score']
    competenceScoreData = [(score / (MAX_POINTS_PER_COMPETENCE_DIMENSION*number_of_threats)) * 100 for score in competenceScoreData]
    competenceDimensionData = competence_dimension_scores['label']         

    df_for_plotting = pd.DataFrame({
    'CompetenceDimension': competenceDimensionData,
    'CompetenceScore': competenceScoreData
    })

    fig = px.bar(df_for_plotting, x='CompetenceDimension', y='CompetenceScore', text=competenceScoreData, labels={'competenceDimensionData': 'Kompetenzdimension', 'competenceScoreData':'Erzielte Punkte in %'},
                  color_discrete_sequence=custom_colors,template="simple_white")

    fig.update_layout(xaxis_title="ITS-Kompetenzdimension",
    yaxis_title="Erzielte Punkte in %",
    yaxis=dict(ticksuffix="%", range=[0, 110]),
    margin=dict(t=5, b=50), 
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

def generate_competence_bar_chart_per_threat(threat):
    """Creates a bar chart showing the percentage of scored points per competence dimension for a specific security threat related to a job profile.

    Args:
        threat (obj): A python object including the current security threat


    Returns:
        str: An HTML string representing the generated bar chart image.
    """

    competenceScoreData = []
    competenceDimensionData = []

    for competence_dimension in threat.values():
                    score = round(
                        (competence_dimension['total_scoredPoints'] /
                        ( MAX_POINTS_PER_COMPETENCE_DIMENSION)) * 100
                    )
                    
                    competenceScoreData.append(score)
                    competenceDimensionData.append(competence_dimension['competence_dimension_name'])

    df_for_plotting = pd.DataFrame({
    'CompetenceDimension': competenceDimensionData,
    'CompetenceScore': competenceScoreData
    })
    
    fig = px.bar(df_for_plotting, x='CompetenceDimension', y='CompetenceScore', text=competenceScoreData, labels={'competenceDimensionData': 'Kompetenzdimension', 'competenceScoreData':'Erzielte Punkte in %'},
                  color_discrete_sequence=custom_colors,template="simple_white")

    fig.update_layout(xaxis_title="Kompetenzdimension",
    yaxis_title="Erzielte Punkte in %",
    yaxis=dict(ticksuffix="%", range=[0, 100]),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.25,
        xanchor="center",
        x=0.5,
        font=dict(
            size=20,  
            color="black"  #
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


def generate_competence_bar_chart_per_threat(competence_dimensions_per_threat, competence_dimension_scores_per_threat):
    """Creates a bar chart showing the percentage of scored points per competence dimension for a specific security threat related to a job profile.

    Args:
        competence_dimension_per_threat (dict): A python dictionary including the competence dimensions per threat
        competence_dimension_score_per_threat (dict): A python dictionary including the competence dimension scores per threat
        


    Returns:
        str: An HTML string representing the generated bar chart image.
    """

    df_for_plotting = pd.DataFrame({
    'CompetenceDimension': competence_dimensions_per_threat,
    'CompetenceScore': competence_dimension_scores_per_threat
    })
    


    fig = px.bar(df_for_plotting, x='CompetenceDimension', y='CompetenceScore', text=competence_dimension_scores_per_threat, labels={'competence_dimensions_per_threat': 'Kompetenzdimension', 'competenceScoreData':'Erzielte Punkte in %'},
                  color_discrete_sequence=custom_colors,template="simple_white")

    fig.update_layout(xaxis_title="Kompetenzdimension",
    yaxis_title="Erzielte Punkte in %",
    yaxis=dict(ticksuffix="%", range=[0, 110]),
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