# Diabetes Prediction Using Machine Learning - Docker APP

This project pertains to the healthcare industry since we will make use of real patient data to manipulate and predict diabetes (yes or no) based on demographics and lab results. We will be creating multiple machine learning models and will be testing them on validation data. Furthermore, we will integrated the best performing model into a web app and connecting it with mysql Database. We will be using Docker Containers for integration.
[WebAppLink](http://3.140.247.108:8501)
# Files
[Dockerfile](https://github.com/rohityadav226/Diabetes_Prediction/blob/master/Dockerfile "Dockerfile")
[classifier.pkl](https://github.com/rohityadav226/Diabetes_Prediction/blob/master/classifier.pkl "classifier.pkl")
[diabetes_app_pkg.yaml](https://github.com/rohityadav226/Diabetes_Prediction/blob/master/diabetes_app_pkg.yaml "diabetes_app_pkg.yaml")
[diabetes_prediction_app.py](https://github.com/rohityadav226/Diabetes_Prediction/blob/master/diabetes_prediction_app.py "diabetes_prediction_app.py")
[requirements.txt](https://github.com/rohityadav226/Diabetes_Prediction/blob/master/requirements.txt "requirements.txt")
# Usage
- Download above mentioned files and place them in one folder. Rename the folder to **docker_app**.
- Run below mentioned Docker Commands to install images and run containers.

Build an image from Docker File.

    docker build -t diabetes_app:1.0 .

 - Create a private repository using AWS ECR.
 - Push the image into your private repository.
 - Change the image link in **diabetes_app_pkg.yaml** to your image link.

Run below command to start your containers using .yaml file.<br>

    docker-compose -f diabetes_app_pkg.yaml up -d

Now your app should be up and running. Use below mentioned link to access the app.<br>

    localhost:8501

Data will be stored in mysql database. You can access the data using phpmyadmin. Paste below mentioned link to access phpmyadmin.<br>

    localhost:8081

**username**: root<br>
**password**: password
