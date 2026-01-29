import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns


df = pd.read_csv(r"C:\Users\Prashant sawant\Downloads\iris.csv")



# df = pd.read_csv("iris.csv")

# Basic Histograms
# df.hist(figsize=(10,8))
# plt.suptitle("Feature Distributions", fontsize=16)
# plt.show()



# Scatterplot
# sns.scatterplot(data=df, x="sepal_length", y="sepal_width", hue="species")
# plt.title("Sepal Length vs Sepal Width")
# plt.show()

# pair plot
# sns.pairplot(df, hue="species")
# plt.show()

# boxplot 
sns.boxplot(data=df, x="species", y="sepal_length")
plt.title("Petal Length Distribution by Species")
# plt.show()

# violinplot
sns.violinplot(data=df, x="species", y="petal_length")
plt.title("Petal Length Violin Plot by Species")
plt.show()

# heatmap
# corr = df.drop(columns="species").corr()
# sns.heatmap(corr, annot=True, cmap="coolwarm")
# plt.title("Feature Correlation Heatmap",loc="Right",color="red")
# plt.show()

# pca 
from sklearn.decomposition import PCA

X = df.drop(columns="species")
pca = PCA(n_components=2)
components = pca.fit_transform(X)

df["PC1"] = components[:,0]
df["PC2"] = components[:,1]

sns.scatterplot(data=df, x="PC1", y="PC2", hue="species")
plt.title("PCA Projection of Iris Dataset")
plt.show()




