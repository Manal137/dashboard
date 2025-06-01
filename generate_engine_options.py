
# Import Statements
from engine import engine_iterations


# Function to promt a menu and select an option
def run_selection(prompt, options):
    items = len(options) + 1
    while True:
        try:
            selection = int(input(prompt))
            if selection > 0 and selection <= items:
                if selection != items: # last item is exit
                    options[str(selection)]()
                break
            else:
                print('Enter an integer between 1 to {}'.format(items))
        except ValueError:
            print('Enter an integer')

"""
Each menu is defined with the following steps:
    1. Define the menu prompt
        This will be a string which will be prompted to the user to select an option in the menu
    2. Define functions in the menu options
        Menu options in step 3 will have a number of functions
        Each function is defined here
    3. Define menu options
        This will define a dictionary with keys 1, 2, etc and values as functions defined in step 2
"""

# START MENU
# ----------

START_MENU_PROMPT = """
START MENU
----------
1) Specify engine requirements
2) Generate plots
3) Export data
4) Exit

Enter your choice: """

# Function in START menu
def engine_requirements():
    run_selection(REQUIREMENTS_MENU_PROMPT, REQUIREMENTS_MENU_OPTIONS)

def generate_plots():
    run_selection(PLOTS_MENU_PROMPT, PLOTS_MENU_OPTIONS)

def export_data():
    pass

START_MENU_OPTIONS = {
    "1": engine_requirements,
    "2": generate_plots,
    "3": export_data
    }


# REQUIREMENTS MENU
# -----------------

# Option 1 in START MENU
REQUIREMENTS_MENU_PROMPT = """
REQUIREMENTS MENU
-----------------
1) Show current requirements
2) Modify thrust
3) Modify flight speed
4) Modify rotor tip ida
5) Modify altitude
6) Generate engine options
7) Start Menu
8) Exit

Enter your choice:  """

# Functions for the requirements menu
def show_requirements():
    thrust = engine_iter.get_req_thrust()
    print(f"Thrust Required = {thrust} N")
    flightSpeed = engine_iter.get_req_flightSpeed()
    print(f"Flight speed = {flightSpeed} m/s^2")
    tipDia = engine_iter.get_tipDia()
    print(f"Rotor tip dia = {tipDia} m")
    altitude = engine_iter.get_req_altitude()
    print(f"Altitude = {altitude} m")
    engine_requirements()

def modify_thrust():
    thrust = float(input("Enter required thrust in N : "))
    engine_iter.set_req_thrust(thrust)
    engine_iter.set_oper_thrust(thrust)
    engine_requirements()

def modify_flightSpeed():
    flightSpeed = float(input("Enter required flight speed in m/s : "))
    engine_iter.set_req_flightSpeed(flightSpeed)
    engine_iter.set_oper_flightSpeed(flightSpeed)
    engine_requirements()

def modify_tipDia():
    tipDia = float(input("Enter tip diameter in m : "))
    engine_iter.set_tip_dia(tipDia)
    engine_requirements()

def modify_altitude():
    altitude = float(input("Enter required altitude in m : "))
    engine_iter.set_req_altitude(altitude)
    engine_iter.set_oper_altitude(altitude)
    engine_requirements()

def generate_engines():
    global engine_motor_options
    engine_motor_options = engine_iter.create_engine_motor_variants("Engine variants")
    engine_requirements()

def reqs_to_start_menu():
    run_selection(START_MENU_PROMPT, START_MENU_OPTIONS)


REQUIREMENTS_MENU_OPTIONS = {
    "1": show_requirements,
    "2": modify_thrust,
    "3": modify_flightSpeed,
    "4": modify_tipDia,
    "5": modify_altitude,
    "6": generate_engines,
    "7": reqs_to_start_menu
    }


# PLOTS MENUE
# -----------

# Option 2 in START MENU
PLOTS_MENU_PROMPT = """
PLOT MENU
-----------------
1) Flight Speev Vs Thrust
2) Flight Speed Vs Power
3) Flight Speed Vs RPM
4) Start Menu
5) Exit

Enter your choice:  """

# Functions for the plot menue
def plot_flightSpeed_thrust():
    fig = engine_motor_options.figure_flightSpeed_thrust()
    fig.show()
    generate_plots()

def plot_flightSpeed_power():
    fig = engine_motor_options.figure_flightSpeed_power()
    fig.show()
    generate_plots()

def plot_flightSpeed_rpm():
    fig = engine_motor_options.figure_flightSpeed_rpm()
    fig.show()
    generate_plots()

def plots_to_start_menu():
    run_selection(START_MENU_PROMPT, START_MENU_OPTIONS)
    

PLOTS_MENU_OPTIONS = {
    "1": plot_flightSpeed_thrust,
    "2": plot_flightSpeed_power,
    "3": plot_flightSpeed_rpm,
    "4": plots_to_start_menu
    }



def start_menu():    
    # Run START menu
    run_selection(START_MENU_PROMPT, START_MENU_OPTIONS)

design_params = "design_params.json"
engine_iter = engine_iterations.EngineIterations(design_params)

start_menu()