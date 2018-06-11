from .tensor import TensorBase, sparseTensor, np
from ..utils import scatter_map, scatter_sum

from .math.tensor_math import install_variable_arithmetics as iva_tensor
from .tensor_plugin import install_tensor_plugin as itp 

itp()
iva_tensor()