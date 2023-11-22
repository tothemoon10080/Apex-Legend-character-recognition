# Apex-Legend-character-recognition (Apex Legend 角色识别)

Using YOLOv8 to train an Apex Legend character recognition model (使用 YOLOv8 训练 Apex Legend 角色识别模型)

1. **Download and Install Dependencies**
   - Clone this repository:
     ```     
     pip clone https://github.com/tothemoon10080/Apex-Legend-character-recognition.git
     ```
   - Then run the following command in the root directory of the repository to install all the necessary libraries:
     ```     
     pip install -r requirements.txt
     ```

2. **Download Dataset**
   - [Image Dataset](https://universe.roboflow.com/online-resource-2/v1-jx7pl/dataset/2)

3. **Download Pretrained Model**
   - Use Yolo's built-in [yolov8n.pt](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt)

4. **Train the Model**
   - `train.py` uses the training code from the YOLOv8 documentation, just modify the dataset path, pretrained model path, and the path for saving the trained model.

5. **Use the Model for Prediction**
   - `predict.py` uses the prediction code from the YOLOv8 documentation, just modify the pretrained model path and the path for the prediction image.

<details>
   <summary>中文描述</summary>
   
   1. **下载并安装依赖**
      - 克隆此仓库:
        ```     
        pip clone https://github.com/tothemoon10080/Apex-Legend-character-recognition.git
        ```
      - 并在仓库根目录下运行以下命令来安装所有必需的库：
        ```     
        pip install -r requirements.txt
        ```
   
   2. **下载数据集**
      - [Image Dataset](https://universe.roboflow.com/online-resource-2/v1-jx7pl/dataset/2)
   
   3. **下载预训练模型**
      - 这里使用 Yolo 自带的 [yolov8n.pt](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt)
   
   4. **训练模型**
      - `train.py` 使用了 YOLOv8 文档中的训练代码，只需修改数据集路径、预训练模型路径及训练后模型的保存路径。
   
   5. **使用模型进行预测**
      - `predict.py` 使用了 YOLOv8 文档中的预测代码，只需修改预训练模型路径及预测图片路径。
</details>
