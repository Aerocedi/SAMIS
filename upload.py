from roboflow import Roboflow

rf = Roboflow(api_key="XcqZAwwgDzDOWwoLclyI")
project = rf.workspace().project("car-maintenance")
project.version(3).deploy(model_type="yolov8", model_path=f"runs/detect/train9/")