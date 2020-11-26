import plotly.express as px
import pandas as pd
import csv
with open ('Student Marks vs Days Present.csv') as f:
    df = csv.DictReader(f)
    fig = px.scatter(df,x ='Roll No',y = 'Marks In Percentage')
    fig.show()