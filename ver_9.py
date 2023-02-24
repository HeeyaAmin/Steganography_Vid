import cv2
import numpy as np

def hide_data(image_path, video_path, output_path):

    # Load the image and the video
    img = cv2.imread(image_path)
    cap = cv2.VideoCapture(video_path)

    # Get the frame dimensions
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS)) #get fps

    # Check if the image can fit into the video
    # img.shape[0] is height, image.shape[1] is width and 3=R,G,B values
    if img.shape[0] * img.shape[1] * 3 > frame_width * frame_height * frame_count:
        raise ValueError("Image too large to hide in video")

    # Convert the image to binary and reshape it
    binary_img = np.unpackbits(img)
    binary_img = np.reshape(binary_img, (-1, 8)) #convert a flat 1D array of binary values into a 2D array where each row contains 8 binary values

    # Iterate through each pixel in the video and hide a bit of the image in it
    i = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
            for row in range(frame_height):
                for col in range(frame_width):
                    if i < binary_img.shape[0]:
                        pixel = frame[row][col]
                        binary_pixel = np.unpackbits(np.array(pixel).astype(np.uint8))
                        binary_pixel[-1] = binary_img[i][-1]
                        pixel = np.packbits(binary_pixel).astype(np.int32)
                        frame[row][col] = pixel
                        i += 1
                else:
                    break
        cv2.imshow('Hidden Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): #this is for termination
            break


    cap.release()
    cv2.destroyAllWindows()

    # Save the modified video to output path
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height), True)
    cap = cv2.VideoCapture(video_path)
    i = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)
        i += 1

    cap.release()
    out.release()
    cv2.destroyAllWindows()


def retrieve_data(video_path, output_path):
    cap = cv2.VideoCapture(video_path)
    binary_img = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        binary_pixel = np.unpackbits(np.array(frame[0][0]).astype(np.uint8))
        binary_img.append(binary_pixel[-1])
    cap.release()

    # Convert the binary string back to an image and save it to output path
    binary_img = np.array(binary_img)
    binary_img = np.packbits(binary_img).astype(np.uint8)
    img = np.reshape(binary_img, binary_img.shape)
    cv2.imwrite(output_path, img)

# hide_data('lemon.png', 'new_vid.mp4', 'output_video.mp4')
retrieve_data('output_video.mp4','retrieved.png')
