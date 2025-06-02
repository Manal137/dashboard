
# # Add the full path to the bladerunner folder to sys.path
# import os
# import sys
# sys.path.append(os.path.join(os.path.dirname(__file__), 'bladerunner'))

# import dash
# from dashboard.layout import layout
# from dashboard.callbacks import register_callbacks

# app = dash.Dash(__name__, suppress_callback_exceptions=True)
# app.title = "BladeRunner Dashboard"
# app.layout = layout

# register_callbacks(app)

# server = app.server

# # Health check endpoint for Docker
# @server.route("/health")
# def healthcheck():
#     return "OK", 200

# if __name__ == '__main__':
#     app.run_server(debug=True, host='0.0.0.0', port=8050)



import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'bladerunner'))

import dash
from dashboard.layout import layout
from dashboard.callbacks import register_callbacks

app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.title = "BladeRunner Dashboard"
app.layout = layout

# Prepare the full path for design_params.json
base_path = os.path.dirname(__file__)
design_params_path = os.path.join(base_path, 'bladerunner', 'engine', 'design_params.json')

# Pass design_params_path to register_callbacks
register_callbacks(app, design_params_path)

server = app.server

@server.route("/health")
def healthcheck():
    return "OK", 200

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)
