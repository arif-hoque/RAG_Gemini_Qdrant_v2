import pandas as pd
import seaborn as sns
import google.generativeai as genai
import matplotlib.pyplot as plt

name = f'tuned-gemini-model'
operation = genai.get_tuned_model(f'tunedModels/{name}')
model = genai.get_tuned_model(f'tunedModels/{name}')

snapshots = pd.DataFrame(model.tuning_task.snapshots)

sns.lineplot(data=snapshots, x = 'epoch', y='mean_loss')
plt.show()

print(snapshots.head())
