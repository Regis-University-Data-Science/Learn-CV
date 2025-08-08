import cv2
import os
from matplotlib import pyplot as plt
from IPython.display import HTML
from IPython.display import Video
def orient_frame(frame, mode="none"):
    """
    Rotate or flip a frame based on mode.
    
    mode options:
      - "none"        -> no change
      - "90cw"        -> rotate 90° clockwise
      - "90ccw"       -> rotate 90° counter-clockwise
      - "180"         -> rotate 180°
      - "flip_h"      -> horizontal flip
      - "flip_v"      -> vertical flip
    """
    if mode == "90cw":
        return cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    elif mode == "90ccw":
        return cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    elif mode == "180":
        return cv2.rotate(frame, cv2.ROTATE_180)
    elif mode == "flip_h":
        return cv2.flip(frame, 1)
    elif mode == "flip_v":
        return cv2.flip(frame, 0)
    elif mode == "none":
        return frame
    else:
        raise ValueError(f"Unknown mode: {mode}")

def show_first_frame(video_path, rotation_mode="none"):
    """
    Opens a video, grabs the first frame, applies rotation/flip,
    and displays it.
    """
    cap = cv2.VideoCapture(video_path)
    ret, frame = cap.read()
    cap.release()

    if not ret:
        print("Error: Could not read first frame.")
        return

    frame = orient_frame(frame, rotation_mode)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    plt.imshow(frame_rgb)
    plt.title(f"First Frame ({rotation_mode})")
    plt.axis("off")
    plt.show()
    
    
    
def play_video(video_path, width=640, height=360):
    return Video(video_path, width=640, height=360)


