
# from dash import Output, Input, State
# import plotly.graph_objs as go
# import pickle
# import base64
# from bladerunner.engine import engine_iterations

# design_params = "design_params.json"
# engine_iter = engine_iterations.EngineIterations(design_params)

# # Helpers for (de)serialization
# def serialize(obj):
#     return base64.b64encode(pickle.dumps(obj)).decode()

# def deserialize(s):
#     return pickle.loads(base64.b64decode(s.encode()))

# def register_callbacks(app):

#     @app.callback(
#         Output('message', 'children'),
#         Output('engine-data-store', 'data'),
#         Input('generate-button', 'n_clicks'),
#         State('thrust', 'value'),
#         State('flight-speed', 'value'),
#         State('tip-dia', 'value'),
#         State('altitude', 'value'),
#     )
#     def generate_engine(n_clicks, thrust, speed, tip_dia, altitude):
#         if n_clicks == 0:
#             return "", None

#         try:
#             print(f"Input values: thrust={thrust}, speed={speed}, tip_dia={tip_dia}, altitude={altitude}")

#             if thrust is not None:
#                 engine_iter.set_req_thrust(thrust)
#             if speed is not None:
#                 engine_iter.set_req_flightSpeed(speed)
#             if tip_dia is not None:
#                 engine_iter.set_tip_dia(tip_dia)
#             if altitude is not None:
#                 engine_iter.set_req_altitude(altitude)

#             engine_motor_options = engine_iter.create_engine_motor_variants("Engine variants")
#             serialized_data = serialize(engine_motor_options)

#             print("Engine options generated and serialized.")
#             return "Engine options generated successfully!", serialized_data

#         except Exception as e:
#             print(f"⚠️ Error in generate_engine: {e}")
#             return f"⚠️ Error: {str(e)}", None

#     @app.callback(
#         Output('plot-output', 'figure'),
#         Input('plot-selector', 'value'),
#         State('engine-data-store', 'data')
#     )
#     def show_plot(plot_type, data):
#         if not plot_type or not data:
#             return go.Figure()

#         try:
#             engine_motor_options = deserialize(data)

#             if plot_type == 'fst':
#                 return engine_motor_options.figure_flightSpeed_thrust()
#             elif plot_type == 'fsp':
#                 return engine_motor_options.figure_flightSpeed_power()
#             elif plot_type == 'fsrpm':
#                 return engine_motor_options.figure_flightSpeed_rpm()
#         except Exception as e:
#             print(f"⚠️ Error in show_plot: {e}")
        
#         return go.Figure()



from dash import Output, Input, State
import plotly.graph_objs as go
import pickle
import base64
from bladerunner.engine import engine_iterations

design_params = "design_params.json"
engine_iter = engine_iterations.EngineIterations(design_params)

# Helpers for (de)serialization
def serialize(obj):
    return base64.b64encode(pickle.dumps(obj)).decode()

def deserialize(s):
    return pickle.loads(base64.b64decode(s.encode()))

def register_callbacks(app):

    @app.callback(
        Output('message', 'children'),
        Output('engine-data-store', 'data'),
        Input('generate-button', 'n_clicks'),
        State('thrust', 'value'),
        State('flight-speed', 'value'),
        State('tip-dia', 'value'),
        State('altitude', 'value'),
    )
    def generate_engine(n_clicks, thrust, speed, tip_dia, altitude):
        if n_clicks == 0:
            return "", None

        try:
            print(f"Input values: thrust={thrust}, speed={speed}, tip_dia={tip_dia}, altitude={altitude}")

            if thrust is not None:
                engine_iter.set_req_thrust(thrust)
            if speed is not None:
                engine_iter.set_req_flightSpeed(speed)
            if tip_dia is not None:
                engine_iter.set_tip_dia(tip_dia)
            if altitude is not None:
                engine_iter.set_req_altitude(altitude)

            engine_motor_options = engine_iter.create_engine_motor_variants("Engine variants")
            serialized_data = serialize(engine_motor_options)

            print("Engine options generated and serialized.")
            return "Engine options generated successfully!", serialized_data

        except Exception as e:
            print(f"⚠️ Error in generate_engine: {e}")
            return f"⚠️ Error: {str(e)}", None

    @app.callback(
        Output('plot-output', 'figure'),
        Input('plot-selector', 'value'),
        State('engine-data-store', 'data')
    )
    def show_plot(plot_type, data):
        if not plot_type or not data:
            return go.Figure()

        try:
            engine_motor_options = deserialize(data)

            if plot_type == 'fst':
                return engine_motor_options.figure_flightSpeed_thrust()
            elif plot_type == 'fsp':
                return engine_motor_options.figure_flightSpeed_power()
            elif plot_type == 'fsrpm':
                return engine_motor_options.figure_flightSpeed_rpm()
        except Exception as e:
            print(f"⚠️ Error in show_plot: {e}")
        
        return go.Figure()
