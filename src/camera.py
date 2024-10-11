import cv2


class Camera:
    def __init__(self) -> None:
        self.cam = cv2.VideoCapture(0)
        self.cam.set(cv2.CAP_PROP_FPS, 24)
        _, _ = self.cam.read()  # activate camera

    def get_image(self):
        _, img = self.cam.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return img
    
    def close_camera(self):
        self.cam.release


if __name__ == '__main__':
    import time
    import matplotlib.pyplot as plt
    
    camera = Camera()

    time.sleep(1.5)  # stabilize sensor

    image = camera.get_image()

    print(f"Image shape is {image.shape}")

    plt.figure()
    plt.imshow(image)
    plt.show()