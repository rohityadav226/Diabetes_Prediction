# Diabetes Prediction Using Machine Learning - Docker APP

This project pertained to the healthcare industry as real patient data was utilized to manipulate and predict diabetes (yes or no) based on demographics and lab results. Multiple machine learning models were created and tested on validation data. The best performing model was integrated into a web app and connected with a MySQL database. Docker containers were used for integration.
[WebAppLink](http://3.99.163.110:8501/)
# Files
[Dockerfile](https://github.com/rohityadav226/Diabetes_Prediction/blob/master/Dockerfile "Dockerfile")<br>
[classifier.pkl](https://github.com/rohityadav226/Diabetes_Prediction/blob/master/classifier.pkl "classifier.pkl")<br>
[diabetes_app_pkg.yaml](https://github.com/rohityadav226/Diabetes_Prediction/blob/master/diabetes_app_pkg.yaml "diabetes_app_pkg.yaml")<br>
[diabetes_prediction_app.py](https://github.com/rohityadav226/Diabetes_Prediction/blob/master/diabetes_prediction_app.py "diabetes_prediction_app.py")<br>
[requirements.txt](https://github.com/rohityadav226/Diabetes_Prediction/blob/master/requirements.txt "requirements.txt")
# Usage
- Download above mentioned files and place them in one folder. Rename the folder to **docker_app**.
- Run below mentioned Docker Commands to install images and run containers.

Build an image from Docker File.

    docker build -t diabetes_app:1.0 .

 - Create a private repository using AWS ECR.
 - Push the image into your private repository.
 - Change the image link in **diabetes_app_pkg.yaml** to your image link.
 <img width="644" alt="Screenshot 2023-01-12 at 10 54 46 AM" src="https://user-images.githubusercontent.com/90460563/212134972-32b4ccd7-1980-4e84-a381-edceaa4294d5.png">


Run below command to start your containers using .yaml file.<br>

    docker-compose -f diabetes_app_pkg.yaml up -d

Now your app should be up and running. Use below mentioned link to access the app.<br>

    localhost:8501

Data will be stored in mysql database. You can access the data using phpmyadmin. Paste below mentioned link to access phpmyadmin.<br>

    localhost:8081

**username**: root<br>
**password**: password
