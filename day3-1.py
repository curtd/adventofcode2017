import numpy as np
value = 325489
lower_right_corner = int(np.ceil(np.sqrt(value)))
lower_right_corner = lower_right_corner + 1 if lower_right_corner%2==0 else lower_right_corner
lr_corner_value = lower_right_corner**2
level = (lower_right_corner-1)/2
# Bottom edge of the square
if lr_corner_value-lower_right_corner+1 <= value:
    midpt = lr_corner_value-lower_right_corner+1 + level
steps = np.abs(midpt-value) + level
print("Steps {}".format(steps))