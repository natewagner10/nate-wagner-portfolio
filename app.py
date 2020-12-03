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
import numpy as np
import matplotlib.pyplot as plt
import torch
from torch import autograd
import torch.nn as nn
eps = np.finfo(float).eps
import os
from PIL import Image
from torchvision.utils import save_image
import base64
from io import BytesIO as _BytesIO
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd









df = pd.DataFrame([
    dict(Name="Palm Beach State College", Start='2014-08-01', Finish='2016-05-01', Event="Education"),
    dict(Name="Santa Fe College", Start='2016-08-01', Finish='2017-05-01', Event="Education"),    
    dict(Name="University of Florida", Start='2017-08-01', Finish='2019-05-01', Event="Education"),        
    dict(Name="Anchor Wealth Group", Start='2017-06-01', Finish='2017-08-01', Event="Internship/Work"),
    dict(Name="RGD Consulting Engineers", Start='2019-06-01', Finish='2019-08-01', Event="Internship/Work"),
    dict(Name="Bradenton Economic Development Corp", Start='2019-09-01', Finish='2020-02-01', Event="Internship/Work"),
    dict(Name="Economic Development Corp of Sarasota", Start='2020-01-01', Finish='2020-05-01', Event="Internship/Work"),    
    dict(Name="Mote Marine Lab", Start='2020-07-01', Finish='2020-12-01', Event="Internship/Work"),        
    dict(Name="Red Tide Research", Start='2020-07-01', Finish='2020-12-01', Event="Internship/Work"),            
    dict(Name="New College of Florida, MSDS", Start='2019-08-01', Finish='2020-12-01', Event="Education")
])

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Name", color="Event", template="plotly_white",hover_data={'Event':False})
fig.update_yaxes(autorange="reversed", visible=False)
fig.update_layout(title_text='Timeline of Education & Experience',
                  hoverlabel=dict(
                        bgcolor="white",
                        font_size=16,
                        font_family="HelveticaNeue"
    ))




app = dash.Dash(__name__,external_stylesheets=[dbc.themes.LITERA])


init_latent = np.random.normal(0,1,40)

app.layout = html.Div([    
                html.Br(),
                html.Br(),                
                html.Div(
                            [
                                html.Div(
                                    [html.H3("Nathaniel Wagner")],
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
                                            style = {'font-size': '14px','font':'HelveticaNeue'})],
                                    className="twelve columns main-title",
                                ),
                                html.Div(
                                    [html.P("(561) 337-0107", 
                                            style = {'font-size': '14px','font':'HelveticaNeue'})],
                                    className="twelve columns main-title",
                                ),                                    
                                html.Div(
                                    [html.P("natewag1234@gmail.com", 
                                            style = {'font-size': '14px','font':'HelveticaNeue'})],
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
                                    color="primary"),                        
                            ],className="twelve columns padded",
                        ),                                
                html.Div(
                            [
                                dbc.Collapse(
                                    dbc.Card(dbc.CardBody(
                                        [
                                            html.H6(["Manatee Identification Application"],style = {'font-size': '22px','font':'HelveticaNeue'},className="twelve columns"),
                                            html.P(["My team and I developed an application designed to query the Mote Marine Lab image dataset for similar images to the input image based on scar shape​ and scar ​location​"],style = {'font-size': '14px','font':'HelveticaNeue'},className="twelve columns"),
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
                                    color="primary"),                        
                            ],className="twelve columns padded",
                        ),                                
                html.Div(
                            [
                                dbc.Collapse(
                                    dbc.Card(dbc.CardBody(
                                        [
                                            html.H6(["Sarasota EDC - Automate Data Entry With Computer Vision"],style = {'font-size': '22px','font':'HelveticaNeue'},className="twelve columns"),
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
                                    color="primary"),                        
                            ],className="twelve columns padded",
                        ),                                
                html.Div(
                            [
                                dbc.Collapse(
                                    dbc.Card(dbc.CardBody(
                                        [
                                            html.H6(["Science and Environment Council"],style = {'font-size': '22px','font':'HelveticaNeue'},className="twelve columns"),
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


                ],className="page",)



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



if __name__ == '__main__':
    app.run_server()







































