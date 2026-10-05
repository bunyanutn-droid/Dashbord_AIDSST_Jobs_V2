import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

# Initialize the Dash app with a Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SLATE], suppress_callback_exceptions=True)
app.title = "AI & Data Science Workforce Dashboard"

# Define the basic layout with Tabs
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("AI, Data Science & Statistics Workforce Dashboard", className="text-center my-4 text-light"), width=12)
    ]),
    
    dbc.Row([
        dbc.Col([
            dcc.Tabs(id="tabs", value='tab-1', children=[
                dcc.Tab(label='Supply & Academic Skills', value='tab-1', className='custom-tab', selected_className='custom-tab--selected'),
                dcc.Tab(label='Industry Demand & Required Skills', value='tab-2', className='custom-tab', selected_className='custom-tab--selected'),
                dcc.Tab(label='Skill Mismatch Analytics', value='tab-3', className='custom-tab', selected_className='custom-tab--selected'),
            ], colors={"border": "white", "primary": "cyan", "background": "#1e293b"})
        ], width=12)
    ]),
    
    dbc.Row([
        dbc.Col(html.Div(id='tabs-content', className="mt-4"), width=12)
    ])
], fluid=True, style={"backgroundColor": "#0f172a", "minHeight": "100vh", "padding": "20px"})

# Callback to render tab content
@app.callback(
    dash.dependencies.Output('tabs-content', 'children'),
    [dash.dependencies.Input('tabs', 'value')]
)
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3("Tab 1: Graduate Supply & Academic Skills", className="text-light"),
            html.P("Content for Supply Analysis will go here.", className="text-light")
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3("Tab 2: Industry Demand & Market Skills", className="text-light"),
            html.P("Content for Demand Analysis will go here.", className="text-light")
        ])
    elif tab == 'tab-3':
        return html.Div([
            html.H3("Tab 3: Skill Mismatch Analytics", className="text-light"),
            html.P("Content for Mismatch Analytics will go here.", className="text-light")
        ])
    return html.Div()

if __name__ == '__main__':
    app.run_server(debug=True)
