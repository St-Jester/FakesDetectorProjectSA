import cv2
from PIL import Image
import face_recognition
import os

image_path = ''


def extract_faces_dfd(img, path):
    image = face_recognition.load_image_file(img)
    head, tail = os.path.split(img)
    face_locations = face_recognition.face_locations(image)

    if len(face_locations) == 1:
        top, right, bottom, left = face_locations[0]
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        pil_img_name = path + tail
        global image_path
        image_path = pil_img_name
        pil_image.save(pil_img_name)


def get_frame(vidcap, sec, vidname, path, count):
    vidcap.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)
    has_frames, image = vidcap.read()

    path_to_save = os.path.basename(os.path.normpath(vidname))
    if has_frames:
        img_path = os.path.join(path, path_to_save + "_image" + str(count) + ".jpg")

        cv2.imwrite(img_path, image)  # save frame as JPG file
        extract_faces_dfd(img_path, path + "faces/")
    return has_frames


def clear_dir(path):
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def video_to_images(absolute_path_to_vid):
    project_path = os.path.dirname(os.path.abspath(__file__))
    project_path = project_path.replace("\\", "/")

    vidname = absolute_path_to_vid
    path_vid = absolute_path_to_vid
    if not os.path.exists(vidname):
        raise SystemExit(f"File not found {vidname}")
    else:
        vidcap = cv2.VideoCapture(path_vid)
        sec = 0
        frameRate = 2
        count = 1
        path = project_path + '/test_images/'
        success = get_frame(vidcap, sec, vidname, path, count)
        while success:
            count = count + 1
            sec = sec + frameRate
            sec = round(sec, 2)
            success = get_frame(vidcap, sec, vidname, path, count)

        folder = project_path + '/test_images/'
        clear_dir(folder)
        return 1


def splitall(path):
    allparts = []
    while 1:
        parts = os.path.split(path)
        if parts[0] == path:  # sentinel for absolute paths
            allparts.insert(0, parts[0])
            break
        elif parts[1] == path:  # sentinel for relative paths
            allparts.insert(0, parts[1])
            break
        else:
            path = parts[0]
            allparts.insert(0, parts[1])
    return allparts


def get_path():
    # get image path
    parts, file = os.path.split(image_path)
    parted = splitall(parts)[-3:]
    final_path = os.path.join(*parted, file)
    final_path = final_path.replace("\\", "/")
    final_path = final_path

    return final_path


def clear_faces():
    project_path = os.path.dirname(os.path.abspath(__file__))
    folder = project_path + '/test_images/faces'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
