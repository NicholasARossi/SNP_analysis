import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import inverse_entropy as ie


#### Notes from other functions:
#       Average entropy of Human Genome = 1.116289189572329
#       Average entropy of Wheat Genome = 1.2517875997584096

sns.set(style="white")
fig,ax1=plt.subplots()


# Load the example iris dataset
iris = sns.load_dataset("iris")

# "Melt" the dataset to "long-form" or "tidy" representation
df_size=500
### Wheat DF
wheat=pd.DataFrame()
### determine probabilities
rez=ie.solver(16,1.2517875997584096)
wheat['species']=['wheat']*df_size
wheat['values']=np.random.rand(df_size)
wheat['genotype']=np.random.choice(16, df_size,p=rez)



human=pd.DataFrame()
### determine probabilities
rez=ie.solver(16,1.116289189572329)

human['species']=['human']*df_size
human['values']=np.random.rand(df_size)
human['genotype']=np.random.choice(16, df_size,p=rez)


random=pd.DataFrame()
random_weights=np.ones(16)*(1/16)
random['species']=['random']*df_size
random['values']=np.random.rand(df_size)
random['genotype']=np.random.choice(16, df_size,p=random_weights)


uniform=pd.DataFrame()

uniform['species']=['uniform']*df_size
uniform['values']=np.random.rand(df_size)
uniform['genotype']=np.zeros(df_size)

# s['human']=np.ones(10)
frames = [random, wheat,human,uniform]

result = pd.concat(frames)

# s = pd.Series(np.ones(10)*10, index='wheat')
# s = pd.Series(np.ones(10)*10, index='sequence')
# # Draw a categorical scatterplot to show each observation
# sns.swarmplot(x="measurement", y="value", hue="sequence",palette="Set2", data=iris)
# "Melt" the dataset to "long-form" or "tidy" representation
iris = pd.melt(iris, "species", var_name="measurement")

# Draw a categorical scatterplot to show each observation
#palette="Set2"

tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]

# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.
for i in range(len(tableau20)):
    r, g, b = tableau20[i]
    tableau20[i] = (r / 255., g / 255., b / 255.)

sns.swarmplot(x="species", y="values", hue="genotype", palette=tableau20,data=result,ax=ax1)
ax1.legend_.remove()
fig.savefig('swarm_plot.png')