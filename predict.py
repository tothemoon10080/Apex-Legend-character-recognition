from ultralytics import YOLO

device = 'cuda'
video_path = 'Path_to_video'
model = YOLO("runs//detect//train//weights//best.pt")  # 加载模型
model.predict(source=video_path,save=True,conf=0.35,save_txt=False)  # 预测视频

