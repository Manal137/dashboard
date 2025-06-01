

# from dash import html, dcc

# layout = html.Div(className="main-container", children=[
#     html.Div(className="header", children=[
#         html.H1(" BladeRunner Dashboard", className="dashboard-title"),
#         html.P(" ", className="subtitle")
#     ]),

#     html.Div(className="grid-container", children=[

#         # LEFT PANEL (30%)
#         html.Div(className="card left-panel", children=[
#             html.Div(className="card-content", children=[
#                 html.Div(className="input-group", children=[
#                     html.Label("Thrust (N)", className="input-label"),
#                     dcc.Input(id="thrust", type="number", placeholder="50", debounce=True, className="input-box"),
#                 ]),
#                 html.Div(className="input-group", children=[
#                     html.Label("Speed (m/s)", className="input-label"),
#                     dcc.Input(id="flight-speed", type="number", placeholder=" 20", debounce=True, className="input-box"),
#                 ]),
#                 html.Div(className="input-group", children=[
#                     html.Label("Diameter (m):", className="input-label"),
#                     dcc.Input(id="tip-dia", type="number", placeholder="0.2", debounce=True, className="input-box"),
#                 ]),
#                 html.Div(className="input-group", children=[
#                     html.Label("Altitude (m)", className="input-label"),
#                     dcc.Input(id="altitude", type="number", placeholder="10", debounce=True, className="input-box"),
#                 ]),

#                 html.Button(" Generate Plot", id="generate-button", n_clicks=0, className="full-btn"),
#                 html.Div(id="message", className="status-message")
#             ])
#         ]),

#         # RIGHT PANEL (70%)
#         html.Div(className="card right-panel", children=[
#             html.Div(className="card-content", children=[
#                 html.Div(className="input-group", children=[
#                     html.Label("Select Plot Type:", className="dropdown-label"),
#                     dcc.Dropdown(
#                         id='plot-selector',
#                         options=[
#                             {'label': 'Flight Speed vs Thrust', 'value': 'fst'},
#                             {'label': 'Flight Speed vs Power', 'value': 'fsp'},
#                             {'label': 'Flight Speed vs RPM', 'value': 'fsrpm'}
#                         ],
#                         placeholder="Select a plot to display",
#                         className="dropdown"
#                     )
#                 ]),
#                 dcc.Graph(id='plot-output', className="graph-style")
#             ])
#         ])
#     ]),

#     dcc.Store(id='engine-data-store')
# ])




from dash import html, dcc

layout = html.Div(className="main-container", children=[
    html.Div(className="header", children=[
        html.H1(" BladeRunner Dashboard", className="dashboard-title"),
        html.P(" ", className="subtitle")
    ]),

    html.Div(className="grid-container", children=[

        # LEFT PANEL (30%)
        html.Div(className="card left-panel", children=[
            html.Div(className="card-content", children=[
                html.Div(className="input-group", children=[
                    html.Label("Thrust (N)", className="input-label"),
                    dcc.Input(id="thrust", type="number", placeholder="50", debounce=True, className="input-box"),
                ]),
                html.Div(className="input-group", children=[
                    html.Label("Speed (m/s)", className="input-label"),
                    dcc.Input(id="flight-speed", type="number", placeholder=" 20", debounce=True, className="input-box"),
                ]),
                html.Div(className="input-group", children=[
                    html.Label("Diameter (m):", className="input-label"),
                    dcc.Input(id="tip-dia", type="number", placeholder="0.2", debounce=True, className="input-box"),
                ]),
                html.Div(className="input-group", children=[
                    html.Label("Altitude (m)", className="input-label"),
                    dcc.Input(id="altitude", type="number", placeholder="10", debounce=True, className="input-box"),
                ]),

                html.Button(" Generate graph", id="generate-button", n_clicks=0, className="full-btn"),
                html.Div(id="message", className="status-message")
            ])
        ]),

        # RIGHT PANEL (70%)
        html.Div(className="card right-panel", children=[
            html.Div(className="card-content", children=[
                html.Div(className="input-group", children=[
                    html.Label("Select Plot Type:", className="dropdown-label"),
                    dcc.Dropdown(
                        id='plot-selector',
                        options=[
                            {'label': 'Flight Speed vs Thrust', 'value': 'fst'},
                            {'label': 'Flight Speed vs Power', 'value': 'fsp'},
                            {'label': 'Flight Speed vs RPM', 'value': 'fsrpm'}
                        ],
                        placeholder="Select a plot to display",
                        className="dropdown"
                    )
                ]),
                dcc.Graph(id='plot-output', className="graph-style")
            ])
        ])
    ]),

    dcc.Store(id='engine-data-store')
])
