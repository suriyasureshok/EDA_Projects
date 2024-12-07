import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter 
df = pd.read_csv("/kaggle/input/chennai-patients-data/Patient_Data_ChennaiCity.csv",encoding='ISO-8859-1')
df
df.isnull().sum()

