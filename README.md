# Route to PyTorch mastery
The goal is to deeply understand how AI models are compiled, optimized and run during inference. Before we go onto working with LLMs, compiling them, and using advanced kernels - we must work with Pytorch Basics and understand the graph tracing of PyTorch.  

## Checklislt
- [x] Torch API
  - Why does Torch Tensor exist?
  - What is eager mode? 
- [x] Basic Profiling using Pytorch
  - How do you view kernel calls?
  - To profile time on GPU vs CPU
-  [ ] FX Graph
-  [ ] Torch Dynamo
    - [x] Tracing - control flow and retracing
    - [x] Guards 
    - [x] Symbolic Shapes
    - [x] Flags - graph capture, dynamo, breaks etc
    - [ ] Graph Breaks
 
-  [ ] torch.compile()
-  [ ] torch.export()
       
## Directory Structure 

### torch_api
- basic forward pass and class defintion
- exporting the model

### profiling
- how to profile a basic 

### torch compile
- examples showing differnt aspects of torch dynamo



Resources 
- [x] [Torch NN and Parameters](https://docs.pytorch.org/tutorials/beginner/introyt/modelsyt_tutorial.html)
- [x] [Using torch profiler](https://huggingface.co/blog/torch-profiler)
- [ ] ⭐[Torch Dynamo Deep Dive](https://docs.pytorch.org/docs/2.12/user_guide/torch_compiler/torch.compiler_dynamo_deepdive.html)
- [ ] ⭐[Torch compile](https://docs.pytorch.org/docs/2.12/user_guide/torch_compiler/compile/programming_model.html)
- [ ] [Graph Break Analysis](https://arxiv.org/abs/2509.16248)



 
