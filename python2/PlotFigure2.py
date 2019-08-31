import numpy as np
import SaveStandardImageBase
from MeanGreyLevel import MeanGreyLevel
from LearningProcess import LearningProcess
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

side_pixels = 64
num_units = 15
num_image = 15

image_db = SaveStandardImageBase.main("../")
meangrey = MeanGreyLevel( side_pixels, image_db, num_image)
weights = LearningProcess( num_units, 
                          side_pixels, 
                          image_db, 
                          num_image, 
                          meangrey,
                         nIter=20)
finalImage = np.zeros((64*3,64*5))
finalImage = weights.reshape((3,5,64,64))
finalImage = np.concatenate(finalImage,axis=-2)
finalImage = np.concatenate(finalImage,axis=-1)
fig,axs = plt.subplots(1,1,figsize=[12,4])
ax = axs
ax.imshow(finalImage)
fig.savefig("Figure2.png")

# for nh in range(5):
#     for nv in range(3):
#         PC =np.zeros(64,64)
#         for I in range