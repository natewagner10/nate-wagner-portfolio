#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 11:22:18 2020

@author: natewagner
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import plotly.graph_objs as go



df = pd.DataFrame([
    dict(Organization="Palm Beach State College", Start='2014-08-01', Finish='2016-05-01', Event="Education"),
    dict(Organization="Santa Fe College", Start='2016-08-01', Finish='2017-05-01', Event="Education"),    
    dict(Organization="University of Florida", Start='2017-08-01', Finish='2019-05-01', Event="Education"),        
    dict(Organization="Anchor Wealth Group", Start='2017-06-01', Finish='2017-08-01', Event="Internship/Work"),
    dict(Organization="RGD Consulting Engineers", Start='2019-06-01', Finish='2019-08-01', Event="Internship/Work"),
    dict(Organization="Bradenton Economic Development Corp", Start='2019-09-01', Finish='2020-02-01', Event="Internship/Work"),
    dict(Organization="Economic Development Corp of Sarasota", Start='2020-01-01', Finish='2020-05-01', Event="Internship/Work"),    
    dict(Organization="Mote Marine Lab", Start='2020-07-01', Finish='2020-12-01', Event="Internship/Work"),        
    dict(Organization="Red Tide Research", Start='2020-07-01', Finish='2020-12-01', Event="Internship/Work"),            
    dict(Organization="New College of Florida, MSDS", Start='2019-08-01', Finish='2020-12-01', Event="Education")
])

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Organization", color="Event", template="plotly_white",hover_data={'Event':False})
fig.update_yaxes(autorange="reversed", visible=False)
fig.update_layout(title_text='Timeline of Education & Experience',
                  font_color="black",
                  font_family="HelveticaNeue",
                  font_size=20,
                  hoverlabel=dict(
                        bgcolor="white",
                        font_size=16,
                        font_family="HelveticaNeue"
    ))



dataSkills=dict(data=[go.Scatterpolar(
                          r = [62.5, 87.5, 87.5, 75, 100, 25, 25, 100, 12.5, 37.6, 25, 25, 25, 12.5, 12.5, 62.5],
                          theta = ['Python','R', 'Tidyverse', 'Machine Learning', 'Statistics', 'Deep Learning', 'Pyspark', 'Data Viz', 'Plotly Dash', 'Shiny', 'Pandas', 'Numpy', 'OpenCv/Pillow','Pytorch', 'Tensorflow', 'Python'],
                          fill = 'toself',
                          line = dict(color='salmon'),
                          hoverinfo='none'
                                            )
                           ],

              layout= go.Layout(xaxis=dict(visible=False),
                                yaxis=dict(visible=False),
                                font=dict(size=14),
                                polar = dict(
                                            radialaxis = dict(
                                                              visible = True,
                                                              range = [0, 100],
                                                              tickvals=[25,50,75,100],
                                                              ticktext=['25%','50%','75%','100%'],
                                                              tickmode='array',
                                                              tickangle=25,
                                                              tickfont=dict(
                                                                    family='Arial',
                                                                    size=13,
                                                                    color='#acb3bf'
                                                                            )
                                                                )
                                              ),
                                showlegend = False,
                                height=500,
                                width=500
                                )
             )



app = dash.Dash(__name__,external_stylesheets=[dbc.themes.LITERA])
server = app.server


app.layout = html.Div([    
                html.Br(),
                html.Br(),                
                html.Div(
                            [
                                html.Div(
                                    [html.H3("Nathaniel Wagner",style = {'font-size': '48px','font':'HelveticaNeue','font-color': '#000000'})],
                                    className="seven columns main-title",
                                ),
                                html.Div(
                                    [html.A("LinkedIn",
                                            href="https://www.linkedin.com/in/nathaniel-wagner-6aa228131/",
                                            style = {'font-size': '14px','font':'HelveticaNeue'},
                                            className="full-view-link",)],
                                    className="five columns",
                                ),                                    
                            ],
                            className="twelve columns",                            
                        ),
                html.Div(
                            [
                                html.Div(
                                    [html.P("724 New Jersey Street, West Palm Beach, Florida 33401", 
                                            style = {'font-size': '18px','font':'HelveticaNeue'})],
                                    className="twelve columns main-title",
                                ),
                                html.Div(
                                    [html.P("(561) 337-0107", 
                                            style = {'font-size': '18px','font':'HelveticaNeue'})],
                                    className="twelve columns main-title",
                                ),                                    
                                html.Div(
                                    [html.P("natewag1234@gmail.com", 
                                            style = {'font-size': '18px','font':'HelveticaNeue'})],
                                    className="twelve columns main-title",
                                ),                                                                                     
                            ],
                    ),                                                                               
                html.Div(
                            [
                                html.Div([
                                    html.Br([]),
                                    html.Hr(),
                                    dcc.Graph(figure=fig,
                                        config={
                                            'displayModeBar': False
                                                }),                                                                                                           
                                    ],className="twelve columns",     
                                ),

                                
                            ],
                    ),
                html.Div(
                            [
                                html.H3(["Projects"],className="subtitle padded"),
                                html.Hr(),
                            ],className="twelve columns"),
                html.Div(
                            [                                
                                html.H5(["Mote Marine Laboratory & Aquarium"],className="nine columns"),
                                dbc.Button(
                                    "More Information",
                                    id="collapse-button",
                                    className="three columns",
                                    color="primary",
                                    style = {'font-size': '10px','font':'HelveticaNeue'}),                        
                            ],className="twelve columns padded",
                        ),                                
                html.Div(
                            [
                                dbc.Collapse(
                                    dbc.Card(dbc.CardBody(
                                        [
                                            html.H6(["Manatee Identification Application - (Data Science Intern)"],style = {'font-size': '22px','font':'HelveticaNeue'},className="twelve columns"),
                                            html.P(["My team and I developed an application designed to query the Mote Marine Lab image dataset for similar images to the input image based on scar shape​ and scar ​location.​"],style = {'font-size': '14px','font':'HelveticaNeue'},className="twelve columns"),
                                            html.P(["The dashboard takes a scar and bounding box as input, and the program only searches for similar scars in that region. The user can also enter empty bounding boxes, signaling the program not to return images with scars in that region.  Many different scar patterns do better with different weights, so we also included the option to adjust the weights in the dashboard, including automatic re-adjustment.​"],style = {'font-size': '14px','font':'HelveticaNeue'},className="twelve columns"),                                            
                                            html.H6(["Tools Used:"],style = {'font-size': '14px','font':'HelveticaNeue'},className="twelve columns"),
                                            html.Li("Python",style = {'font-size': '14px','font':'HelveticaNeue'}),
                                            html.Li("Plotly Dash",style = {'font-size': '14px','font':'HelveticaNeue'}),                                            
                                            html.Li("Open CV, Pillow",style = {'font-size': '14px','font':'HelveticaNeue'}),                                            
                                            html.Div(
                                                [
                                                    html.A(
                                                        html.Button("See Application"),
                                                        href="https://identify-manatee.herokuapp.com/",
                                                        className="twelve columns left-aligned",
                                                    ),                                                        
                                                    html.A(
                                                        html.Button("See Github"),
                                                        href="https://github.com/natewagner10/Mote-Marine-Lab",
                                                        className="twelve columns left-aligned",
                                                    ),                                                                                                
                                                ],className="twelve columns",
                                                )
                                            
                                            
                                        ],className="twelve columns"),),
                                    id="collapse",
                                    className="twelve columns",                                         
                                ),
                            ],className="twelve columns",
                        ),
                html.Div(
                            [                                
                                html.H5(["Sarasota Economic Development Corp"],className="nine columns"),
                                dbc.Button(
                                    "More Information",
                                    id="collapse-button2",
                                    className="three columns",
                                    color="primary",
                                    style = {'font-size': '10px','font':'HelveticaNeue'}),                        
                            ],className="twelve columns padded",
                        ),                                
                html.Div(
                            [
                                dbc.Collapse(
                                    dbc.Card(dbc.CardBody(
                                        [
                                            html.H6(["Sarasota EDC - Automate Data Entry With Computer Vision (Data Science Intern)"],style = {'font-size': '22px','font':'HelveticaNeue'},className="twelve columns"),
                                            html.P(["This project explores various techniques to automate the data entry of surveys sent out by the EDC of Sarasota.​"],style = {'font-size': '14px','font':'HelveticaNeue'}, className="twelve columns"),                                            
                                            html.H6(["Tools Used:"],style = {'font-size': '14px','font':'HelveticaNeue'} ,className="twelve columns"),
                                            html.Li("Python",style = {'font-size': '14px','font':'HelveticaNeue'}),
                                            html.Li("Tenserflow - Keras",style = {'font-size': '14px','font':'HelveticaNeue'}),                                            
                                            html.Li("Open CV, Pillow",style = {'font-size': '14px','font':'HelveticaNeue'}),
                                            html.Li("Mask R-CNN",style = {'font-size': '14px','font':'HelveticaNeue'}),
                                            html.Li("Tidyverse",style = {'font-size': '14px','font':'HelveticaNeue'}),                                            
                                            html.Div(
                                                [
                                                    html.A(
                                                        html.Button("See Presentation"),
                                                        href="https://github.com/natewagner10/SarasotaEDC/blob/master/Computer%20Vision%20To%20Read%20Scanned%20Surveys%20(1).pdf",
                                                        className="twelve columns left-aligned",
                                                    ),                                                        
                                                    html.A(
                                                        html.Button("See Github"),
                                                        href="https://github.com/natewagner10/SarasotaEDC",
                                                        className="twelve columns left-aligned",
                                                    ),     
                                                    html.A(
                                                        html.Button("See Survey Results"),
                                                        href="https://github.com/natewagner10/SarasotaEDC/blob/master/2019survey_focused_report.pdf",
                                                        className="twelve columns left-aligned",
                                                    ),                                                                                             
                                                ],className="twelve columns",
                                                )
                                            
                                            
                                        ],className="twelve columns"),),
                                    id="collapse2",
                                    className="twelve columns",                                         
                                ),
                            ],className="twelve columns",
                        ),   
                html.Div(
                            [                                
                                html.H5(["Red Tide Research Project"],className="nine columns"),
                                dbc.Button(
                                    "More Information",
                                    id="collapse-button3",
                                    className="three columns",
                                    color="primary",
                                    style = {'font-size': '10px','font':'HelveticaNeue'}),                        
                            ],className="twelve columns padded",
                        ),                                
                html.Div(
                            [
                                dbc.Collapse(
                                    dbc.Card(dbc.CardBody(
                                        [
                                            html.H6(["Science and Environment Council (Research Associate)"],style = {'font-size': '22px','font':'HelveticaNeue'},className="twelve columns"),
                                            html.P(["New College of Florida professor Dr. Andrey Skripnikov and I use Twitter data to study the 2018 Florida red tide event. Our goal is to develop a framework to enhance response and assesment of future red tide events."],style = {'font-size': '14px','font':'HelveticaNeue'},className="twelve columns"),                                            
                                            html.H6(["Tools Used:"],style = {'font-size': '14px','font':'HelveticaNeue'},className="twelve columns"),
                                            html.Li("R - Tidyverse",style = {'font-size': '14px','font':'HelveticaNeue'}),                                           
                                            html.Div(
                                                [
                                                    html.A(
                                                        html.Button("See Presentation"),
                                                        href="https://github.com/natewagner10/Florida-Red-Tide/blob/master/Red_Tide_Presentation%20(3).pdf",
                                                        className="twelve columns left-aligned",
                                                    ),                                                        
                                                    html.A(
                                                        html.Button("See Github"),
                                                        href="https://github.com/UsDAnDreS/Florida-Red-Tide-Event",
                                                        className="twelve columns left-aligned",
                                                    ),                                                                                                
                                                ],className="twelve columns",
                                                )
                                            
                                            
                                        ],className="twelve columns"),),
                                    id="collapse3",
                                    className="twelve columns",                                         
                                ),
                            ],className="twelve columns",
                        ),      
                html.Div(
                            [                                
                                html.H5(["Political Facebook Ads Analysis"],className="nine columns"),
                                dbc.Button(
                                    "More Information",
                                    id="collapse-button4",
                                    className="three columns",
                                    color="primary",
                                    style = {'font-size': '10px','font':'HelveticaNeue'}),                        
                            ],className="twelve columns padded",
                        ),                                
                html.Div(
                            [
                                dbc.Collapse(
                                    dbc.Card(dbc.CardBody(
                                        [
                                            html.H6(["Distributed Computing Final Project"],style = {'font-size': '22px','font':'HelveticaNeue'},className="twelve columns"),
                                            html.P(["This project explores Pro Publica's Database of political Facebook ads. Our approach was to analyze ad frequencies over time, as well as a sentiment analysis broken down by political issues and organizations."],style = {'font-size': '14px','font':'HelveticaNeue'},className="twelve columns"),                                            
                                            html.H6(["Tools Used:"],style = {'font-size': '14px','font':'HelveticaNeue'},className="twelve columns"),
                                            html.Li("Pyspark",style = {'font-size': '14px','font':'HelveticaNeue'}),
                                            html.Li("Pyspark Machine Learning Library",style = {'font-size': '14px','font':'HelveticaNeue'}),                                                                                       
                                            html.Li("Python",style = {'font-size': '14px','font':'HelveticaNeue'}),                                                                                       
                                            html.Li("R - Tidyverse",style = {'font-size': '14px','font':'HelveticaNeue'}),                                           
                                            html.Div(
                                                [
                                                    html.A(
                                                        html.Button("See Presentation"),
                                                        href="https://natewagner10.github.io/Distributed-Computing-Facebook-Ads/main.html",
                                                        className="twelve columns left-aligned",
                                                    ),                                                        
                                                    html.A(
                                                        html.Button("See Github"),
                                                        href="https://github.com/natewagner10/Distributed-Computing-Facebook-Ads",
                                                        className="twelve columns left-aligned",
                                                    ),                                                                                                
                                                ],className="twelve columns",
                                                )
                                            
                                            
                                        ],className="twelve columns"),),
                                    id="collapse4",
                                    className="twelve columns",                                         
                                ),
                            ],className="twelve columns",
                        ),   
                html.Div(
                            [                                
                                html.H5(["COVID-19 Dashboard"],className="nine columns"),
                                dbc.Button(
                                    "More Information",
                                    id="collapse-button5",
                                    className="three columns",
                                    color="primary",
                                    style = {'font-size': '10px','font':'HelveticaNeue'}),                        
                            ],className="twelve columns padded",
                        ),                                
                html.Div(
                            [
                                dbc.Collapse(
                                    dbc.Card(dbc.CardBody(
                                        [
                                            html.H6(["Data Visualization and Reporting Project"],style = {'font-size': '22px','font':'HelveticaNeue'},className="twelve columns"),
                                            html.P(["This project consist of a Shiny Dashboard visualizing aggregated Covid-19 timeseries data from the New York Times."],style = {'font-size': '14px','font':'HelveticaNeue'},className="twelve columns"),                                            
                                            html.H6(["Tools Used:"],style = {'font-size': '14px','font':'HelveticaNeue'},className="twelve columns"),                                        
                                            html.Li("R Shiny",style = {'font-size': '14px','font':'HelveticaNeue'}),                                                                                       
                                            html.Li("R - Tidyverse",style = {'font-size': '14px','font':'HelveticaNeue'}),                                           
                                            html.Div(
                                                [
                                                    html.A(
                                                        html.Button("See Dashboard"),
                                                        href="https://nwagner.shinyapps.io/COVID-19/?_ga=2.186977761.896718136.1589809159-688664654.1589372921",
                                                        className="twelve columns left-aligned",
                                                    ),                                                        
                                                    html.A(
                                                        html.Button("See Github"),
                                                        href="https://github.com/natewagner10/DataViz_Final_Project",
                                                        className="twelve columns left-aligned",
                                                    ),                                                                                                
                                                ],className="twelve columns",
                                                )
                                            
                                            
                                        ],className="twelve columns"),),
                                    id="collapse5",
                                    className="twelve columns",                                         
                                ),
                            ],className="twelve columns",
                        ),                  
                html.Div(
                            [                                
                                html.H5(["Uber Trips Analysis"],className="nine columns"),
                                dbc.Button(
                                    "More Information",
                                    id="collapse-button6",
                                    className="three columns",
                                    color="primary",
                                    style = {'font-size': '10px','font':'HelveticaNeue'}),                        
                            ],className="twelve columns padded",
                        ),                                
                html.Div(
                            [
                                dbc.Collapse(
                                    dbc.Card(dbc.CardBody(
                                        [
                                            html.H6(["Distributed Computing Course Project"],style = {'font-size': '22px','font':'HelveticaNeue'},className="twelve columns"),
                                            html.P(["Using distributed computing systems to develop a story about Uber pickup data in New York 2014."],style = {'font-size': '14px','font':'HelveticaNeue'},className="twelve columns"),                                            
                                            html.H6(["Tools Used:"],style = {'font-size': '14px','font':'HelveticaNeue'},className="twelve columns"),                                        
                                            html.Li("Pyspark",style = {'font-size': '14px','font':'HelveticaNeue'}),
                                            html.Li("R Shiny",style = {'font-size': '14px','font':'HelveticaNeue'}),                                                                                       
                                            html.Li("R - Tidyverse",style = {'font-size': '14px','font':'HelveticaNeue'}),                                           
                                            html.Div(
                                                [
                                                    html.A(
                                                        html.Button("See Dashboard"),
                                                        href="https://mandabucklin7.shinyapps.io/Uber-Pickups/",
                                                        className="twelve columns left-aligned",
                                                    ),                                                        
                                                    html.A(
                                                        html.Button("See Github"),
                                                        href="https://github.com/natewagner10/Distributed-Computing-Uber-Project",
                                                        className="twelve columns left-aligned",
                                                    ),                                                                                                
                                                ],className="twelve columns",
                                                )
                                            
                                            
                                        ],className="twelve columns"),),
                                    id="collapse6",
                                    className="twelve columns",                                         
                                ),
                            ],className="twelve columns",
                        ),  
                html.Div(
                            [                                
                                html.H5(["2018 PGA Tour Season Analysis"],className="nine columns"),
                                dbc.Button(
                                    "More Information",
                                    id="collapse-button7",
                                    className="three columns",
                                    color="primary",
                                    style = {'font-size': '10px','font':'HelveticaNeue'}),                        
                            ],className="twelve columns padded",
                        ),                                
                html.Div(
                            [
                                dbc.Collapse(
                                    dbc.Card(dbc.CardBody(
                                        [
                                            html.H6(["Statistical Inference II Final Project"],style = {'font-size': '22px','font':'HelveticaNeue'},className="twelve columns"),
                                            html.P(["For our final project we explored data from the 2018 PGA Tour Season. We use methods such as linear and logistic regression as well as chi-squared test."],style = {'font-size': '14px','font':'HelveticaNeue'},className="twelve columns"),                                            
                                            html.H6(["Tools Used:"],style = {'font-size': '14px','font':'HelveticaNeue'},className="twelve columns"),                                                                                                                             
                                            html.Li("R - Tidyverse",style = {'font-size': '14px','font':'HelveticaNeue'}),                                           
                                            html.Div(
                                                [
                                                    html.A(
                                                        html.Button("See Presentation"),
                                                        href="https://natewagner10.github.io/Stat-Inference-Final-Project/main.html",
                                                        className="twelve columns left-aligned",
                                                    ),                                                        
                                                    html.A(
                                                        html.Button("See Github"),
                                                        href="https://github.com/natewagner10/Stat-Inference-Final-Project",
                                                        className="twelve columns left-aligned",
                                                    ),                                                                                                
                                                ],className="twelve columns",
                                                )
                                            
                                            
                                        ],className="twelve columns"),),
                                    id="collapse7",
                                    className="twelve columns",                                         
                                ),
                            ],className="twelve columns",
                        ), 
                html.Div(
                            [                                
                                html.H5(["Ride Sharing Analysis"],className="nine columns"),
                                dbc.Button(
                                    "More Information",
                                    id="collapse-button8",
                                    className="three columns",
                                    color="primary",
                                    style = {'font-size': '10px','font':'HelveticaNeue'}),                        
                            ],className="twelve columns padded",
                        ),                                
                html.Div(
                            [
                                dbc.Collapse(
                                    dbc.Card(dbc.CardBody(
                                        [
                                            html.H6(["Statistical Inference I Final Project"],style = {'font-size': '22px','font':'HelveticaNeue'},className="twelve columns"),
                                            html.P(["For our final project we explored Uber and Lyft pricing data."],style = {'font-size': '14px','font':'HelveticaNeue'},className="twelve columns"),                                            
                                            html.H6(["Tools Used:"],style = {'font-size': '14px','font':'HelveticaNeue'},className="twelve columns"),                                                                                                                             
                                            html.Li("R - Tidyverse",style = {'font-size': '14px','font':'HelveticaNeue'}),                                           
                                            html.Div(
                                                [
                                                    html.A(
                                                        html.Button("See Presentation"),
                                                        href="https://natewagner10.github.io/Ride-Sharing-Project/stats_project.html",
                                                        className="twelve columns left-aligned",
                                                    ),                                                        
                                                    html.A(
                                                        html.Button("See Github"),
                                                        href="https://github.com/natewagner10/Ride-Sharing-Project",
                                                        className="twelve columns left-aligned",
                                                    ),                                                                                                
                                                ],className="twelve columns",
                                                )
                                            
                                            
                                        ],className="twelve columns"),),
                                    id="collapse8",
                                    className="twelve columns",                                         
                                ),
                            ],className="twelve columns",                            
                        ),                     
                ],className="page")

@app.callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collapse2", "is_open"),
    [Input("collapse-button2", "n_clicks")],
    [State("collapse2", "is_open")],
)
def toggle_collapse2(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collapse3", "is_open"),
    [Input("collapse-button3", "n_clicks")],
    [State("collapse3", "is_open")],
)
def toggle_collapse3(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collapse4", "is_open"),
    [Input("collapse-button4", "n_clicks")],
    [State("collapse4", "is_open")],
)
def toggle_collapse4(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collapse5", "is_open"),
    [Input("collapse-button5", "n_clicks")],
    [State("collapse5", "is_open")],
)
def toggle_collapse5(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collapse6", "is_open"),
    [Input("collapse-button6", "n_clicks")],
    [State("collapse6", "is_open")],
)
def toggle_collapse6(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collapse7", "is_open"),
    [Input("collapse-button7", "n_clicks")],
    [State("collapse7", "is_open")],
)
def toggle_collapse7(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collapse8", "is_open"),
    [Input("collapse-button8", "n_clicks")],
    [State("collapse8", "is_open")],
)
def toggle_collapse8(n, is_open):
    if n:
        return not is_open
    return is_open

if __name__ == '__main__':
    app.run_server()
