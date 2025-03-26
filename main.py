import imageio
import numpy as np
from PIL import Image, ImageDraw

# Parameters
width, height = 400, 70  # Size of the image
bar_height = 40  # Height of the progress bar
frames = 46 # Number of frames (smoothness)
duration = 10 # Total duration in seconds
frame_duration = duration / frames  # Time per frame
print(frame_duration)
gif_frames = []

for i in range(frames + 1):
    img = Image.new("RGBA", (width, height), "white")
    draw = ImageDraw.Draw(img, "RGBA")
    
    # Background Bar
    draw.rectangle([50, (height - bar_height) // 2, width - 50, (height + bar_height) // 2], outline="black", width=3)
    
    # Progress Fill with Reduced Opacity
    progress = (width - 100) * (i / frames)
    draw.rectangle([50, (height - bar_height) // 2, 50 + progress, (height + bar_height) // 2], fill=(135, 110, 204))  # Blue with 50% opacity
    
    gif_frames.append(np.array(img.convert("RGB")))

# Save GIF
imageio.mimsave("progress_bar_training.gif", gif_frames, duration=frame_duration, loop = 0)