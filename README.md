# 🛣️ Pothole Detection System using YOLOv8 and Digital Image Processing

## 📌 Project Overview

This project detects potholes from images, videos, and live camera feed using a hybrid approach:

* Digital Image Processing pipeline (Enhancement → Restoration → Morphology → Segmentation)
* Deep Learning detection using YOLOv8
* GUI built with Tkinter for interactive testing

The system allows users to visualize each processing phase and run real-time pothole detection.

---

## 🎯 Features

* Upload image or video for testing
* Step-by-step DIP processing visualization
* Pothole detection on:

  * Images
  * Videos
  * Live camera feed
* YOLOv8 custom trained model support
* Modular project architecture

---

## 🧠 Model Training (Google Colab)

The YOLOv8 model was trained on Google Colab using a custom pothole dataset.

Training steps included:

* Dataset preparation in YOLO format
* Training using Ultralytics YOLOv8
* Exporting best weights (`best.pt`)
* Downloading the model for local inference

After training, place the model file here:

```
pothole-detection/models/best.pt
```

---

## 📂 Project Structure

```
pothole-detection/
│
├── main.py
├── gui/
├── processing/
├── detection/
├── utils/
├── models/
│   └── best.pt
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```
git clone [<your-repo-link>](https://github.com/avxway/pothole-detection-system)
cd pothole-detection
```

### 2️⃣ Create virtual environment (recommended)

```
python -m venv venv
```

Activate it:

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Running the Application

```
python main.py
```

The GUI window will open.

---

## 🖥️ How to Use

1. Click **Upload Image/Video**
2. Try DIP steps individually
3. Run detection on image/video/live camera
4. Press **q** to stop video/camera detection

---

## 🧰 Technologies Used

* Python
* OpenCV
* NumPy
* Matplotlib
* Tkinter
* Ultralytics YOLOv8
* PyTorch

---

## 📊 Future Improvements

* Mobile deployment
* Web-based dashboard
* Road severity estimation
* Automatic pothole reporting system

---

## 👨‍💻 Author

**Anmol Verma**

---

## 📜 License

This project is for academic and research purposes.
