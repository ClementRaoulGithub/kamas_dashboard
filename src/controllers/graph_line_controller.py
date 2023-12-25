"""Controller for the line graph."""

import dash

from src.utils import global_variables
from src.utils.graphs import create_line_graph
from src.utils.scraping import get_scope_kamas_value
from src.utils.tools import LineGraphScope


@dash.callback(
    dash.Output("graph-line", "figure"), [dash.Input("graph-slider", "value")]
)
def graph_line_controller(value: int):
    """
    Controller for the line graph.

    Args:
        value (int): the value of the slider

    Returns:
        px.line: the line graph
    """
    scope = LineGraphScope(value).name.lower()
    kamas_dict = get_scope_kamas_value(
        server=global_variables.current_server_name,
        scope=scope,
    )

    return create_line_graph(
        "Evolution<br>du million de kamas",
        "",
        "Tps",
        "Valeur estimée moyenne",
        [dict["timestamp"] for dict in kamas_dict],
        [dict["average"] for dict in kamas_dict],
        [dict["max"] for dict in kamas_dict],
        [dict["min"] for dict in kamas_dict],
    )
