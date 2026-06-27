"""
View the bytecode generated for the compiled graph
esentially how dynamo moddfies the bytecode
"""

import torch

@torch.compile()
def fn(a):
    b = a + 2 
    print("Hi")
    return b + a

fn(torch.randn(4))











