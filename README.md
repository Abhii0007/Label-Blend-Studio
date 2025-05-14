# 🧠 LabelBlend v1.1 — Synthetic Image Studio

**LabelBlend** is a powerful desktop application for generating high-quality large amount of synthetic images with annotations. Designed for AI practitioners, computer vision engineers, and researchers, it allows automatic seamless placement over randomized backgrounds to create rich, labeled datasets for model training.

> 🚀 Create multi-class datasets with bounding box or segmentation annotations for AI/ML pipelines in minutes.

---

## ✨ Key Features

- 🎨 **Drag & Drop Studio**: Load cutouts and background images easily.
- 🏷️ **Auto Label Generation**: Creates YOLO-format `.txt` annotations alongside each synthetic image.
- 🔁 **Randomized Augmentation**: Applies rotation, scaling, and random placement.
- 🗂️ **Multi-class Support**: Generate data for multiple object classes simultaneously.
- 📦 **Export-Ready Datasets**: Structured output folder with `images/` and `labels/`.

---

## 📸 Example Output

| Synthetic Image | YOLO Label |
|-----------------|------------|
| ![Example](assets/Image10.png) | `0 0.52 0.55 0.2 0.2` (YOLO format) |

---

🧪 Use Cases and Applications:-
LabelBlend is designed to be a core utility for:
      
      🧠 Training computer vision models (YOLO, SSD, Mask R-CNN, etc.)
      🧬 Creating synthetic data for deep learning pipelines
      🏭 Augmenting data in industrial automation and robotics
      📊 Academic research in AI/ML
      🚗 Datasets for modern agricultural Ai applications,autonomous driving, object detection, or instance segmentation

📌 How to Use:-
1.Load transparent cutout images with class labels.

2.Add background images.
3.Set parameters:-

    a.Number of images to generate
    b.Minimum/maximum size for cutouts
    c.Starting image number

4.Click Generate.
5.Check output/images/ and output/labels/ for results.

📎 Notes
      
      Images are resized and randomly rotated before placement.
      YOLO annotations are normalized (x_center, y_center, width, height).
      You can use the generated dataset directly with YOLOv5, YOLOv8, etc.

## 🛠️ Installation

### 📍 Requirements
- Python 3.10+
- pipenv (Python virtual environment manager)

### 🔧 Setup Instructions


# Clone the repository
[git clone https://github.com/yourusername/LabelBlend.git](https://github.com/Abhii0007/Label-Blend-Studio.git)
    
cd LabelBlend

# Install pipenv if not already installed
pip install pipenv

# Install all dependencies
pipenv install

# Activate virtual environment
pipenv shell

# Run the application
python main.py



🤝 Contributing
    
    Contributions, feedback, and feature requests are welcome! Please open an issue or submit a pull request.

📜 License
        
    This project is licensed under the MIT License. See the LICENSE file for details.

👨‍💻 Author
    
    Developed by Abhishek — Passionate about AI, ML, and building tools that bridge data and models.
