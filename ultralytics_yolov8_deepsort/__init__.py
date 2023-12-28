# Ultralytics YOLO 🚀, GPL-3.0 license

__version__ = "8.0.3"

from ultralytics_yolov8_deepsort.hub import checks
from ultralytics_yolov8_deepsort.yolo.engine.model import YOLO
from ultralytics_yolov8_deepsort.yolo.utils import ops

__all__ = ["__version__", "YOLO", "hub", "checks"]  # allow simpler import
