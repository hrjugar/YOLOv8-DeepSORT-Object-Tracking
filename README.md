<h1 align="center">YOLOv8 Object Detection with DeepSORT Tracking (ID + Trails)</h1>

## Steps to run code

1. Clone the repository
```
git clone https://github.com/hrjugar/yolov8-deepsort.git
```
2. Go to the cloned folder.
```
cd yolov8-deepsort
```
3. Install the dependencies.
```
pip install -e .
```
4. Set the current directory.
```
cd ultralytics/yolo/v8/detect
```
5. Download sample video *test3.mp4* from this [link](https://drive.google.com/uc?id=1rjBn8Fl1E_9d0EMVtL24S9aNQOJAveR5&confirm=t) and save it in the current folder.

6. Run the command below.
```
python predict.py model=yolov8l.pt source="test3.mp4"
```

## Command configurations
> NOTE: There are a lot of other configurations made by their original authors. The ones listed here are configurations that have been verified to work by the current author.
<table>
  <tbody>
    <tr>
      <th>Configuration</th>
      <th>Description</th>
      <th>Possible Values</th>
    </tr>
    <tr>
      <td>model</td>
      <td>YOLOv8 model to use</td>
      <td>
        <ul>
          <li>yolov8n.pt</li>
          <li>yolov8s.pt</li>
          <li>yolov8m.pt</li>
          <li>yolov8l.pt</li>
          <li>yolov8x.pt</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>source</td>
      <td>The path of the video file to be analyzed by DeepSORT</td>
      <td>Any video file path</td>
    </tr>
    <tr>
      <td>show</td>
      <td>Boolean flag for displaying video while DeepSORT is processing</td>
      <td>
        <ul>
          <li>True</li>
          <li>False</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>save_dir</td>
      <td>The path of the folder where the output will be saved</td>
      <td>Any folder path</td>
    </tr>
    <tr>
      <td>socket_port</td>
      <td>The port to be used for the web sockets that will be used to communicate with the app.</td>
      <td>Any available port number</td>
    </tr>
  </tbody>
</table>

## Outputs
As of the moment, there are two outputs that are saved in the *save_dir* folder:
- The original input video file that has a bounding box marked on each object on each frame
- The results of DeepSORT in JSON, formatted in the following way:
  ```
  [
    // FRAME 1
    [
      // FRAME 1 OBJECT 1
      {
        "id": 1,
        "classification": "car",
        "x": 501,
        "y": 395,
        "w": 152,
        "h": 122
      },
      // OTHER FRAME 1 OBJECTS
      ...
    ],
    // OTHER FRAMES
    ...
  ]
  ```