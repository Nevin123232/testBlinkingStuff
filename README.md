# 👁️ Blink-to-Action Prototype

A lightweight, high-performance computer vision tool designed to detect eye blinks from a live webcam feed and trigger a system-level action (Spacebar press). 

This project was specifically optimized to run on **Python 3.12** using **Haar Cascade Classifiers**, bypassing the dependency conflicts often found in newer MediaPipe or Dlib builds.



## 🛠️ Installation & Setup

Follow these steps to create an isolated environment and get the script running on your machine.

### 1. Create a Virtual Environment
Using a virtual environment ensures that the project dependencies don't interfere with your other Python work.
```powershell
# Create the environment folder
python -m venv blink_env

# Activate the environment
.\blink_env\Scripts\activate

2. Install Dependencies
Once the environment is active, install the required libraries:

pip install -r requirements.txt
