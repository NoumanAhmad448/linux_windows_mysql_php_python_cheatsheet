
```
def convert_to_numpy(tensor:torch.Tensor):
  """
  convert tensor to numpy
  """
  try:
    return tensor.cpu() if tensor.ndim > 1 else "tensor ndim must be greater than 1"
      
  except:
    return "Something went wrong while converting tensor to numpy"
```
```
def show_image(image):
  """
    show image on the screen
    require convert_to_numpy function to be called first
  """
  plt.figure(figsize=(9,9))
  plt.imshow(convert_to_numpy(image))
  plt.axis(False)
```
