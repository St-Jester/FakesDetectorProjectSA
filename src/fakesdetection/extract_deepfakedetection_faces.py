# from PIL import Image
# import face_recognition
# import time
# import os
#
# def extract_faces_dfd(img):
#     image = face_recognition.load_image_file(img)
#     dir_save = "/content/drive/My Drive/FakeImageDetector/data/manipulated_sequences/DeepFakeDetection/c23/faces/"
#     head, tail = os.path.split(img)
#     face_locations = face_recognition.face_locations(image)
#
#     if len(face_locations) == 1:
#         top, right, bottom, left = face_locations[0]
#         face_image = image[top:bottom, left:right]
#         pil_image = Image.fromarray(face_image)
#         pil_img_name = dir_save + tail + ".jpg"
#         pil_image = pil_image.save(pil_img_name)
#
#
#
# start_time = time.time()
# directory = "/content/drive/My Drive/FakeImageDetector/data/manipulated_sequences/DeepFakeDetection/c23/images/"
# n = 0
# for img in os.listdir(directory):
#     n += 1
#     img_name = img
#     path_img = os.path.join(directory, img)
#     if os.path.isdir(path_img) or (path_img == directory + "/" '.DS_Store'):
#         continue
#     extract_faces_dfd(path_img)
#
# print(n)
# print("--- %s seconds ---" % (time.time() - start_time))
