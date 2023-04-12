```
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
 ```


```
# show the confusion matrix 
# step 1
# in the evaluation loop use the following
pred_arr.append(torch.softmax(test_pred, dim=1).argmax(dim=1).cpu())
pred_arr=torch.cat(pred_arr)

#step 2
import torchmetrics, mlxtend
    print(f"mlxtend version: {mlxtend.__version__}")
    assert int(mlxtend.__version__.split(".")[1]) >= 19, "mlxtend verison should be 0.19.0 or higher"
except:
    !pip install -q torchmetrics -U mlxtend # <- Note: If you're using Google Colab, this may require restarting the runtime
    import torchmetrics, mlxtend
    print(f"mlxtend version: {mlxtend.__version__}")
    
# step 3
from torchmetrics import ConfusionMatrix
from mlxtend.plotting import plot_confusion_matrix

confmat = ConfusionMatrix(num_classes=len(data_classes), task='multiclass')
confmat_tensor = confmat(preds=pred_arr,
                         target=y_test)

fig, ax = plot_confusion_matrix(
    conf_mat=confmat_tensor.numpy(),
    class_names=data_classes,
    figsize=(5, 5)
);
```


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
def show_image(image, label=None, cmap:str="gray",figsize:tuple = (4,4)):
  """
    show image on the screen
    require convert_to_numpy function to be called first
  """
  if label is None:
    label = "Image Caption"
  plt.figure(figsize=figsize)
  plt.imshow(convert_to_numpy(image), cmap=cmap)
  plt.title(label)
  plt.axis(False)
```
