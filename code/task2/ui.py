from ipywidgets import widgets, Layout
from IPython.display import display, HTML
from random import random
from labels import labels

image_widget = widgets.Image(format='jpeg', width=300, height=300)
label_widget = widgets.Dropdown(options=labels, value=1,description='Label')
distance_widget = widgets.IntSlider(description='Distance', min=40, max=4000, orientation='horizontal')
obj_widget = widgets.Image(format='jpeg', width=300, height=300)
target_widget = widgets.Image(format='jpeg', width=300, height=300)
similarity_widget = widgets.FloatSlider(description='Similarity', min=0, max=1, orientation='horizontal')
obstacle_slider = widgets.IntSlider(description='Obstacle', min=40, max=4000, orientation='horizontal')


start_button = widgets.Button(
    description='start',
    disabled=False,
    layout=Layout(flex='1 1 auto', width='auto'),
    button_style='success', # 'success', 'info', 'warning', 'danger' or ''
)

track_button = widgets.Button(
    description='track',
    disabled=False,
    layout=Layout(flex='1 1 auto', width='auto'),
    button_style='info', # 'success', 'info', 'warning', 'danger' or ''
)

stop_button = widgets.Button(
    description='stop',
    disabled=False,
    layout=Layout(flex='1 1 auto', width='auto'),
    button_style='danger', # 'success', 'info', 'warning', 'danger' or ''
)
