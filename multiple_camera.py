import cv2
from imutils.video import FileVideoStream
from imutils.video import WebcamVideoStream
import time


def multi_camera(list_of_camera):

	camera = []

	for i in list_of_camera:
		vid = cv2.VideoCapture(i)
		camera.append(vid)

	num_of_camera = len(camera)

	while True:
		# initialize the list of frames that have been processed
		frames = []
	 
		# loop over the frames and their respective motion detectors
		for stream in camera:
			# read the next frame from the video stream and resize
			# it to have a maximum width of 400 pixels
			ftft, frame = stream.read()
			frame = cv2.resize(frame, (400, 300))
	 
			# convert the frame to grayscale, blur it slightly, update
			# the motion detector
	 
			# we should allow the motion detector to "run" for a bit
			# and accumulate a set of frames to form a nice average
			frames.append(frame)

		for (frame, name) in zip(frames, (str(k) for k in range(len(camera)))):

			cv2.imshow(name, frame)

		if cv2.waitKey(1) & 0xFF == ord('q'):
	            break

	print('chal gaya')
	cv2.destroyAllWindows()
	for j in camera:
		j.release()
	# vid1.stop()
	# vid2.stop()


def main():
	start = time.time()
	list_of_camera = [0, 1, 2, 'rtsp://admin:mintm1234@192.168.0.64:554/Streaming/Channels/101']
	multi_camera(list_of_camera)	
	duration = time.time() - start
	print('duration:' + str(duration))


if __name__ == '__main__':
	main()