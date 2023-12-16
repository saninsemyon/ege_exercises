import plotly.express as px
import pandas as pd


def chart_progress(group, value):
    # Sample data
    df = pd.DataFrame(dict(
        group=group,
        value=value))

    fig = px.bar(df, x='group', y='value')

    fig.show()



