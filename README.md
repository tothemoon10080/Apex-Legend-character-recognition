# Apex-Legend-character-recognition

使用 YOLOv8 训练 Apex Legend 角色识别模型

1. **下载并安装 YOLOv8 及其依赖库**
   - 克隆此仓库，并在仓库根目录下运行以下命令来安装所有必需的库：
     ```
     pip install -r requirements.txt
     ```

2. **下载 Apex Legend 角色识别数据集 v1**
   - [Image Dataset](https://universe.roboflow.com/online-resource-2/v1-jx7pl/dataset/2)

3. **下载 Apex Legend 角色识别预训练模型**
   - 这里使用 Yolo 自带的 `yolov8n.pt`

4. **训练模型**
   - `train.py` 使用了 YOLOv8 文档中的训练代码，只需修改数据集路径、预训练模型路径及训练后模型的保存路径。

5. **使用模型进行预测**
   - `predict.py` 使用了 YOLOv8 文档中的预测代码，只需修改预训练模型路径及预测图片路径。
