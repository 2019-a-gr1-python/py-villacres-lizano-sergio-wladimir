
# %% 
#tree -L 3


#%%
import pandas as pd 
fybeca_df = pd.read_csv('scrapy_pipelines/tmp/productos-fybeca.csv')
fybeca_df.head() 

#%%
fybeca_df.precio.mean() 


#%%
fybeca_df.info()

#%%


#%%
