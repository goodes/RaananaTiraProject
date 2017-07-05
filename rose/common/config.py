import os

# Networking

game_port = 8888
web_port = 8880

# Server

game_rate = 1.0
game_duration = 60

# Client

frame_rate = 30
number_of_cars = 4
car_jitter = 10
play_sound = True

# Matrix

matrix_height = 9
matrix_width = 6
row_height = 65
cell_width = 130
left_margin = 95
top_margin = 10

# Dashboard

dashboard_height = 150
dashboard_top_margin = 35

# Finish line

# How many seconds to display the finish line (max matrix_height)
finish_line_duration = 5

# Window

background_color = 0, 0, 0
window_caption = "ROSE Project"
windows_width = cell_width*(matrix_width+1)
windows_height = (row_height * matrix_height)+dashboard_height
window_size = windows_width, windows_height

# Files
res_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../res'))

obstacles_glob = os.path.join(res_path, 'obstacles/obstacle*.png')
road_glob = os.path.join(res_path, 'bg/bg*.png')
cars_dir = os.path.join(res_path, 'cars')
dashboard_png = os.path.join(res_path, 'dashboard/dashboard.png')
splash_png = os.path.join(res_path, 'splash/splash_screen.png')
finish_line_png = os.path.join(res_path, 'end/final_flag.png')
soundfile = os.path.join(res_path, 'soundtrack/Nyan_Cat.ogg')

# Player
max_players = 2
cells_per_player = matrix_width / max_players

# Score Points
score_pickup_penguin = 10
score_move_forward = 10
score_move_backward = -10
score_jump = 5
score_brake = 4
