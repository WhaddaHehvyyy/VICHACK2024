
from inference import InferencePipeline
from inference.core.interfaces.camera.entities import VideoFrame
import cv2
import supervision as sv

import os
print(os.path.exists("Boxing1.mp4"))

def prediction_function(predictions: dict, video_frame: VideoFrame) -> None: 
    labels = sv.LabelAnnotator()
    boxes = sv.BoxAnnotator() 

    # Extract predictions
    detections = sv.Detections.from_inference(predictions)

    # Ensure the number of classes and confidence scores matches the number of detections
    classes = [p["class"] for p in predictions["predictions"]]
    confidence = [p["confidence"] for p in predictions["predictions"]]

    for 

    # Annotate the image with labels and confidence
    image = labels.annotate(scene=video_frame.image, detections=detections, labels=classes)
    image2 = boxes.annotate(image, detections=detections)
    
    cv2.imshow("Predictions", image2)
    cv2.waitKey(0)


pipeline = InferencePipeline.init(
    model_id="boxer-detection-n1rbc/3",
    video_reference="VIDEO/Boxing1.mp4",
    on_prediction=prediction_function, 
    confidence= 0.60
)

pipeline.start()
pipeline.join()
cv2.destroyAllWindows()


    
