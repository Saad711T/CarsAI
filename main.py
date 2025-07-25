import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import cv2
import numpy as np
import sys
import os


# Cars
class_names = ['bmw', 'chevy', 'ferrari', 'ford', 'toyota']



def load_model(model_path="car_model.pth"):
    model = models.resnet18(pretrained=False)
    model.fc = nn.Linear(model.fc.in_features, len(class_names))
    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    model.eval()
    return model





def preprocess_image(image_path):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
    ])
    image = Image.open(image_path).convert("RGB")
    return transform(image).unsqueeze(0)



def predict(model, image_path):
    img_tensor = preprocess_image(image_path)
    with torch.no_grad():
        outputs = model(img_tensor)
        _, predicted = torch.max(outputs, 1)
    return class_names[predicted.item()]

def display_image_with_prediction(image_path, prediction):
    image = cv2.imread(image_path)
    if image is None:
        print("Failed to loading the image")
        return

    cv2.putText(image, prediction, (40, 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)
    cv2.imshow(prediction, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("🔧 الاستخدام: python main.py path/to/image.jpg")
        sys.exit(1)

    image_path = sys.argv[1]
    if not os.path.exists("car_model.pth"):
        print("car_model.pth not found")
        sys.exit(1)

    if not os.path.exists(image_path):
        print(f"image not found {image_path}")
        sys.exit(1)





    model = load_model()
    prediction = predict(model, image_path)
    display_image_with_prediction(image_path, prediction)
