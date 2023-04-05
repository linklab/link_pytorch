import torch

# create a non-contiguous tensor
x = torch.randn(3, 4)
y = x[:, 3]

# check if y is contiguous
print(y.is_contiguous())  # False

# make y contiguous
y = y.contiguous()

# check if y is now contiguous
print(y.is_contiguous())  # True