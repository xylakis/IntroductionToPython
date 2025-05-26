# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 19:49:00 2024

@author: Manos
"""
#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

df = pd.read_csv("Results/vr_feature_importance_OnlyAT_OnlyShortMem.csv")

#df['Feature'][0] = "Curvature Δ"

df.loc[0, "Feature"] = "Curvature Δ"
df.loc[3, "Feature"] = "Height Δ"
df.loc[6, "Feature"] = "Illumination Δ"
df.loc[9, "Feature"] = "Occlusions Δ"

print(df['Feature'][0])

# Set the 'feature' column as the index
df.set_index('Feature', inplace=True)

#%%
# Plotting the heatmap with custom size
plt.figure(figsize=(25, 10))  # Adjust the size as needed
sns.set_theme(font_scale=1.5)
sns.heatmap(df,annot=True,fmt=".2f",linewidth=.4, annot_kws={'size': 18}, cbar=True)
plt.xticks(rotation=-40, rotation_mode="anchor",ha="left",fontsize=18)
plt.yticks(fontsize=18)
plt.xlabel('',fontsize=24,fontweight='bold')
plt.ylabel('',fontsize=24,fontweight='bold',rotation=90)
# %%
