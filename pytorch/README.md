```
def setup_device():
    return "cuda" if  torch.cuda.is_available() else "cpu"
```

```
def change_dtype(tensor:torch.Tensor, dtype=torch.float):
  """
    dtype must be type mentioned in the torch documentation
    e.g. torch.float , torch.LongTensor
  """
  return tensor.to(dtype)
```
