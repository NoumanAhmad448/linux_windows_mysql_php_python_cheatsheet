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
