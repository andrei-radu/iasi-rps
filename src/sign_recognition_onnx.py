import numpy as np
import onnxruntime as ort


class HandSignRecognizer:
    def __init__(self):
        self.targets = {
            1: "call",
            2: "dislike",
            3: "fist",
            4: "four",
            5: "like",
            6: "mute",
            7: "ok",
            8: "one",
            9: "palm",
            10: "peace",
            11: "rock",
            12: "stop",
            13: "stop inverted",
            14: "three",
            15: "two up",
            16: "two up inverted",
            17: "three2",
            18: "peace inverted",
            19: "no gesture",
        }

        self.model = self.__get_model()
        self.input_name = self.model.get_inputs()[0].name
        self.output_name = self.model.get_outputs()[0].name
        

    def __get_model(self, path='models/MobileNetV3FF_small.onnx', num_classes=18):
        provider = ['CPUExecutionProvider']
        ort_session = ort.InferenceSession(path, providers=provider)
        return ort_session
    
    
    def predict(self, x: np.ndarray):
        x = x.astype(np.float32)
        x = np.expand_dims(x, axis=0)
        output = self.model.run([self.output_name], {self.input_name: x})
        return output
    
    
    def __call__(self, x: np.ndarray):
        logits = self.predict(x)[0]
        class_ = np.argmax(logits)
        return self.targets[class_]
    
    
    












if __name__ == '__main__':
    model = HandSignRecognizer()
    img = np.random.rand(3, 224, 224)
    output = model.predict(img)
    
    print(output)
    