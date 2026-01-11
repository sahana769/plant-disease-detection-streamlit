# 🌿 Plant Disease Detection System

A **Deep Learning-based Web App** to detect plant diseases from leaf images.  
Built with **TensorFlow**, **Streamlit**, and **Python**.  

This app can predict whether a plant leaf is **Healthy** or **Unhealthy**, and if unhealthy, it will tell you the **type of disease**.  

---

## **Features**

- Upload a leaf image (`jpg`, `jpeg`, `png`)  
- Detect if the plant is **Healthy ✅** or **Unhealthy ❌**  
- Identify the **disease name** (if any)  
- Show **confidence score**  
- User-friendly **Streamlit web interface**  

---

## **Demo**

| Upload Image | Prediction |
|--------------|------------|
| ![sample_leaf](demo/sample_leaf.jpg) | Status: Unhealthy ❌ <br> Disease: Apple - Apple Scab <br> Confidence: 92.34% |

---

## **Technologies Used**

- **Python 3.11**  
- **TensorFlow 2.19** – for the deep learning model  
- **Streamlit** – for the web interface  
- **PIL / Pillow** – for image processing  
- **NumPy** – for numerical operations  

---

## **Dataset**

- [PlantVillage Dataset](https://www.kaggle.com/datasets/emmarex/plantdisease)  
- 43,456 images of 38 classes of plant leaves  
- Includes both **healthy** and **diseased** leaves  

---

## **Installation / Run Locally**

1. **Clone the repository**

```bash
git clone https://github.com/your-username/plant-disease-detection-streamlit.git
cd plant-disease-detection-streamlit
