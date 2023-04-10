```
def convert_to_tensor(array, is_change_dtype=False)->torch.Tensor:
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
    return change_dtype(tensor)
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
