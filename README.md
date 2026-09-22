# YOLOv8 猪脸检测项目

## 项目简介

本项目使用 YOLOv8 目标检测框架，实现猪的自动识别与检测。通过采集猪的图片数据集，使用 Label Studio 进行标注，训练自定义 YOLOv8 模型，最终实现对图片和视频中猪的检测。

## 技术栈

<<<<<<< HEAD
- **检测框架**：YOLOv8（ultralytics）
- **标注工具**：Label Studio
- **编程语言**：Python
- **开发工具**：VS Code

## 项目结构

```
pig_test/
├── pig_dataset/
│   ├── images/
│   │   ├── train/          # 训练集图片（32张）
│   │   └── val/            # 验证集图片（8张）
│   ├── labels/
│   │   ├── train/          # 训练集标注文件
│   │   └── val/            # 验证集标注文件
│   └── data.yaml           # 训练配置文件
├── runs/
│   └── detect/
│       └── train-2/
│           └── weights/
│               └── best.pt # 训练好的模型
├── detect_person.py        # 检测脚本
├── download_pigs.py       # 图片下载脚本
└── split_data.py          # 数据分割脚本
```

## 环境安装

```bash
pip install ultralytics
pip install opencv-python
pip install label-studio
```

## 使用方法

### 1. 训练模型

```bash
yolo train model=yolov8n.pt data=C:/Users/jielun/Desktop/pig_test/pig_dataset/data.yaml epochs=50
```

### 2. 检测图片

```bash
yolo predict model=runs/detect/train-2/weights/best.pt source=test.jpg save=True conf=0.3
```

### 3. 检测视频

```bash
yolo predict model=runs/detect/train-2/weights/best.pt source=test.mp4 save=True conf=0.3
```
=======
- 检测框架：YOLOv8（ultralytics）
- 标注工具：Label Studio
- 编程语言：Python
- 开发工具：VS Code
>>>>>>> 362ccbf4992631f69f13de2ef639c2575b6ee1fb

## 模型性能

| 指标 | 数值 |
|------|------|
| mAP50 | 98.6% |
| Precision | 90.7% |
| Recall | 100% |
| 训练集 | 32张 |
| 验证集 | 8张 |
<<<<<<< HEAD
| 训练轮数 | 50 epochs |

## 项目流程

1. **数据采集**：使用爬虫脚本从网络下载猪的图片
2. **数据标注**：使用 Label Studio 对猪的区域进行框选标注
3. **数据分割**：将数据集按 80:20 比例分为训练集和验证集
4. **模型训练**：基于 YOLOv8n 预训练模型进行迁移学习
5. **模型测试**：使用新图片和视频验证检测效果
=======

## 使用方法

### 训练模型
```bash

### 检测图片
```bash

### 检测视频
```bash




## 项目流程

1. 数据采集：下载猪的图片
2. 数据标注：使用 Label Studio 框选猪的区域
3. 数据分割：80%训练集，20%验证集
4. 模型训练：基于 YOLOv8n 迁移学习
5. 模型测试：验证检测效果
>>>>>>> 362ccbf4992631f69f13de2ef639c2575b6ee1fb

## 改进方向

- 增加训练数据量（目标 200+ 张）
- 使用更大的模型（yolov8s/yolov8m）
- 增加训练轮数（100-200 epochs）
<<<<<<< HEAD
- 添加数据增强（mosaic、flipud）
- 扩展检测类别（如猪的不同姿态）
=======
















>>>>>>> 362ccbf4992631f69f13de2ef639c2575b6ee1fb
