<H1 align="center">
YOLOv8 Object Detection with DeepSORT Tracking(ID + Trails) </H1>

## Steps to run Code

1. Clone the repository
```
git clone https://github.com/hrjugar/yolov8-deepsort.git
```
2. Go to the cloned folder.
```
cd yolov8-deepsort
```
3. Install the dependecies
```
pip install -e .
```
4. Setting the Directory.
```
cd ultralytics/yolo/v8/detect
```
5. Download sample video *test3.mp4* from this [link](https://drive.google.com/uc?id=1rjBn8Fl1E_9d0EMVtL24S9aNQOJAveR5&confirm=t) and save it in the current folder.

6. Run the code with mentioned command below.
```
python predict.py model=yolov8l.pt source="test3.mp4" show=True
```