import pickle

import cv2
import face_recognition
import numpy as np
from joblib import load
import os

bb_dimensions = (40, 40)


def get_bounding_box(data):
    min_x = min(data, key=lambda t: t[0])[0]
    max_x = max(data, key=lambda t: t[0])[0]
    min_y = min(data, key=lambda t: t[1])[1]
    max_y = max(data, key=lambda t: t[1])[1]

    offset_x = int((bb_dimensions[0] - (max_x - min_x)) / 2.0)
    offset_y = int((bb_dimensions[1] - (max_y - min_y)) / 2.0)

    bb_tl = (min_x - offset_x, min_y - offset_y)
    bb_bl = (min_x - offset_x, max_y + offset_y)
    bb_tr = (max_x + offset_x, min_y - offset_y)
    bb_br = (max_x + offset_x, max_y + offset_y)

    return [bb_tl, bb_tr, bb_br, bb_bl]


def get_pixels(target_image, bb):
    top_left = bb[0]
    pixels = np.zeros((bb_dimensions[0], bb_dimensions[1], 3), dtype=np.uint8)

    for i in range(bb_dimensions[0]):
        for j in range(bb_dimensions[1]):
            new_top_left_y = top_left[1] + j
            new_top_left_x = top_left[0] + i

            if new_top_left_y > 127:
                new_top_left_y = 127
            if new_top_left_x > 127:
                new_top_left_x = 127
            pixels[j, i, :] = target_image[new_top_left_y, new_top_left_x, :]
    return pixels


def get_feature_vector(image):
    face_landmarks = face_recognition.face_landmarks(image)

    if len(face_landmarks) == 0:
        return []
    face_landmarks = face_recognition.face_landmarks(image)[0]

    eyel = get_pixels(image, get_bounding_box(face_landmarks['left_eye']))

    # print('eyel')
    eyer = get_pixels(image, get_bounding_box(face_landmarks['right_eye']))
    # print('eyer')
    nose = get_pixels(image, get_bounding_box(face_landmarks['nose_bridge'] + face_landmarks['nose_tip']))
    # print('nose')
    lips = get_pixels(image, get_bounding_box(face_landmarks['top_lip'] + face_landmarks['bottom_lip']))
    # print('lips')
    feature_vector = np.concatenate((eyel.ravel(), eyer.ravel(), nose.ravel(), lips.ravel()))
    return feature_vector


def get_feature_array_from_image_list(imgpathlist):
    images_resized = []
    features_all = []
    img = imgpathlist

    img_cv2 = cv2.imread(img)[..., ::-1]

    img_cv2_res = cv2.resize(img_cv2, (128, 128), interpolation=cv2.INTER_AREA)

    feature_vector = get_feature_vector(img_cv2_res)
    features_all.append(feature_vector)
    return np.asarray(features_all)


def extract_model(img_path):
    file_path = "../models/all_faces_knn.pickle"

    infile = open(file_path, 'rb')
    model = pickle.load(infile)
    infile.close()

    if os.path.exists(img_path):
        f_array = get_feature_array_from_image_list(img_path)
    else:
        raise SystemExit(f"File not found {img_path}")

    pca_dict = load("../models/pca550.joblib")
    new_data_pca = pca_dict.transform(f_array)

    prediction = model.predict(new_data_pca)
    print(prediction)
