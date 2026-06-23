import torch

def mse(x, y):
    z = (x - y) ** 2 
    return z.sum()

x = torch.randn(200)
y = torch.randn(200)
res = mse(x, y)
print(res)











