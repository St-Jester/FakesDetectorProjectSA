This is a Software Architecture for Data Science in Python final project.

I expanded an ML project. That project had a goal of creatning models that can determine if the image is fake.

At this SA project I created a feature, where you can introduce new videos to the model and see if it's fake or not.

This project uses videos and only videos.

What was added to the projects:

1. You can provide a path to the video and choose what model to use. Avaliable models: KNN and LGBM.
2. The video is cropped into several frames.
3. face_recognition library is used to crop a face from the frame.
4. face_recognition also used to create a vector of features, needed for the models.
5. If KNN model is chosen the PCA is also done for feature vector.
6. Chosen model shows the result of prediction
7. tests.


## Some notes 
Please, provide only absolute path ot video.

The video shouldn't be long (or it will take ages to compile)

There are some example videos for you to test the project (those are videos from face_forensics)
Usage:

```
python detector.py -i D:/UCU/000.mp4 -m knn
```