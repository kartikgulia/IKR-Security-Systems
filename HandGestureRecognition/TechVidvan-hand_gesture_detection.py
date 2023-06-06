# TechVidvan hand Gesture Recognizer

# import necessary packages
import time
import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
import os
from google.cloud import pubsub_v1
from tensorflow.keras.models import load_model
from google.cloud import bigquery
import RPi.GPIO as GPIO

# initialize mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

# Load the gesture recognizer model
model = load_model('mp_hand_gesture')

# Load class names
f = open('gesture.names', 'r')
classNames = f.read().split('\n')
f.close()
print(classNames)


# Initialize the webcam
cap = cv2.VideoCapture(0)

#CREDENTIALS
credentials_path = r'/home/ryan/Downloads/ikr-security-db-388523-766e28bbf69c.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

#ryans fix
client = bigquery.Client()


# kartik's fix maybe 
publisher = pubsub_v1.PublisherClient()
topic_name = 'projects/ikr-security-db-388523/topics/testing_topic'.format(
    project_id=os.getenv('GOOGLE_CLOUD_PROJECT'),
    topic='testing_topic',
)
#publisher.create_topic(name=topic_name)

#setting up pin 12 as output
#echo 79 > /sys/class/gpio/export
#echo out >/sys/class/gpio/gpio79/direction
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)

#haha even funnier ryan code for connecting two nanos LOL
roundabout = 40


while True:
    # Read each frame from the webcam
    _, frame = cap.read()

    x, y, c = frame.shape

    # Flip the frame vertically
    frame = cv2.flip(frame, 1)
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Get hand landmark prediction
    result = hands.process(framergb)

    #print(result)
    
    className = ''
    

    # post process the result
    if result.multi_hand_landmarks:
        landmarks = []
        for handslms in result.multi_hand_landmarks:
            for lm in handslms.landmark:
                # print(id, lm)
                lmx = int(lm.x * x)
                lmy = int(lm.y * y)

                landmarks.append([lmx, lmy])

            # Drawing landmarks on frames
            mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

            # Predict gesture
            prediction = model.predict([landmarks])
            #print(prediction)
            classID = np.argmax(prediction)
            className = classNames[classID]

    # show the prediction on the frame
    cv2.putText(frame, className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                   1, (0,0,255), 2, cv2.LINE_AA)

    # print the gesture in terminal (our edits)
    print(className)
    
    # connect to pubsub
   # publisher = pubsub_v1.PublisherClient()
   # topic_name = 'projects/ikr-security-db-388523/topics/testing_topic'.format(
   #         project_id=os.getenv('GOOGLE_CLOUD_PROJECT'),
   #         topic='testing_topic',
   # )

    # actually publishing the info 
   # publisher.create_topic(name=topic_name)
    
    # isean hope
    data_str= f"{str(className)}. "
    #data = data_str.encode("utf-8")

    # back to kartik lol
   #publisher.create_topic(name=topic_name)
   #future = publisher.publish(topic_name, str(className), spam='eggs')
    future = publisher.publish(topic_name, data=data_str.encode('utf-8'))
    future.result()
    
    #query data
  #  for row in query_job:
   #     records = [dict(row) for row in query_job]
    #    print(str(records))

   # query_job = client.query(QUERY)
   # rows = query_job.reload()
   # print(rows)
   # for row in rows:
   #     print(row.name)

    sql_query = "SELECT CASE WHEN DATA LIKE '%peace%' THEN 'true' END AS is_equal_to_peace FROM `authentication.test123`"

    query_job = client.query(sql_query)
    #if query_job.state == 'DONE':
        #if query_job.result() != 'NULL':
            #data = query_job.result()
            #if data == true:
                #rows = list(data)
            #print(rows)
            #print("\n")
          #print(query_job.result())
    # isean's version of the above
   # publisher = pubsub_v1.PublisherClient()

    #haha funny ryan code lol
    if className == 'peace':
        print('signal: true')
        if roundabout > 0:
            GPIO.output(18, GPIO.HIGH)
            print('people count: okay')
        else:
            print('people count: not okay')
       # GPIO.output(18, GPIO.HIGH)
        #echo 1 > /sys/class/gpio/gpio79/value
    else:
        print('signal: false')
        if roundabout > 0:
            print('people count: okay')
        else:
            print('people count: not okay')
        GPIO.output(18,GPIO.LOW)
        #echo 0 > /sys/class/gpio/gpio79/value
    
    #part 2 of funny connecting nano code by ryan LOL
    roundabout = roundabout-1

    # Show the final output (okay back to their code)
    cv2.imshow("Output", frame) 

    if cv2.waitKey(1) == ord('q'):
        break

# release the webcam and destroy all active windows
cap.release()

cv2.destroyAllWindows()
