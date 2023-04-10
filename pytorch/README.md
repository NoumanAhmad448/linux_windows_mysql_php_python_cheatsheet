```
def convert_to_tensor(array, is_change_dtype=False, is_change_device=False, to_device="cpu")->torch.Tensor:
  """
  Convert numpy array to tensor
  is_change_dtype=True will change the dtype to float
  
  Require: change_dtype, change_device functions to be intialized first
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
  ```




```
def change_device(tensor: torch.Tensor, device="cuda"):
  return tensor.to(device)
```


```
def setup_device():
    return "cuda" if  torch.cuda.is_available() else "cpu"
```

```
def change_dtype(tensor:torch.Tensor, dtype=torch.float):
  """
    dtype must have the value mentioned in the torch documentation
    e.g. torch.float , torch.LongTensor
  """
  return tensor.to(dtype)
```
