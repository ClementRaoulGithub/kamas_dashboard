from dash import html, dcc
import numpy as np
from src.models.graph_model import GraphModel
from src.utils.scraping import get_kamas_value
from src.views.monocompte import boune_view
from src.utils.utils import fr_months
import plotly.express as px
import datetime


def monocompte_server() -> html.Div:
    start_year = 2020
    current_year = datetime.datetime.now().year

    description = f'Ces graphiques représentent les valeurs estimée du kamas en euros pour le serveur mono compte dofus rétro (sortie en {start_year})'
    fig_avg = create_graph(
        'Evolution du cours moyen du kamas',
        '',
        'Mois',
        'Valeur estimée moyenne',
        list(fr_months),
        list(range(12))
    )
    
    fig_day = create_daily_graph(
        'Valeur journalière du kamas',
        '',
        'Jour',
        'Valeur estimée journalière',
        get_kamas_value(),
        ["Kamas Facile", "Fun Shop", "Les Kamas"]
    )
    slider = dcc.Slider(
        min=0,
        step=1,
        max=current_year - start_year,
        marks={i: str(start_year + i) for i in range(current_year - start_year + 1)},
        value=0,
    )
    return boune_view(description, fig_day, fig_avg, slider)

def create_daily_graph(title: str, description: str, x_title: str, y_title: str, x_values: list, y_values: list) -> px.line:
    model = GraphModel(
        title=title,
        description=description,
        x_title=x_title,
        y_title=y_title,
        x_values=x_values,
        y_values=y_values,
    )
    fig = px.bar(
        x=y_values,
        y=x_values,
        title=model.title,
    )
    average_value=np.mean(x_values)
    fig.add_hline(y=average_value, line_dash="dash", annotation_text=f"Moyenne = {average_value}€", annotation_position="top left")
    
    return fig


def create_graph(title: str, description: str, x_title: str, y_title: str, x_values: list, y_values: list) -> px.line:
    model = GraphModel(
        title=title,
        description=description,
        x_title=x_title,
        y_title=y_title,
        x_values=x_values,
        y_values=y_values,
    )
    fig = px.line(
        x=model.x_values,
        y=model.y_values,
        labels={'x': model.x_title, 'y': model.y_title},
        title=model.title,
    )
    fig.update_traces(line=dict(color='red'))
    
    return fig