import torch
from torch.export import export, ExportedProgram

class Mod(torch.nn.Module):
    def forward(self, x:torch.Tensor, y:torch.Tensor) -> torch.Tensor:
        a = torch.sin(x)
        b = torch.cos(y)
        return a + b

example_args = (torch.randn(10, 10),  torch.randn(10, 10))

exported_program: ExportedProgram = export(Mod(), args=example_args)
print(exported_program)



"""ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, x: "f32[10, 10]", y: "f32[10, 10]"):
            # File: /home/sheldon/Desktop/xla/torch_compile/basic_forward.py:6 in forward, code: a = torch.sin(x)
            sin: "f32[10, 10]" = torch.ops.aten.sin.default(x);  x = None

            # File: /home/sheldon/Desktop/xla/torch_compile/basic_forward.py:7 in forward, code: b = torch.cos(y)
            cos: "f32[10, 10]" = torch.ops.aten.cos.default(y);  y = None

            # File: /home/sheldon/Desktop/xla/torch_compile/basic_forward.py:8 in forward, code: return a + b
            add: "f32[10, 10]" = torch.ops.aten.add.Tensor(sin, cos);  sin = cos = None
            return (add,)

Graph signature:
    # inputs
    x: USER_INPUT
    y: USER_INPUT

    # outputs
    add: USER_OUTPUT

Range constraints: {}
"""
# Has aten ops in pytorch - produced by AOT 

