from dash import html

from src.utils.backend.backend import backend_get_kamas_value
from src.utils.scraping import get_daily_kamas_value, get_yesterday_kamas_value
from src.utils.utils import view_graph
from src.views.server_view import server_view


def henual_server() -> html.Div:
    name = "henual"
    description = f"Ces graphiques représentent les valeurs estimée du kamas en euros pour le serveur multi compte {name}"
    kamas_dict = backend_get_kamas_value(server=name)
    day_kamas_dict = get_daily_kamas_value(server=name)
    yesterday_kamas_dict = get_yesterday_kamas_value(server=name)

    fig_day, fig_avg, fig_gauge, best_price = view_graph(day_kamas_dict, yesterday_kamas_dict, kamas_dict)

    return server_view(
        name,
        description,
        fig_day,
        fig_avg,
        fig_gauge,
        best_price,
        average=day_kamas_dict["average"],
        nb_site=len(day_kamas_dict["kamas_dict"]),
    )