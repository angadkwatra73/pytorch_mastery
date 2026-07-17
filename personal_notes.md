# Doubts or Questions

- The trace happens for a graph in two stages 
    - This 2 stage prcoess - tracing the fx, then checking and adding gurards
    - Now if there is fullgraph then 2 traces
    - does this hold for each subgraph also - where we trace and do guards

- still confused about the IR 

- so I mean, I still don't know what causes the graph break and what doesn't? --

- also torch compile - anyway needs a python interpreter right?
    - that's why need to export, lightweight runtime
    - that's why exec pytorch exists - need something to deply on edge?
// Here the asnwer is somewhat about the eval framework and how it hooks

---- Look at torch export ----
- i mean so then AOT - waht does it do for control flow ?
    - jit tracer chooses one path 



# notes 

Tracing - is about creating a dataflow graph of tensor ops . Dynamo all about 

Guards - need to make graph sound.
        - cause recompile if it fails
Graph Breaks - is about python code unexecutable by Dynamo. - make graph complete. 
            - no compile, jsut python execution

Sym shapes -- diff idea. control flow w sym int can be done. 



# organise 
