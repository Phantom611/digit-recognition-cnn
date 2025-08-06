# 🧠 Handwritten Digit Recognition using CNN

This is a deep learning project that uses a Convolutional Neural Network (CNN) to recognize handwritten digits from the popular MNIST dataset. The model is trained using TensorFlow/Keras and deployed using Streamlit.

🔗 **Live App**: [Click here to try it!](https://your-streamlit-app-link)  
📁 **Dataset**: [MNIST Digits Dataset](http://yann.lecun.com/exdb/mnist/)

---

## 🚀 Features

- 🎯 Predicts handwritten digits (0 to 9) with high accuracy
- 📷 Accepts image uploads of 28x28 grayscale digits
- 💻 Built with TensorFlow, Streamlit, and Python
- 🌐 Deployed on Streamlit Cloud (free and accessible)

---

## 🛠️ Tech Stack

- Python
- TensorFlow / Keras
- NumPy
- Streamlit
- PIL (Pillow)

---

## 📦 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/Phantom611/digit-recognition-cnn.git
cd digit-recognition-cnn
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App

```bash
streamlit run digit_app.py
```
---

# 🧠 Model Architecture

- Conv2D with 32 filters (3x3), ReLU
- MaxPooling2D
- Conv2D with 64 filters (3x3), ReLU
- MaxPooling2D
- Flatten + Dense(128) with ReLU
- Dropout(0.3)
- Dense(10) with Softmax activation

---

🧪 Results

| Metric          | Value |
| --------------- | ----- |
| Training Acc.   | \~99% |
| Validation Acc. | \~98% |
| Test Acc.       | \~98% |

---

📬 Contact

Created by Mayank Pahade
Feel free to reach out or fork this project to improve it!
