import plotly.express as px
import pandas as pd
import csv
with open ('cups of coffee vs hours of sleep.csv') as f:
    df = csv.DictReader(f)
    fig = px.scatter(df,x ='week',y = 'Coffee in ml')
    fig.show()