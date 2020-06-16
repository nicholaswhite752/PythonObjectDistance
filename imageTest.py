from imageai.Detection import ObjectDetection
import os
import tensorflow.compat.v1 as tf

# Object Baseline for 2 feet
xLen2 = 929
yLen2 = 316

# gets path
execution_path = os.getcwd()
# creates object detector
detector = ObjectDetection()

# sets model type
detector.setModelTypeAsRetinaNet()
# sets specific model
detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "ImageYouWantToFindDistanceFor.jpg"), output_image_path=os.path.join(execution_path , "ImageResult.jpg"))

for eachObject in detections:
    print(eachObject["name"], " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"])
    xLength = eachObject["box_points"][2] - eachObject["box_points"][0]
    yLength = eachObject["box_points"][3] - eachObject["box_points"][1]

    xProp = xLength / xLen2
    yProp = yLength / yLen2

    propAverage = (xProp + yProp) / 2

    # 2.23 is accurate because I took the photo one foot off the ground, so diagonal
    # Answer was 3.57 when it should of been 4.12, not extremely accurate for phase 1, but good start
    distApprox = 2 / propAverage

    print("Approx Distance:", distApprox)


#Test From 2 feet
#929 316

#Test From 4 feet
#590 194