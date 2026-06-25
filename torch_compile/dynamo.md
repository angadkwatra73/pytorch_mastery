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
calling system which knows when to use prev called graph, and trtrace
## Graph Breaks  - Making Dynamo complete
// is their execuion dependent on the backend?
// Graph breaks itself - go the python interpreter so should be okay   
- To execute a graph break we just switch context from GPU runtime to the python runtime on the CPU

For a function without graph breaks,  the tracingg process of a program calls t he function 2 times with the same arguments

1. First call to funciono
-  Traces the function into an FX graph
    - FX graph is compiled by the compiler into efficieint low level code ( default inductor)
- Rewrites the bytecode of thhe function to call the compiled function
- CPython  is given the new bytecode to run  in the Eval Frame

2.Second call to the function
- checksk the guards fromm the first call against the new args, since they're same as before they pass
- asks Cpython to tun  the bytecodde associatetd with those guards

This is the method that enanbles us to implement graph breaks. Because for a graph break how it would play out
- Bytecode that executes the first graph
- Bytecode that leaves the stack as it would be if CPython would have executed the first graph. It also replays any modifications to local or global variables that would be visible at this point
- The bytecode that made Dynamo graph break
- Bytecode that executes the second graph
