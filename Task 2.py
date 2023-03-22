import argparse
import cv2
import time


def parse_arguments():
    ap = argparse.ArgumentParser()

    ap.add_argument("-v", "--video", type=str, required=True,
                    help="path to input video file")
    ap.add_argument("-fps", "--processing_fps", type=int, required=True,
                    help="number of processing frames per second")
    args = vars(ap.parse_args())

    return args


if __name__ == '__main__':

    args = parse_arguments()

    # Set local variables
    video_name = args["video"]
    processing_fps = args["processing_fps"]


    video = cv2.VideoCapture(video_name)
    video_fps = video.get(cv2.CAP_PROP_FPS)


    if video_fps > processing_fps:
        skip_rate = round(video_fps / processing_fps)
    else:
        skip_rate = 1

    frame_no = 0
    processed_frame_count = 0

    total_grab_time = 0
    total_retrieve_time = 0

    start = time.time()

    while True:
        tmp = time.time()
        ret = video.grab()
        total_grab_time += (time.time() - tmp)
        if not ret:
            break

        frame_no += 1

        if (frame_no % skip_rate == 0):
            processed_frame_count += 1

            tmp = time.time()
            status, frame = video.retrieve()
            total_retrieve_time += (time.time() - tmp)


            frame = cv2.resize(frame, (1280, 720))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow("Frame", frame)
            cv2.waitKey(1)

    video.release()

    end = time.time()
