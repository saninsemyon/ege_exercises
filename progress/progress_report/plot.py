from datetime import date, timedelta

import plotly.express as px
import pandas as pd
import polars as pl


def chart_progress(x, y):
    # Sample data
    df = pd.DataFrame(dict(
        Weeks=x,
        Progress=y))

    fig = px.bar(df, x='Weeks', y='Progress')

    fig.show()


def gapminder_progress():
    df = px.data.gapminder()
    print(df)

    fig = px.scatter(df.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
                     hover_name="country", log_x=True, size_max=60)
    fig.show()


def show_chart_activities(hist_dict):
    df = pd.DataFrame(
        hist_dict
    )
    print(df)
    print(df.info())

    # fig = px.scatter(df.query("subjects=='inf'"), x="dates", y="subjects", size="progress", color="tasks", title="EGE Progress Chart")
    fig = px.bar(df, x="date", y="progress", color="subjects", hover_name="tasks", title="EGE Progress Chart")
    fig.show()


def show_chart_fact(hist_dict):
    df = pd.DataFrame(
        hist_dict
    )
    print(df)
    print(df.info())

    # fig = px.scatter(df.query("subjects=='inf'"), x="dates", y="subjects", size="progress", color="tasks", title="EGE Progress Chart")
    fig = px.bar(df, x="tasks", y="progress", color="levels", hover_name="tasks", title="EGE Fact Chart")
    fig.show()
