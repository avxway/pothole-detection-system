from tkinter import filedialog
import cv2

def upload_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files","*.jpg *.png"),("Video Files","*.mp4 *.avi")]
    )

    if not file_path:
        return None, None, None

    if file_path.endswith(('.jpg','.png')):
        image = cv2.imread(file_path)
        return file_path, "image", image

    return file_path, "video", None
