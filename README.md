# ILLEAGL FISHING DETECTION

The aim of this project to detect the illegal fishing vessels and and their activities using our training model .The several parameters are to be in consideration on training model is vessels locaton, vessels Id ,Country, Date and Time and Boundaries like Distance from port and shore.The predicated result shown in web application which is developed using  flask framework and pyhon language. 

Data Set : 
we have take  reference from 'Global fishing watch' which is provide Automatic Identification System or AIS data set 

src https://globalfishingwatch.org/data-download/
 
 1.The data we used to training the model is :
 Src https://drive.google.com/drive/folders/18ADPPy8ZEGQx-FJcWHtgTEdqJQZQl-wv?usp=sharing

 2.The predicted data is :
 src https://drive.google.com/drive/folders/18u1V3JwJKQjeiz5Gwk9VRHHuNmH-TaY6?usp=sharing
 
 
Train The Model :
  
    cd dashboard
    pip install -r requirements.txt
    python train.py
 
Run Dashboard locally : 
    
    cd dashboard
    python app.py

Note: Upload the training file in the dashboard directry and also upload trollers.csv and predictions.csv file in the data.
