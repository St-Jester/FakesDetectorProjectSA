import getopt
import sys

import fakesdetection.video_to_images
from fakesdetection import video_to_images

import fakesdetection.model_extractor
from fakesdetection import model_extractor
import fakesdetection.lgbm_model
from fakesdetection import lgbm_model

USAGE = 'usage: detector.py -i <infile> -m <model> \nprovide absolute path to file \npossible models name: lgbm, knn'
USAGE_MODELS = 'Wrong Model name\npossible models name: lgbm, knn'


def main(argv):
    # "/src/fakesdetection/test_images/faces/000_003.mp4_image4.jpg"
    # todo add cmd args
    # video_to_images.video_to_images(argv)
    # help input model

    try:
        opts, args = getopt.getopt(argv, "hi:m:", ["infile=", "model="])
        if not opts or len(opts) != 2:
            raise SystemExit(USAGE)

    except getopt.GetoptError:
        print(USAGE)
        sys.exit(2)
    try:
        operands = [int(arg) for arg in args]
    except ValueError:
        raise SystemExit(USAGE)

    both = 0
    filepath = ''
    model_choice = ''

    possible_models = ['lgbm', 'knn']
    for opt, opt_value in opts:
        if opt == '-h':
            print(USAGE)
            sys.exit()
        elif opt in ("-i", "--infile"):
            both += 1
            filepath = opt_value
        #   todo: do stuf
        elif opt in ("-m", "--model"):
            both += 1
            model_choice = opt_value
            if model_choice not in possible_models:
                raise SystemExit(USAGE_MODELS)

        if both == 2:
            video_to_images.video_to_images(filepath)
            image_path = video_to_images.get_path()

            if model_choice == 'knn':
                model_extractor.extract_model(image_path)
            if model_choice == 'lgbm':
                lgbm_model.extract_model(image_path)

    video_to_images.clear_faces()
if __name__ == "__main__":
    main(sys.argv[1:])
