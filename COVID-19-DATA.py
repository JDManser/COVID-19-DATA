#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np


# # Import and clean confirmed cases data

# In[ ]:


confirmed_raw = pd.read_csv("time_series_covid19_confirmed_global.csv")


# In[ ]:


confirmed_raw.head()


# In[ ]:


confirmed_raw.columns


# In[ ]:


confirmed = pd.melt(confirmed_raw, id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], var_name="Date", value_name="Confirmed")


# In[ ]:


confirmed.head()


# In[ ]:


pd.isna(confirmed["Province/State"]).sum()


# In[ ]:


confirmed["Province/State"] = confirmed["Province/State"].fillna("None")


# In[ ]:


pd.isna(confirmed["Province/State"]).sum()


# # Import and clean reported deaths data 

# In[ ]:


deaths_raw = pd.read_csv("time_series_covid19_deaths_global.csv")


# In[ ]:


deaths_raw.head()


# In[ ]:


deaths = pd.melt(deaths_raw, id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], var_name="Date", value_name="Deaths")


# In[ ]:


deaths.head()


# In[ ]:


pd.isna(deaths["Province/State"]).sum()


# In[ ]:


deaths["Province/State"] = deaths["Province/State"].fillna("None")


# In[ ]:


pd.isna(deaths["Province/State"]).sum()


# In[ ]:


deaths.head()


# # Import and clean recovered data

# In[ ]:


recovered_raw = pd.read_csv("time_series_covid19_recovered_global.csv")


# In[ ]:


recovered_raw.head()


# In[ ]:


recovered = pd.melt(recovered_raw, id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], var_name="Date", value_name="Recovered")


# In[ ]:


recovered.head()


# In[ ]:


pd.isna(recovered["Province/State"]).sum()


# In[ ]:


recovered["Province/State"] = recovered["Province/State"].fillna("None")


# In[ ]:


pd.isna(recovered["Province/State"]).sum()


# In[ ]:


recovered.head()


# # Merge the data

# In[ ]:


confirmed.columns


# In[ ]:


merge_1 = pd.merge(confirmed, deaths, on=['Province/State', 'Country/Region','Date'])


# In[ ]:


merge_1.head()


# In[ ]:


len(covid_19)


# In[ ]:


covid_19 = pd.merge(merge_1, recovered, on=['Province/State', 'Country/Region','Date'])


# In[ ]:


covid_19.head()


# In[ ]:


covid_19 = covid_19.drop(columns=['Lat_x', 'Long_x', 'Lat_y', 'Long_y'])


# In[ ]:


covid_19.head()


# # Export to csv

# In[ ]:


covid_19.to_csv("covid_19_data.csv", index=False)

