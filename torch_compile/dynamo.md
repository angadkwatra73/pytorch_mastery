## A guide to Torch Dynamo
Dynamo is a tracer
Meaning given a function and inputs to it - executes the function, records linear sequence of functions into a graph

It is represented by an FX graph.Simply think of it as a container that stores a list of function calls

- see the bytecode of a regular function call
- then with torch dynamo


## The code
- Used a simple function - produced the bytecode with dis disassmebler by python on the .pyc file
- The bytecode does not chanege much when you add torch.compile
- dynamo uses the bytecode to produce a graph trace - which can be seen by setting TORCH LOGS=graph_code
