# MIT License
#
# Copyright (c) 2023 Clément RAOUL
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""This module create the div containing the instant bar graph view."""

import dash
from plotly import graph_objects as go


# pylint: disable=too-few-public-methods
class InstantGraphView:
    """
    Instant Graph View.
    """

    @staticmethod
    def create_instant_graph_view(fig_day: go.Figure) -> dash.html.Div:
        """
        Return the html.Div for the right daily graph

        Args:
            fig_day (go.Figure): the figure for the day

        Returns:
            html.Div: the html.Div for the right daily graph
        """
        return dash.html.Div(
            [
                dash.html.Div(
                    [
                        dash.dcc.Graph(
                            figure=fig_day,
                            config={
                                "displayModeBar": False,
                                "displaylogo": False,
                            },
                            id="graph-day",
                        ),
                    ],
                    className="graph-day-container",
                ),
            ],
            className="graphs-content",
        )
