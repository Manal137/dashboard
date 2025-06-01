# import dash
# from layout import layout
# from callbacks import register_callbacks

# app = dash.Dash(__name__)
# app.title = "BladeRunner Dashboard"
# app.layout = layout

# register_callbacks(app)

# server = app.server

# if __name__ == '__main__':
#     app.run_server(debug=True, port=8050)


import dash
from layout import layout
from callbacks import register_callbacks

app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.title = "BladeRunner Dashboard"
app.layout = layout

register_callbacks(app)

server = app.server

# Health check endpoint for Docker
@server.route("/health")
def healthcheck():
    return "OK", 200

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)
