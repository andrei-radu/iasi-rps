import time

from src.camera import Camera
from src.display import Display
from src.sign_recognition import HandSignRecognizer
from src.game_logic import RockPaperScisors


if __name__ == '__main__':

    camera = Camera()
    display = Display()
    sign_recog = HandSignRecognizer()
    game = RockPaperScisors()

    last_state = "ok"  # placeholder for last recognized sign
    text = None

    while True:
        img = camera.get_image()
        sign = sign_recog.predict(img)
        
        if sign != last_state:
            last_state = sign

            results = game.round(sign)
            if results is None:
                continue
            
            text = f"Player: {results['player_choice']}\n"
            text += f"Computer: {results['computer_choice']}\n"
            text += f"Winner is {results['who_wins']}\n\n"

        display.show(img, text)
