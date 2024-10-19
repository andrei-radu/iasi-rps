import numpy as np
import onnxruntime as ort


if __name__ == '__main__':
    
    ort_session = ort.InferenceSession("models/MobileNetV3FF_small.onnx")
    
    input_name = ort_session.get_inputs()[0].name
    output_name = ort_session.get_outputs()[0].name
    
    input = np.random.randn(1, 3, 224, 224).astype(np.float32)
    output = ort_session.run([output_name], {input_name: input})
    
    print(output)