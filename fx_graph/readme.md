## FX graphs
- What is an FX graph?  -- what does it look like?
- How to produce an FX graph? - fx sysmbolic trace, then dynamo


## [Torch export](https://docs.pytorch.org/docs/2.12/user_guide/torch_compiler/export.html) 

Takes a torch.nn.Module -> produces 

- reuturn graph with aten ops 


## [Torch compile]

Leverages the following underlying tech
- Torch Dynamo 
- Torch inductor - default backedn
- AOT Autograd

has multiiple baceknds including - tvm, tensorrt,

### Frontend - Dynamo
- sequeunce of ops, guagrds andn residual bytecode
- 

