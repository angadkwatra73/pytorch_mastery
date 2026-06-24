## A guide to Torch Dynamo
Dynamo is a tracer. Meaning given a function and inputs to it - executes the function, records linear sequence of functions into a graph.

It is represented by an FX graph.Simply think of it as a container that stores a list of function calls

How does it work?
- see the bytecode of a regular function call
- then with torch dynamo JIT compiles the bytecode to an FX graph

Consists mainly of 4 major concepts 
- Tracing 
- Guards 
- Symbolic Shapes
- Graph Breaks

## Tracing 

### Running the exmaples and analyzing the output 
- for dynamo_1.py we introduce the concept of dynamo and how to see the output
- Used a simple function - produced the bytecode with dis disassmebler by python on the .pyc file
- dynamo uses the bytecode to produce a graph trace - which can be seen by setting TORCH LOGS=graph_code
- It records a linear sequence of pytorch operations
- use TORHC_LOGS = graph_code to see graph trace
- use TORCH_LOGS = dynamo to see what dyanmo is doing

### Branching and control-flow with Dynamo
- for dynamo_2.py we show how the branching is traced - but does not cause an error because it not data dependent control flow
- use TORCH_LOGS = dynamo to see what dyanmo is doing
- notice the use of SymInt when recompiling

## Guards - Making dynamo sound
- guard breaking means the tracing is not accurate so we must change
- It is an assumption made in order to specialise a frame for one set of example inputs
- reusing the graph is only valid if these assumptions hold on the new inputs
- Therefore GUARD FAIL triggers RECOMPILATION
- use TORCH LOGS = guards to see the guards produced
- use TORCH_LOGS = recompiles to see when guards fail and the model recompiles

## Symbolic Shapes - 
- not to be confused with symbolic execution
- in dynamo_2.py when recompiling the first time -> it uses SymInt variable
- Static shapes by default
- 

Unti now we have a tracer that can trace Pytorch operations on tensors and integers and has a 
## Graph Breaks  - Making Dynamo complete
// is their execuion dependent on the backend?
// Graph breaks itself - go the python interpreter so should be okay   
- To execute a graph break we just switch context from GPU runtime to the python runtime on the CPU


