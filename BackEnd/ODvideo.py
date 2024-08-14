from inference import InferencePipeline
from inference.core.interfaces.camera.entities import VideoFrame
import cv2
import supervision as sv
import os
print(os.path.exists("Boxing1.mp4"))



label_annotator = sv.LabelAnnotator()
box_annotator = sv.BoxAnnotator()

def my_custom_sink(predictions: dict, video_frame: VideoFrame):
    # get the text labels for each prediction
    labels = [p["class"] for p in predictions["predictions"]]
    # load our predictions into the Supervision Detections api
    detections = sv.Detections.from_inference(predictions)
    # annotate the frame using our supervision annotator, the video_frame, the predictions (as supervision Detections), and the prediction labels
    image = label_annotator.annotate(
        scene=video_frame.image.copy(), detections=detections, labels=labels
    )
    image = box_annotator.annotate(image, detections=detections)
    # display the annotated image
    cv2.imshow("Predictions", image)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        pipeline.stop()
        cv2.destroyAllWindows()
        return

pipeline = InferencePipeline.init(
    model_id="boxer-detection-n1rbc/3",
    video_reference="BackEnd/Boxing1.mp4",
    on_prediction=my_custom_sink, 
    confidence= 0.60
)

pipeline.start()
pipeline.join()
cv2.destroyAllWindows()