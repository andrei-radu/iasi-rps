import argparse

from src.camera import Camera
from src.display import Display
# from src.sign_recognition import HandSignRecognizer
from src.sign_recognition_onnx import HandSignRecognizer
from src.game_logic import RockPaperScissors


if __name__ == '__main__':

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-p', '--platform', type=str, default='jetson', help='Choose the platform: jetson or desktop')
    args = arg_parser.parse_args()

    camera = Camera(platform=args.platform)
    camera.start()
    display = Display()
    sign_recog = HandSignRecognizer()
    game = RockPaperScissors()

    last_state = "ok"  # placeholder for last recognized sign
    text = None

    frame_counter = 0
    results = {}
    while True:
        img = camera.get_image()
        
        if frame_counter % 10 == 0:
            sign = sign_recog(img)
            
            if sign != last_state:
                last_state = sign
                results = game.round(sign)

        if 'error' in results:
            continue
        
        text = f"Player: {results['player_choice']}\n"
        text += f"Computer: {results['computer_choice']}\n"
        text += f"Winner is {results['who_wins']}\n\n"

        display.show(img, text)
        frame_counter += 1
