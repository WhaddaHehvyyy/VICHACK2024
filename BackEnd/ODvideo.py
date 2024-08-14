from inference import InferencePipeline
from inference.core.interfaces.camera.entities import VideoFrame
import cv2
import supervision as sv
import os
import mediapipe as mp

print(os.path.exists("Boxing1.mp4"))

label_annotator = sv.LabelAnnotator()
box_annotator = sv.BoxAnnotator()

# Initialize Mediapipe components
# Initialize Mediapipe components for Pose detection
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

# Initialize the Mediapipe Pose model
pose = mp_pose.Pose(static_image_mode=False, model_complexity=1, enable_segmentation=False, min_detection_confidence=0.5)

def my_custom_sink(predictions: dict, video_frame: VideoFrame):
     # Process the frame with Mediapipe Pose detection
    image_rgb = cv2.cvtColor(video_frame.image, cv2.COLOR_BGR2RGB)
    results = pose.process(image_rgb)

    # Annotate Mediapipe Pose results on the frame
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(
            image=video_frame.image,
            landmark_list=results.pose_landmarks,
            connections=mp_pose.POSE_CONNECTIONS
        )
    
    # get the text labels for each prediction
    # labels = [p["class"] for p in predictions["predictions"]]
    labels = [f"{p['class']} ({p['confidence']:.2f})" for p in predictions["predictions"]]

    confidences = []

    # print(predictions["predictions"])
    for prediction in predictions["predictions"]:
        # print(prediction)
        label = prediction["class"]
        confidence = str(prediction["confidence"])
        confidences.append(confidence)
        x = prediction["x"]
        y = prediction["y"]
        w = prediction["width"]
        h = prediction["height"]
        
        
        # # Print the class label and confidence
        # print(f"Class: {label}, Confidence: {confidence:.2f}, BBox: x={x}, y={y}, w={w}, h={h}")


    # for prediction in predictions["predictions"]:
    #     if prediction["class"]  == "person":
    #         pass

    # load our predictions into the Supervision Detections api
    detections = sv.Detections.from_inference(predictions)
    # annotate the frame using our supervision annotator, the video_frame, the predictions (as supervision Detections), and the prediction labels
    image = label_annotator.annotate(
        scene=video_frame.image.copy(), detections=detections, labels=labels
    )
    image = box_annotator.annotate(image, detections=detections)
    # display the annotated image
    cv2.imshow("Predictions", image)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        pipeline.stop = True

pipeline = InferencePipeline.init(
    model_id="boxer-detection-n1rbc/3",
    video_reference="BackEnd/Boxing1.mp4",
    on_prediction=my_custom_sink, 
    confidence= 0.60
)

pipeline.start()
pipeline.join()
#pipeline join makes sure everything is processed first
cv2.waitKey(0)
cv2.destroyAllWindows()

pose.close()
