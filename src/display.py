import cv2
import numpy as np
from typing import Union

class Display:
    def __init__(self) -> None:
        """
        Initialize the display object properties. 
        """
        self.pos = (50, 50)
        self.text_options ={
            'fontFace': cv2.FONT_HERSHEY_PLAIN,
            'fontScale': 2,
            'color': (0, 255, 0),
            'thickness': 2,
            'lineType': 2,
        }


    def show(self, image: np.ndarray, text: Union[str, None] = None) -> None:
        """ Display the image with optional text overlay.

        Args:
            image (np.ndarray): Image to display.
            text (str or None, optional): Text to overlay on the image. Defaults to None.
        """
        if text is not None:
            text = text.split('\n')
            for idx, t in enumerate(text):
                text_pos = (self.pos[0], (idx + 1) * self.pos[1])
                image = cv2.putText(image, t, text_pos, **self.text_options)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        cv2.imshow('video-feed', image)
        cv2.waitKey(1)



if __name__ == '__main__':
    from camera import Camera
    
    cam = Camera()
    cam.start()
    
    display = Display()
    
    
    while True:
        img = cam.get_image()
        display.show(img)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break