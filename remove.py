#Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
#python app.py runserver 0.0.0.0:5000
from flask import Flask, render_template, session, request, current_app
from flask_socketio import SocketIO, emit
import numpy as np
from engineio.payload import Payload
import json
from flask_cors import CORS, cross_origin
import time

# motion rec libraries
import tensorflow_hub as hub
from moRec import select_ML_model

#
# #Socket app
Payload.max_decode_packets = 2048

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
cors = CORS(app, resources={"*": {"origins": "localhost:4200"}})
socketio = SocketIO(app, cors_allowed_origins="*"
                    # ,
                    # engineio_logger=True,
                    # logger=True
                    )


@app.route('/<user_id>', methods=['POST', 'GET'])
def index(user_id):
    return render_template('index.html')


@socketio.on('auth')
def user_auth(user_id, user_exercise_id, exerciseId, model_name):
    try:
        print(f"User ID auth socket: {user_id}")
        print(f"UserExcercise ID: {user_exercise_id}")
        print(f"User exerciseId: {exerciseId}")
        print(f"Model name: {model_name}")
        # ML modelio pavadinimas
        exercise_id = int(exerciseId)
        user_id_str = str(user_id)
        user_exercise_id = int(user_exercise_id)
        user_exercise_id = 4
        # ML modelio pasirinkimas
        session[user_id_str] = select_ML_model(exercise_id, int(user_id), int(user_exercise_id), model_name)
        print(f"AUTH sesion object {session[user_id_str]}")
    except e:
        print(e)


@socketio.on('pose')
def get_pose(json_str, user_id, height, width):
    try:
        #print(json_str)
        user_id_str = str(user_id)
        if json_str is not None:
      #      print(f"User ID Pose socket: {user_id}")
            user_id_str = str(user_id)
            json_dumped = json.dumps(json_str)
            json_data = json.loads(json_dumped)
 #           arr = np.array([[[[row['y'], row['x'], row['score']] for row in json_data['keypoints']]]]) / [int(height), int(width), 1]
            arr = np.array([[[[row['y'], row['x'], row['score']] for row in json_data['keypoints']]]]) / [480, 640, 1]

            start = time.time()
            label, prob = session[user_id_str].get_continuous_prediction(arr)
            end = time.time()
            result_str = f"""
                    {{
                    "kinectCounterStatus": {session[user_id_str].start_exercise},
                    "currentPose": "{session[user_id_str].pose_dict[label]}",
                    "prob": {prob:.4f},
                    "squatCount": {session[user_id_str].squat_count},
                    "pushUpCount": {session[user_id_str].push_up_count},
                    "crunchCount": {session[user_id_str].crunch_count},
                    "currentPlankTime": {session[user_id_str].elbow_plank_current_time:.4f},
                    "plankCount": {session[user_id_str].elbow_plank_count},
                    "plankTotalTime": {session[user_id_str].elbow_plank_total_time:.4f},
                    "kinectPracticeEndStatus" : {session[user_id_str].end_exercise},
                    "kinectUploadedExerciseSQL" : {session[user_id_str].uploaded_exercise_to_sql},
                    "kinectExcerciseDataSetID" : {session[user_id_str].data_set_id},
                    "timeToStartExcercise" : {session[user_id_str].time_left_start:.4f},
                    "timeToEndExcercise" : {session[user_id_str].time_left_end:.4f},
                    "latency" : {end - start},
                    "standing" : {session[user_id_str].prediction_list[0]:.4f},
                    "squat" : {session[user_id_str].prediction_list[1]:.4f},
                    "push_up_start" : {session[user_id_str].prediction_list[2]:.4f},
                    "push_up_end" : {session[user_id_str].prediction_list[3]:.4f},
                    "elbow_plank" : {session[user_id_str].prediction_list[4]:.4f},
                    "start_end_pos" : {session[user_id_str].prediction_list[5]:.4f},
                    "crunch_start" : {session[user_id_str].prediction_list[6]:.4f},
                    "crunch_end" : {session[user_id_str].prediction_list[7]:.4f},
                    "missingPoints" : "{session[user_id_str].missing_keypoints_str}"
                    # "squatSetProgress" : "{session[user_id_str].squat_current_set} / {session[user_id_str].squat_sets}",
                    # "squatRepProgress" : "{session[user_id_str].squat_current_set_reps} / {session[user_id_str].squat_reps}", 
                    # "pushUpSetProgress" : "{session[user_id_str].push_up_current_set} / {session[user_id_str].push_up_sets}",
                    # "pushUpRepProgress" : "{session[user_id_str].push_up_current_set_reps} / {session[user_id_str].push_up_reps}", 
                    # "crunchSetProgress" : "{session[user_id_str].crunch_current_set} / {session[user_id_str].crunch_sets}",
                    # "crunchRepProgress" : "{session[user_id_str].crunch_current_set_reps} / {session[user_id_str].crunch_reps}",
                    # "elbowPlankSetProgress" : "{session[user_id_str].elbow_plank_current_set} / {session[user_id_str].elbow_plank_sets}",
                    # "elbowPlankRepProgress" : "{session[user_id_str].elbow_plank_current_set_reps:.4f} / {session[user_id_str].elbow_plank_reps}",
                    # "restTimeLeft" : "{session[user_id_str].global_rest_time_amount_left:.4f}"
                    }}
                    """

            return result_str
        return None
    except TypeError as err:
        print(f"ERROR in pose event: {err}")
        test = err

if __name__ == '__main__':
    #socketio.run(app, host="192.168.2.131", port="5006", debug=True)#(local DEV)
    socketio.run(app, host='192.168.3.82', port=5006, debug=True)#(Prod)