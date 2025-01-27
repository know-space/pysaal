"""
SGP4-XP Basic Usage
===================
"""

from pysaal.elements import TLE
from pysaal.time import Epoch

# %%
# Let's initialize a XP TLE object

l1 = "1 61429U          24362.90619720 +.00000000  00000 0  55480 0 4 0001"
l2 = "2 61429  88.9747 334.1365 0159713  22.5177  31.9343 14.3545506800001"

tle = TLE.from_lines(l1, l2)

# %%
# We can confirm that this is one of the new XP TLEs:
print(tle.ephemeris_type)


# %%
# Let's now initialize an epoch and propagate the TLE to it

epoch = Epoch.from_components(2024, 10, 10, 10, 10, 10.0)

tle_prop = tle.get_state_at_epoch(epoch)

print(f"TLE position: {tle_prop.cartesian_elements.position} [km]")
print(f"TLE velocity: {tle_prop.cartesian_elements.velocity} [km/s]")
