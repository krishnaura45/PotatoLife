# Potato Life : API based Potato Disease Classification 

'Potato Life' is an automated project for farmers for timely and accurate diagnosis of diseases in potato leaves.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)
![Optimized For Accuracy](https://img.shields.io/badge/Metric--Focused-Accuracy-yellowgreen?style=for-the-badge)


### INTRODUCTION
- Potato(Solanum tuberosum) is the fourth-most important staple crop in the world.   
- Potato crops are susceptible to multiple diseases.
- This project identifies and classifies major potato diseases.
- By accurately diagnosing diseases, farmers can apply targeted treatments, reducing the need for excessive pesticide use.

![image](https://github.com/KD-Blitz/PotatoLife/assets/118080140/d31e8943-9e5d-4524-b15a-141998694ce5)

### RELATED WORKS
![image](https://github.com/KD-Blitz/PotatoLife/assets/118080140/2cf49bb6-f4da-4457-b784-1043395233ba)

### PROBLEM DEFINITION
- Potato crops are highly vulnerable to diseases, impacting yield and food security.
- Early, precise disease detection is crucial for efficient management and reduced crop loss.
- Traditional diagnosis methods are slow and unsuitable for large-scale agriculture.
- There's a need for automated, scalable solutions for disease detection.

### METHODOLOGY
##### Step 1: Dataset Preparation
- We have used publicly available ‘PlantVillage’ dataset.
- It includes 1000 images each of ‘Early Blight’ and ‘Late Blight’, along with 152 ‘Healthy’ leaf images, totalling 2152 potato leaf images.

![image](https://github.com/KD-Blitz/PotatoLife/assets/118080140/2414525f-a9c3-41ce-a4dd-168be5820b1c)

##### Step 2: Data Preprocessing
- Data Batch Loading: Into 68 batches of 32 images each
- Data Partitioning: Into train, test and validation sub-datasets
- Data Resizing: To a constant size of 256 X 256
- Data Rescaling: Divided pixel intensities of each image by 255.
- Data Augmentation: As random flipping and random rotation

##### Step 3: Model Building
- CNN Model Architecture: Consisted of-
  1) 6 convolutional layers with 3X3 kernel size and ReLU activation function
  2) 6 max-pooling layers 
  3) A dropout layer
  4) A flattening layer
  5) 2 dense layers
- Compiled the model using Adam optimizer, Sparse categorical cross-entropy loss and Accuracy metric.
- The training process involved 50 epochs, with each epoch comprising 54 steps.

##### Step 4: FastAPI Integration
- Implementation details:
  1) Endpoint Creation: We developed a FastAPI server on localhost, listening on port 8000.
  2) Endpoint Routes: We implemented the Post / Predict API route to facilitate interaction with the model. This route accepts an uploaded potato leaf image, processes it, feeds it into our trained model, and returns the predicted class (early blight, late blight, or healthy) along with a confidence score.
- Image Processing and Model Prediction
Upon receiving an image upload through the /predict endpoint, FastAPI performs the following steps:
  1) Image Conversion: FastAPI converts the uploaded image into a NumPy array.
  2) Tensor Conversion: The NumPy array is further transformed into a tensor, which is compatible with our trained model.
  3) Model Prediction: The tensorized image is passed through the model, and the model predicts the disease class and provides a confidence score for the prediction.

- Response Format

![image](https://github.com/KD-Blitz/PotatoLife/assets/118080140/f0d62ccf-869c-4c59-a73b-b9d561cb1255)

### PROPOSED FRAMEWORK
![image](https://github.com/KD-Blitz/PotatoLife/assets/118080140/c0f5cebc-a9d3-4870-81b5-8abd416b20c0)

### RESULTS
- Upon completion of training, our model achieved a remarkable test accuracy of 98.83%, demonstrating the model's efficacy in classifying potato leaves into three categories: early blight, late blight, and healthy conditions.
![image](https://github.com/KD-Blitz/PotatoLife/assets/118080140/d4a77d8c-e31f-41f6-b59f-0fce38e70c95)

- Alongside, we have the model’s predictions on a sample of test images, where:
   “Actual" represents the true class.
   “Predicted represents the predicted class.
   “Confidence" is the confidence score associated with the prediction, which reflects upon the reliability of the model's decision.
![image](https://github.com/KD-Blitz/PotatoLife/assets/118080140/199ceb75-6bd8-4ab3-9f99-a75f5dcf4ddb)

- FastAPI Working
![image](https://github.com/KD-Blitz/PotatoLife/assets/118080140/7798b018-aef7-4b34-b0af-c73fae61cb29)
![image](https://github.com/KD-Blitz/PotatoLife/assets/118080140/2443d89d-37e4-423d-af33-11f3fdf755dd)


- Postman software interacting with the model via API request and giving prediction result as a json response for a sample leaf image.
![image](https://github.com/KD-Blitz/PotatoLife/assets/118080140/349da7dc-f94e-420e-a528-1d6fbfc74606)

### CONCLUSIONS/OUTCOMES
- Robust Data Preparation: Data preprocessing, involving batch loading, resizing, rescaling, and data augmentation, enhanced dataset quality and diversity.
- Model achieved an impressive 98.83% test accuracy, showcasing deep learning's effectiveness in disease classification.
- User-Friendly Implementation: FastAPI and Postman software facilitated user-friendly disease classification, empowering farmers and experts for on-the-spot diagnosis.
- Effectively address timely and accurate detection of potato leaf diseases.

### FUTURE SCOPE/PLANS
- Create a mobile app
- Emphasize on the need for FastAPI server security, including measures like authentication and authorization to safeguard model and user data.
- Implement monitoring and logging tools to track server performance, usage, and errors. 
- Implement a feedback mechanism to collect user input for ongoing model enhancements.

### REFERENCES
1) S. Biswas, B. Jagyasi, B. P. Singh and M. Lal, "Severity identification of Potato Late Blight disease from crop images captured under uncontrolled environment," 2014 IEEE Canada International Humanitarian Technology Conference - (IHTC), Montreal, QC, Canada, 2014, pp. 1-5, doi: 10.1109/IHTC.2014.7147519.
2) G. Athanikar and P. Badar, “Potato Leaf Diseases Detection and Classification System”, IJCSMC, Vol. 5, Issue. 2, February 2016, pg.76 – 88
3) Rabbia Mahum, Haris Munir, Zaib-Un-Nisa Mughal, Muhammad Awais, Falak Sher Khan, Muhammad Saqlain, Saipunidzam Mahamad & Iskander Tlili. A novel framework for potato leaf disease detection using an efficient deep learning model, Human and Ecological Risk Assessment: An International Journal; 2022.
4) Chakraborty KK, Mukherjee R, Chakroborty C, Bora K. Automated recognition of optical image based potato leaf blight diseases using deep learning. Physiological and Molecular Plant Pathology. 2022;117:101781

### Group/Team
Krishna Dubey (DL and Backend), Pankaj Kumar Giri (Backend)
