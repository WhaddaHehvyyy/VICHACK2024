"""
Avoid warnings relevant to GPU usage & providers 
"""
import warnings 
warnings.filterwarnings("ignore", message="Specified provider 'OpenVINOExecutionProvider' is not in available provider names")
warnings.filterwarnings("ignore", category=UserWarning)
"""
START:
"""
import roboflow as rf 
from inference import get_model
import cv2 
import supervision as sv 
import numpy as np 
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


# returns array of all the frames within the video 
frames = sv.get_video_frames_generator(source_path="/Users/natha/Desktop/YT2MP$/Boxing1.mp4") 

boxing_detector = get_model(model_id = "boxer-detection-n1rbc/3")
image = cv2.imread("/Users/natha/Desktop/YT2MP$/Boxing9.jpg")

results = boxing_detector.infer(image)[0]
detections = sv.Detections.from_inference(results)

box_annotator = sv.BoxAnnotator()
annotated_image = box_annotator.annotate(scene= image, detections=detections)

cv2.imwrite("annotated_image.jpg", annotated_image)
cv2.imshow("Annotated Image", annotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()