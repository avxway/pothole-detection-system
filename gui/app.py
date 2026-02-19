import tkinter as tk
import matplotlib.pyplot as plt
import cv2

from detection.model import load_model
from utils.file_handler import upload_file

from processing.enhancement import enhance
from processing.restoration import restore
from processing.morphology import apply_morphology
from processing.segmentation import segment

from detection.image_detect import detect_image
from detection.video_detect import detect_video
from detection.camera_detect import detect_camera


class PotholeDetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pothole Detection")

        self.model = load_model()
        self.file_path=None
        self.file_type=None
        self.image=None

        tk.Button(root,text="Upload Image/Video",command=self.upload).pack(pady=10)
        tk.Button(root,text="Enhancement",command=self.show_enhance).pack(pady=10)
        tk.Button(root,text="Restoration",command=self.show_restore).pack(pady=10)
        tk.Button(root,text="Morphological Processing",command=self.show_morph).pack(pady=10)
        tk.Button(root,text="Segmentation",command=self.show_segment).pack(pady=10)
        tk.Button(root,text="Detected Potholes (Image)",command=self.show_detect_image).pack(pady=10)
        tk.Button(root,text="Detected Potholes (Video)",command=self.show_detect_video).pack(pady=10)
        tk.Button(root,text="Start Live Camera",command=self.show_camera).pack(pady=10)

    def upload(self):
        self.file_path,self.file_type,self.image = upload_file()

    def display(self,img,title="Result"):
        if len(img.shape)==2:
            plt.imshow(img,cmap='gray')
        else:
            plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
        plt.title(title)
        plt.axis("off")
        plt.show()

    def show_enhance(self):
        if self.image is not None:
            self.display(enhance(self.image),"Enhanced")

    def show_restore(self):
        if self.image is not None:
            self.display(restore(self.image),"Restored")

    def show_morph(self):
        if self.image is not None:
            self.display(apply_morphology(self.image),"Morphology")

    def show_segment(self):
        if self.image is not None:
            self.display(segment(self.image),"Segmented")

    def show_detect_image(self):
        if self.image is not None:
            out=detect_image(self.model,self.image)
            self.display(out,"Detected Potholes")

    def show_detect_video(self):
        if self.file_type=="video":
            detect_video(self.model,self.file_path)

    def show_camera(self):
        detect_camera(self.model)
