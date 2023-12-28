"""Main template view for the app."""

import dash

from src import NAME


def header() -> dash.html.Header:
    """
    return the header of the app

    Returns:
        dash.html.Header: the header of the app
    """
    return dash.html.Header(
        children=[
            dash.html.Div(
                [
                    dash.html.Img(src="/assets/logo.png", className="logo"),
                    dash.html.H3(children=NAME.capitalize()),
                ],
                className="header-container",
            ),
            dash.html.P("Visualisation de valeurs de kamas"),
        ],
        className="header",
    )


def footer() -> dash.html.Footer:
    """
    return the footer of the app

    Returns:
        dash.html.Footer: the footer of the app
    """
    return dash.html.Footer(
        dash.html.P(children=f"© {NAME} 2023, work in progress", className="footer")
    )


def top_menu() -> dash.html.Div:
    """
    return the top menu of the app

    Returns:
        dash.html.Div: the top menu of the app
    """
    dofus_retro_menu = dash.html.Div(
        dash.html.Div(
            [
                dash.html.Button("Dofus Retro", id="button-top-menu-retro"),
                dash.html.Div(
                    [
                        dash.dcc.Link("Serveur Boune", href="/boune", className="link"),
                        dash.dcc.Link("Serveur Crail", href="/crail", className="link"),
                        dash.dcc.Link("Serveur Eratz", href="/eratz", className="link"),
                        dash.dcc.Link(
                            "Serveur Galgarion", href="/galgarion", className="link"
                        ),
                        dash.dcc.Link(
                            "Serveur Henual", href="/henual", className="link"
                        ),
                    ],
                    style={"display": "none"},
                    id="top-menu-retro",
                ),
            ]
        )
    )
    dofus_classic_menu = dash.html.Div(
        dash.html.Div(
            [
                dash.html.Button("Dofus 2", id="button-top-menu-classic"),
                dash.html.Div(
                    [
                        dash.dcc.Link(
                            "Serveur Draconiros", href="/draconiros", className="link"
                        ),
                        dash.dcc.Link(
                            "Serveur HellMina", href="/hellmina", className="link"
                        ),
                        dash.dcc.Link(
                            "Serveur Imagiro", href="/imagiro", className="link"
                        ),
                        dash.dcc.Link("Serveur Ombre", href="/ombre", className="link"),
                        dash.dcc.Link(
                            "Serveur Orukam", href="/orukam", className="link"
                        ),
                        dash.dcc.Link(
                            "Serveur Talkasha", href="/talkasha", className="link"
                        ),
                        dash.dcc.Link(
                            "Serveur Tylezia", href="/tylezia", className="link"
                        ),
                    ],
                    style={"display": "none"},
                    id="top-menu-classic",
                ),
            ]
        )
    )
    return dash.html.Div(
        [
            dofus_retro_menu,
            dofus_classic_menu,
        ],
        className="top-menu",
    )


def template_view() -> dash.html.Div:
    """
    return the template view of the app

    Returns:
        dash.html.Div: the template view of the app
    """
    content = dash.html.Div(className="main-content", id="main-content")
    return dash.html.Div(
        children=[
            header(),
            dash.dcc.Location(id="url"),
            top_menu(),
            dash.html.Div(
                children=[
                    content,
                    footer(),
                ],
                className="body-container",
            ),
        ],
        className="container",
    )
