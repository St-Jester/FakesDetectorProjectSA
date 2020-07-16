import os
import unittest
from src.fakesdetection import video_to_images


class FileTestCase(unittest.TestCase):
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

    def testWrongFilename(self):
        filepath = "wrong"
        with self.assertRaises(SystemExit) as cm:
            video_to_images.video_to_images(filepath)
        the_exception = cm.exception
        video_to_images.clear_faces()
        self.assertEqual(the_exception.code, f"File not found {filepath}")

    def testOkFile(self):
        filepath = "D:/UCU/000.mp4"
        res = video_to_images.video_to_images(filepath)
        video_to_images.clear_faces()
        self.assertEqual(1, res)

    def testKNNModelExists(self):
        model = "../models/all_faces_knn.pickle"
        self.assertEqual(True, os.path.exists(model))

    def testLGBMModelExists(self):
        model = "../models/lgbm_all_updated.pickle"
        self.assertEqual(True, os.path.exists(model))

    def testPCAModelExists(self):
        model = "../models/pca550.joblib"
        self.assertEqual(True, os.path.exists(model))

    def testfacesfolderModelExists(self):
        project_path, file = os.path.split(os.path.dirname(os.path.abspath(__file__)))
        final_path = project_path.replace("\\", "/")
        final_path = final_path + '/src/fakesdetection/test_images/faces/'
        self.assertEqual(True, os.path.isdir(final_path))

    def testtest_imagesfolderModelExists(self):
        project_path, file = os.path.split(os.path.dirname(os.path.abspath(__file__)))
        final_path = project_path.replace("\\", "/")

        final_path = final_path + '/src/fakesdetection/test_images/'
        print(final_path)

        self.assertEqual(True, os.path.isdir(final_path))

    def testemptyfaces(self):
        project_path, file = os.path.split(os.path.dirname(os.path.abspath(__file__)))
        final_path = project_path.replace("\\", "/")
        final_path = final_path + '/src/fakesdetection/test_images/faces'
        self.assertEqual(0, len(os.listdir(final_path)))


if __name__ == '__main__':
    unittest.main()
