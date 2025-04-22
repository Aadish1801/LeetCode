#  Facial Expression Recognition with CNN

##  Problem Statement
The goal of this project is to build a deep learning model that can recognize facial expressions from images. By using a Convolutional Neural Network (CNN), we aim to classify grayscale face images into one of seven emotional categories.

##  Objective
Classify facial expressions into the following categories:
- Angry
- Disgust
- Fear
- Happy
- Sad
- Surprise
- Neutral

##  Dataset
- **Name:** FER-2013 (Facial Expression Recognition 2013)
- **Link:** [https://www.kaggle.com/datasets/msambare/fer2013](https://www.kaggle.com/datasets/msambare/fer2013)
- **Format:** CSV with 48x48 grayscale image pixels and emotion labels
- **Size:** ~35,000 images

##  Techniques Used
- Convolutional Neural Networks (CNN)
- Data normalization
- Model training & evaluation using Keras & TensorFlow
- Confusion matrix and classification report for performance

##  How to Run
1. Open the notebook in Google Colab
2. Upload your Kaggle API key (`kaggle.json`)
3. Run all cells to train and evaluate the model
