"# Apex-Legend-character-recognition" 

使用YOLOv8训练Apex Lengend角色识别模型

1. 下载安装YOLOv8以及其他依赖库 [YOLOv8] (https://pytorch.org/get-started/locally/) [PyTorch] (https://pytorch.org/get-started/locally/) [Nvidia Cuda] (https://developer.nvidia.com/cuda-toolkit-archive)

2. 下载Apex Lengend角色识别数据集 v1 [Image Dataset] (https://universe.roboflow.com/online-resource-2/v1-jx7pl/dataset/2)

3. 下载Apex Lengend角色识别预训练模型 这里使用Yolo自带的yolov8n.pt

4. 训练模型 train.py 使用了YOLOv8文档中的训练代码，只需要修改数据集路径，预训练模型路径，以及训练后模型保存路径即可 

5. 使用模型进行预测 predict.py 使用了YOLOv8文档中的预测代码，只需要修改预训练模型路径，以及预测图片路径即可
