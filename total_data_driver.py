import pandas as pd
import numpy as np
import entropy_calculators as ec


### Calculate For the Human Genome
file = '../data/JHS_Genotype.csv'
tp = pd.read_csv(file, iterator=True, chunksize=100)
df = pd.concat(tp, ignore_index=True)



Total_entropy = 0
for index, row in df.iterrows():
    temp_list = row.tolist()
    del temp_list[:2]
    Total_entropy += ec.H(temp_list)

average_entropy = Total_entropy / df.shape[0]
np.save('human_entropy', average_entropy)
print("Average entropy of Human test = " +str(average_entropy)+'\n')
print(df.head(n=5))



### Calculate for the Wheat Genome
file = '../data/kasp.csv'
tp = pd.read_csv(file, iterator=True, chunksize=100)
df = pd.concat(tp, ignore_index=True)


Total_entropy = 0
for index, row in df.iterrows():
    temp_list = row.tolist()

    # remove unsequenced wheat strain data
    list(filter(('NS').__ne__, temp_list))
    del temp_list[:13]
    Total_entropy += ec.H(temp_list)
#
average_entropy = Total_entropy / df.shape[0]
print(df.shape[0])
np.save('wheat_entropy', average_entropy)
print("Average entropy of Wheat Genome = " +str(average_entropy)+'\n')
