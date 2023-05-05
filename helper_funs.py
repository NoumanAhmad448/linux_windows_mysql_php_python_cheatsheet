import torch 
import numpy as np
import matplotlib.pyplot as plt
import requests

from sklearn.model_selection import train_test_split
from numpy import random
from torch import nn
try:
  from torchsummary import summary
except:
  !pip install torchsummary
  from torchsummary import summary

try:
  from torchmetrics import Accuracy
except:
  !pip install torchmetrics
  from torchmetrics import Accuracy

from torchvision.transforms import ToTensor
from torch.utils.data import DataLoader

#new 
from torchvision import models
from torchvision import transforms
from torchsummary import summary

try:
  import fiftyone as fo
except:
  !pip install fiftyone
  import fiftyone as fo
import fiftyone.zoo as foz
from fiftyone import ViewField as F
import fiftyone.utils.coco as fouc
from PIL import Image
import pandas as pd
from torchvision.transforms import functional as func
import fiftyone.brain as fob
import eta.core.utils as etau
from pathlib import Path
import sys
from google.colab import files,drive
import fiftyone.utils.random as four

def fo_rename_field(dataset, pre_label_field,new_label_field):
  if dataset.get_field(pre_label_field) is not None:
    dataset.rename_sample_field(pre_label_field,new_label_field)

def download_file_colab(file):
  files.download(file)

def export_dataset(file_name,dataset,dataset_type=fo.types.FiftyOneDataset,is_req_field=False,label_field="ground_truth"):
  if is_req_field:
    dataset.export(file_name, dataset_type=dataset_type,label_field=label_field)
  else:
    dataset.export(file_name, dataset_type=dataset_type)

def mount_google_drive(path='/content/gdrive/'):
  drive.mount(path, force_remount=True)
  
def upload_file_colab():
    uploaded = files.upload()
    for filename in uploaded.keys():
        print("Uploaded '%s'" % filename)

def show_multi_images(data: torch.Tensor, figsize:tuple=(9,9), rows:int=3, cols:int=3, classes=None,
                      cmap="gray", is_require_squeeze:bool=True):
  """
  classes list|dict
  require convert_to_numpy function to be called first
  """
  DEFAULT_LABEL = None
  if classes is None:
    DEFAULT_LABEL = "Image Caption"
  
  figure = plt.figure(figsize=figsize)
  cols, rows = cols, rows
  for i in range(1, cols * rows + 1):
      sample_idx = torch.randint(len(data), size=(1,)).item()
      img, label = data[sample_idx]
      figure.add_subplot(rows, cols, i)
      plt.title(DEFAULT_LABEL if classes is None else classes[label])
      plt.axis(False)
      plt.imshow(convert_to_numpy(img.squeeze() if is_require_squeeze else img), cmap=cmap)
  plt.show()

def convert_to_numpy(tensor:torch.Tensor):
  """
  convert tensor to numpy
  """
  try:
    return tensor.cpu() if tensor.ndim > 1 else "tensor ndim must be greater than 1"
      
  except:
    return "Something went wrong while converting tensor to numpy"
def show_image(image, label=None, cmap:str="gray",figsize:tuple = (4,4), is_squeeze_not_req:bool=False,
               is_img_rgb:bool=False):
  """
    show image on the screen
    require convert_to_numpy function to be called first
  """
  if label is None:
    label = "Image Caption"
  if is_img_rgb:
    image = image.permute(1,2,0)
  
  plt.figure(figsize=figsize)
  plt.imshow(convert_to_numpy(image if is_squeeze_not_req else image.squeeze()), cmap=cmap)
  plt.title(label)
  plt.axis(False)








def change_device(tensor: torch.Tensor, device="cuda"):
  return tensor.to(device)

def setup_device():
    return "cuda" if  torch.cuda.is_available() else "cpu"


def change_dtype(tensor:torch.Tensor, dtype=torch.float):
  """
    dtype must have the value mentioned in the torch documentation
    e.g. torch.float , torch.LongTensor
  """
  return tensor.to(dtype)

def convert_to_tensor(array, is_change_dtype=False, is_change_device=False, to_device="cpu")->torch.Tensor:
  """
  convert numpy array to tensor
  is_change_dtype=True will change the dtype to float
  """

  tensor = None
  if torch.is_tensor(array):
     tensor = array
  else:
     tensor = torch.from_numpy(array)
  
  if is_change_dtype: 
    tensor = change_dtype(tensor)
  
  if is_change_device: 
    tensor = change_device(tensor, device=to_device)
  
  return tensor

# convert_to_tensor(random.rand(2,3),is_change_dtype=True)
def convert_to_numpy(tensor:torch.Tensor):
  """
  convert tensor to numpy
  """
  try:
    return tensor.cpu() if tensor.ndim > 1 else "tensor ndim must be greater than 1"
      
  except:
    return "Something went wrong while converting tensor to numpy"
