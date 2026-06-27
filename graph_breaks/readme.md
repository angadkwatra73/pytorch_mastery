If we look at branching two thingns can happen
- The tracer to form an FX graph, has to choose a path
    - that is when dynamo can handle the opeeration
- If dynamo cannont handlel the if - then it causes the break
    - ? or maybe it cannot guard it? somemthihng

## Graph Break
The simple funda is if you encounter code dynamo cannot handle the python code - thenn we get a graph bbreak


### Graph breaks reasons 
- data-dependent if statements 
- many python built-in functions --> opencv, etc
- C functions?

Functions that are not supported, printing and logging may not concern us much.

### What does the bytecode look like?
 - modified bytecode now look like - call compiled grpah 1, regular bytecode python, call compiled graph 2


## Usage 
 branch_wo_break.py and bramch_w_break.py show that branching does not always cause graph breaks
    - set TORCH_LOGS = graph_breaks, dynamo
    - compare the dynamo_flag files for both - to see the difference
    - graph breaks flag will tell you where the graph break is called

What we understand 
 - data depended operation will cause a graph break 
- here data means the tesnor

//should be linked to how 




