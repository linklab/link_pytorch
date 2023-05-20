import torch

# create a non-contiguous tensor
x = torch.randn(3, 4)
y = x[:, 3]

# check if y is contiguous
print(y.is_contiguous())  # False

# make y contiguous
y = y.contiguous()

# check if y is now contiguous
print(y.is_contiguous())  # Tru


a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]# e
print(a[::2])
