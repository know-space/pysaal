"""
Basic Time Operations
=====================
"""

from pysaal.time import Epoch

# %%
# Let's initialize an Epoch object

epoch = Epoch.from_components(2024, 10, 10, 10, 10, 10.0)

print(epoch)
