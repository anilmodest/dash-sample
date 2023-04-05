import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from pages.page1 import page_3_layout
from config import db_config

# Define the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the sidebar
sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P("This is a sidebar"),
        dbc.Nav(
            [
                dbc.NavLink("Page 1", href="/page-1", id="page-1-link"),
                dbc.NavLink("Page 2", href="/page-2", id="page-2-link"),
                dbc.NavLink("Page 3", href="/page-3", id="page-3-link")
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="bg-light",
    style={
        "position": "fixed",
        "top": 0,
        "left": 0,
        "bottom": 0,
        "width": "20%",
        "padding": "20px",
    },
)

# Define the content
content = html.Div(id="page-content", style={"margin-left": "25%"})

# Define the pages
page_1_layout = html.Div([html.H1("Page 1")])
page_2_layout = html.Div([html.H1("Page 2")])

# Define the callbacks
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.H1("Welcome to the app!")
    elif pathname == "/page-1":
        return html.Div([
            html.H1("Page 1"),
            dcc.Graph(
                id="example-graph",
                figure={
                    "data": [{"x": [1, 2, 3], "y": [4, 1, 2], "type": "bar"}],
                    "layout": {"title": "Bar Chart"},
                },
            ),
        ])
    elif pathname == "/page-2":
        return html.Div([
            html.H1("Page 2"),
            dcc.Graph(
                id="example-graph-2",
                figure={
                    "data": [{"x": [1, 2, 3], "y": [10, 5, 7], "type": "line"}],
                    "layout": {"title": "Line Chart"},
                },
            ),
        ])
    elif pathname == "/page-3":
        return page_3_layout
    else:
        return html.H1("404 - Page not found")

# Define the app layout
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
