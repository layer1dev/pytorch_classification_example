import torchvision.transforms as transforms
import net as netc
import requests
import warnings
import torch
from torch.autograd import Variable
from PIL import Image

warnings.filterwarnings(action='ignore') 

def finder(img_url):
    classes = ['0','1','10','11.1','12','13','15','18','19','2','3','4','5','6','7','8','9']

    PATH = "./model/cars_model.pth"
    net = netc.Net()
    device = torch.device("cpu")
    net.load_state_dict(torch.load(PATH, map_location=device))

    image = image_loader(2, img_url)

    outputs = net(image)
    _, predicted = torch.max(outputs, 1)

    return classes[predicted]

def image_loader(dType, data):
    loader = transforms.Compose([transforms.Resize((32,32)), transforms.ToTensor()])
    # type:1 == data: image path
    # type:2 == data: image url
    """load image, returns cuda tensor"""
    if dType==1:
        image = Image.open(image_name)
    if dType==2:
        image = Image.open(requests.get(data, stream=True).raw)
    image = loader(image).float()
    image = Variable(image, requires_grad=True)
    image = image.unsqueeze(0)
    return image #.cuda()