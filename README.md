# Rock-Paper-Scisor on Jetson Nano

This project represents one of the **IASI** laboratories (ro: _Inteligență artificială pentru sisteme integrate_, en: _Artificial Inteligence for Integrated Systems_), for the **BIOSINF** (ro: _Tehnologii multimedia în aplicații de biometrie și securitatea informației_ , en: _Multimedia Technologies in Biometrics and Information Security Applications_) master program.

## Developing
This repo is under development. Please come back later.


## Description
To be added

## To Do
- [ ] add mediapipe for hand tracking ?
- [ ] clean the code
- [x] bash script for models download


## Installation

### Check that the camera is working

First, check if the camera is working by running the following command:
```bash
gst-launch-1.0 nvarguscamerasrc ! nvoverlaysink
```

If the camera is working, you should see a window with the camera feed. Press `Ctrl+C` to close the window.

If the camera is not working, make sure the pins are configured correctly. Use the following command to check the pins:
```bash
sudo /opt/nvidia/jetson-io/jetson-io.py
```

### Install PyTorch and Torchvision
To run this project, you need to install PyTorch and Torchvision. You can install them by following the oficial instructions from [here](https://qengineering.eu/install-pytorch-on-jetson-nano.html). This project was tested on PyTorch 1.9.0 and Torchvision 0.10.0, builded from wheel, which are the versions that should be installed.


### Clone the repository
Jetson Nano should already have the git-cli installed. If not, run the following command:
```bash
sudo apt-get install git
```

Then clone the repository:
```bash
git clone https://github.com/andrei-radu/iasi-rps.git
```


### Download the model
Run the following command in the root directory of the project to download the model:
```bash
wget -O models/MobileNetV3FF_small.pth 'https://ctipub-my.sharepoint.com/:u:/g/personal/andrei_radu_danila_stud_etti_upb_ro/EZXgxLpmO7hOt4GqmMwleXQBE509Mq81vP7F6khJg4MgaQ?e=0VA5NQ&download=1'
```

ONNX version of the model can be downloaded with:
```bash
wget -O models/MobileNetV3FF_small.onnx 'https://ctipub-my.sharepoint.com/:u:/g/personal/andrei_radu_danila_stud_etti_upb_ro/EToWxBwWudNGqGjrAGovwNIB9V54-Q7b9UdE1nu62MuEcg?e=hWaclM&download=1'
```



## Acknowledgments
TODO: add github repo for mobilnet

