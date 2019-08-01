
# %% 
#tree -L 3


#%%
import pandas as pd 
mercado_libre_df = pd.read_csv('scrapy_pipelines/tmp/productos-ml.csv')
mercado_libre_df.head()

#%%
mercado_libre_df.precio.mean() 


#%%
mercado_libre_df.info()

#%%


#%%
