'''Use tkinter to draw an image of the Japanese cartoon character
"Doraemon".
Author: Kameron Squire
'''

import tkinter as tk


def main():
    # The width and height of the scene window.
    width = 800
    height = 500 

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    #draws landscape in background
    draw_sky(canvas, 0, 0)
    draw_grass(canvas, 0, 301, 5)
    draw_moon(canvas, 100, 50)
    draw_fence(canvas, 0, 350, 20)

    #draws the birds using two arches each
    draw_bird(canvas, 350, 150)
    draw_bird(canvas, 300, 150)
    draw_bird(canvas, 425, 250, scale=.5)
    draw_bird(canvas, 400, 250, scale=.5)
    draw_bird(canvas, 430, 175, scale=.75)
    draw_bird(canvas, 468, 175, scale=.75)

    #draws single cloud using variously placed ovals
    draw_cloud(canvas, 600, 50)
    draw_cloud(canvas, 530, 70)
    draw_cloud(canvas, 620, 70, scale=1.5)
    draw_cloud(canvas, 560, 90, scale=1.5)

    #draws Doraemon peaking in the window
    draw_doraemon_head(canvas, 200, 285)
    draw_doraemon_face(canvas, 240, 360)
    draw_doraemon_eye(canvas, 320, 320)
    draw_doraemon_eye(canvas, 400, 320)
    draw_doraemon_pupil(canvas, 375, 375)
    draw_doraemon_pupil(canvas, 410, 375)
    draw_doraemon_face(canvas, 100, 460, scale=.2)
    draw_doraemon_face(canvas, 630, 460, scale=.2)
    draw_doraemon_nose(canvas, 385, 400)
    draw_doraemon_nose_shine(canvas, 390, 407)
    draw_doraemon_nose_line(canvas, 397, 435)
    draw_doraemon_whiskers(canvas) 

    #draws window sill and shutters in the foreground
    draw_window(canvas, 0, 480)
    draw_window_shutter(canvas, 0, 0, 40)
    draw_window_shutter(canvas, 749, 0, 40)

    #grid used to accurately place lines
    # draw_grid(canvas, scene_left, scene_top, scene_right, scene_bottom, 100) 




#Draws temporary grid to accurately place other objects
def draw_grid(canvas, left, top, right, bottom, grid_spacing):
    
    text_horizontal_margin = 20
    text_vertical_margin = 10
    # Draw horizontal lines
    for i in range(top, bottom, grid_spacing):
        canvas.create_line(left, i, right, i)
        canvas.create_text(left + text_horizontal_margin, i + text_vertical_margin, text=f'{i}')

    #Draw vertical lines
    for i in range(left, right, grid_spacing):
        canvas.create_line(i, top, i, bottom)
        canvas.create_text(i, top + text_vertical_margin, text=f'{i}')

def draw_moon(canvas, moon_left, moon_top):
    moon_width = 100
    moon_height = 100
    moon_right = moon_left + moon_width
    moon_bottom = moon_top + moon_height

    canvas.create_oval(moon_left, moon_top, moon_right, moon_bottom, fill='goldenrod2', width=False)

def draw_sky(canvas, sky_left, sky_top):
    sky_width = 799
    sky_height = 300
    sky_right = sky_left + sky_width
    sky_bottom = sky_top + sky_height

    canvas.create_rectangle(sky_left, sky_top, sky_right, sky_bottom, fill='midnightBlue')

def draw_grass(canvas, grass_left, grass_top, grass_spacing):
    grass_width = 799
    grass_height = 299
    grass_right = grass_left + grass_width
    grass_bottom = grass_top + grass_height

    canvas.create_rectangle(grass_left, grass_top, grass_right, grass_bottom, fill='darkGreen')

    for i in range(grass_left, grass_right, grass_spacing):
        canvas.create_line(i, grass_top, i, grass_bottom, fill='forestGreen')

def draw_cloud(canvas, cloud_left, cloud_top, scale=1):
    cloud_width = 100 * scale
    cloud_height = 45 * scale
    cloud_right = cloud_left + cloud_width
    cloud_bottom = cloud_top + cloud_height

    canvas.create_oval(cloud_left, cloud_top, cloud_right, cloud_bottom, fill='gray34', width=False)

def draw_fence(canvas, fence_left, fence_top, fence_spacing):
    fence_width = 799
    fence_height = 75
    fence_right = fence_left + fence_width
    fence_bottom = fence_top + fence_height

    canvas.create_rectangle(fence_left, fence_top, fence_right, fence_bottom, fill='white')

    for i in range(fence_left, fence_right, fence_spacing):
        canvas.create_rectangle(i, fence_top, i, fence_bottom, fill='forestGreen')

def draw_bird(canvas, bird_left, bird_top, scale=1):
    bird_width = 50 * scale
    bird_height = 20 * scale
    bird_right = bird_left + bird_width
    bird_bottom = bird_top + bird_height

    canvas.create_arc(bird_left, bird_top, bird_right, bird_bottom, width=3, style=tk.ARC, extent=180) 

def draw_window_shutter(canvas, window_shutter_left, window_shutter_top, window_shutter_spacing):
    window_shutter_width = 50
    window_shutter_height = 499
    window_shutter_right = window_shutter_left + window_shutter_width
    window_shutter_bottom = window_shutter_top + window_shutter_height  
        
    canvas.create_rectangle(window_shutter_left, window_shutter_top, window_shutter_right, window_shutter_bottom, fill='brown4')

    for i in range(window_shutter_top, window_shutter_bottom, window_shutter_spacing):
        canvas.create_line(window_shutter_left, i, window_shutter_right, i)

def draw_window(canvas, window_left, window_top):
    window_width = 799
    window_height = 20
    window_right = window_left + window_width
    window_bottom = window_top + window_height

    canvas.create_rectangle(window_left, window_top, window_right, window_bottom, width = 3, fill='ivory3')

#The following functions work together to create Doraemon from
# the Japanese television show by the same name.
def draw_doraemon_head(canvas, head_left, head_top):
    head_width = 400
    head_height = 400
    head_right = head_left + head_width
    head_bottom = head_top + head_height

    canvas.create_arc(head_left, head_top, head_right, head_bottom, width=10, style=tk.CHORD, fill='DodgerBlue2', extent=180)

def draw_doraemon_face(canvas, face_left, face_top, scale=1):
    face_width = 320 * scale
    face_height = 250 *scale
    face_right = face_left + face_width
    face_bottom = face_top + face_height

    canvas.create_arc(face_left, face_top, face_right, face_bottom, width=10, style=tk.CHORD, fill='white', extent=180)

def draw_doraemon_eye(canvas, eye_left, eye_top):
    eye_width = 80
    eye_height = 100
    eye_right = eye_left + eye_width
    eye_bottom = eye_top + eye_height

    canvas.create_oval(eye_left, eye_top, eye_right, eye_bottom, width=5, fill='white')


def draw_doraemon_pupil(canvas, pupil_left, pupil_top):

    pupil_width = 15
    pupil_height = 20
    pupil_right = pupil_left + pupil_width
    pupil_bottom = pupil_top + pupil_height

    canvas.create_oval(pupil_left, pupil_top, pupil_right, pupil_bottom, fill='black')

def draw_doraemon_nose(canvas, nose_left, nose_top):
    nose_width = 30
    nose_height = 20
    nose_right = nose_left + nose_width
    nose_bottom = nose_right + nose_height

    canvas.create_oval(nose_left, nose_top, nose_right, nose_bottom, width=4, fill='red2')
    
def draw_doraemon_nose_shine(canvas, nose_left, nose_top):
    nose_width = 10
    nose_height = 17
    nose_right = nose_left + nose_width
    nose_bottom = nose_right + nose_height

    canvas.create_oval(nose_left, nose_top, nose_right, nose_bottom, width=False, fill='white')

def draw_doraemon_nose_line(canvas, nose_left, nose_top):
    nose_width = 5
    nose_height = 65
    nose_right = nose_left + nose_width
    nose_bottom = nose_right + nose_height

    canvas.create_rectangle(nose_left, nose_top, nose_right,nose_bottom, fill='black')

def draw_doraemon_whiskers(canvas):
    canvas.create_line(275, 400, 339, 425, width=5)
    canvas.create_line(270, 425, 335, 440, width=5)
    canvas.create_line(260, 455, 335, 450, width=5.5)
    canvas.create_line(520, 400, 450, 425, width=5)
    canvas.create_line(513, 425, 460, 440, width=5)
    canvas.create_line(520, 453, 458, 451, width=5.5)




# Call the main function so that
# this program will start executing.
main()