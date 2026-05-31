# %%

import numpy as np
import matplotlib.pyplot as plt

def roofline_plot(B, D, F):
    flops = 2*B*D*F
    comm_bytes = 2*B*D + D*F + 2*B*F
    t_math = flops / 1.97e14
    t_comm = comm_bytes / 8.2e11
    t_lower = np.maximum(t_math, t_comm)
    return flops / t_lower

Bs = np.arange(1, 580)

roofline_4096 = roofline_plot(Bs, 4096, 4096)
roofline_1024 = roofline_plot(Bs, 1024, 1024)

plt.plot(Bs, roofline_4096, label='F=D=4096')
plt.plot(Bs, roofline_1024, label='F=D=1024')
plt.xlabel('Batch Size (B)')
plt.ylabel('peak FLOPS/s')
plt.legend()
plt.grid()

# %%



