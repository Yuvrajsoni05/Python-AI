import numpy as np
image = np.array([
    [0   ,0  , 255   ,0  , 0],
    [0   ,0  , 255   ,0  , 0],
    [0   ,0  , 255   ,0  , 0],
    [0   ,0  , 255   ,0  , 0]
])


print(image)
print(image.shape)
print(image.size)
image = image / 255.0
print(image)