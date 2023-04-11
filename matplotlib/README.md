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
def show_image(image, label=None):
  """
    show image on the screen
    require convert_to_numpy function to be called first
  """
  if label is None:
    label = "Image Caption"
  plt.figure(figsize=(4,4))
  plt.imshow(convert_to_numpy(image))
  plt.title(label)
  plt.axis(False)
```
