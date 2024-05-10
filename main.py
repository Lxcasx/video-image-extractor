import shutil
import uuid
import cv2
import json
import os
from path import OUT_PATH, TMP_PATH, ensure_out_path, ensure_tmp_path

def extract_images(video, video_capture):
    name = video['qualified_name']
    print("Extracting images from video: " + name)

    ensure_tmp_path(video)

    rand_id = uuid.uuid4()
    frame_count = 0
    while True:
        # Read the next frame from the video. If we're at the end, break
        ret, frame = video_capture.read()
        if not ret:
            break

        # Write the image to the 'tmp' directory
        cv2.imwrite(f'{TMP_PATH}/{name}/frame_{rand_id}_{frame_count}.jpg', frame)

        frame_count += 1

def filter_images(video):
    ensure_out_path(video)

    name = video['qualified_name']
    # Get list of all files in source_folder
    source_folder = f'{TMP_PATH}/{name}'
    files = os.listdir(source_folder)
    x = video['frame_interval']

    # Filter out every x image
    images_to_move = files[::x]

    print(f"Saving {len(images_to_move)} of source {source_folder}")

    # Move every x image to destination_folder
    destination_folder = f'{OUT_PATH}/{name}'
    for image in images_to_move:
        shutil.move(os.path.join(source_folder, image), os.path.join(destination_folder, image))

    shutil.rmtree(source_folder)

def run():
    videos_json = open('videos.json', 'r')
    videos = json.load(videos_json)

    for video in videos:
        path = "data/" + video['file']
        print("Processing video: " + path)
        cap = cv2.VideoCapture(path)
        extract_images(video, cap)
        filter_images(video)

if __name__ == "__main__":
    run()