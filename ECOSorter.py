import os
import tensorflow
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
import numpy


def predict_image (image_path):
  model = MobileNetV2(weights='imagenet')
  img = image.load_img(image_path, target_size = (224,224))
  img_array = image.img_to_array(img)
  img_array_expanded_dims = numpy.expand_dims(img_array, axis=0)
  img_preprocessed = preprocess_input(img_array_expanded_dims)

  predictions = model.predict(img_preprocessed)
  result = decode_predictions(predictions, top = 1)[0]
  # lists used for sample test run but ideally items placed in bin will be compared with the items in 3 big text files, one for each bin
  compost = ["banana", "apple", "eggshells", "orange"]
  garbage = ["candy wrappers", "straw", "tissues"]
  recycle = ["paper", "cardboard", "plastic bottle"]
  print(f"{os.path.basename(image_path)}")
  for i, (imagenet_id, label, score) in enumerate(result):
    i += 1;
    print(f"Prediction: {label} ({score*100:.2f}%)")
    if label in compost:
      print(f"{os.path.basename(image_path)} - {label} - goes to compost bin")
    elif label in garbage:
      print(f"{os.path.basename(image_path)} - {label} - goes to garbage bin")
    elif label in recycle:
      print(f"{os.path.basename(image_path)} - {label} - goes to recycle bin")
    else:
      print(f"{os.path.basename(image_path)} - {label} - goes to garbage bin")
  print("\n")
folder = r'/content/images'
for filename in os.listdir(folder):
  if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
    image_path = os.path.join(folder, filename)
    predict_image(image_path)



