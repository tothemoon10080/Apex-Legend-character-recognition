import os
import torch
import torch.cuda as cuda
from ultralytics import YOLO
from multiprocessing import freeze_support

if __name__ == '__main__':
    freeze_support()
    os.environ['KMP_DUPLICATE_LIB_OK']='TRUE'#OpenMP允许多个运行时库的副本存在

    if cuda.is_available():
        device = torch.device("cuda")  # 将设备设置为CUDA设备
        print("CUDA可用")
    else:
        device = torch.device("cpu")   # 如果CUDA不可用，则将设备设置为CPU
        print("CUDA不可用")

    device='cuda'
    data_path='v1.v2i.yolov8/data.yaml'
    model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)

    # Train the model

    model.train(data=data_path, epochs=25, imgsz=800)