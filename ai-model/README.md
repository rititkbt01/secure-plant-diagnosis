# AI MODELS - Vision Transformers (200MB Total)

## Purpose  
Stores trained Deep Learning models:
1. resnet50_teacher.pth    - Teacher model (82% accuracy baseline)
2. deit_tiny_final.pth     - Student model (TARGET: 85-90% accuracy)
3. deit_tiny.onnx          - Mobile-optimized inference

## Model Architecture
- DeiT-Tiny (5.7M parameters)
- Knowledge Distillation (ResNet50 → DeiT)
- Input: 224x224 leaf images
- Output: 25 disease classes

## Status: Yashraj (AI Lead)
