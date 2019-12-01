import pandas as pd
import os

data_path = 'MovieLens-Dataset/ml-100K/'

u1_base = pd.read_csv(os.path.join(data_path, 'u1_base.csv'),sep='	', header=None,
                     names=['user_id','item_id','rating','timestamp'])
u1_base = u1_base.drop(labels=['timestamp'], axis=1)

u1_test = pd.read_csv(os.path.join(data_path, 'u1_test.csv'),sep='	', header=None,
                     names=['user_id','item_id','rating','timestamp'])
u1_test = u1_test.drop(labels=['timestamp'], axis=1)

u2_base = pd.read_csv(os.path.join(data_path, 'u2_base.csv'),sep='	', header=None,
                     names=['user_id','item_id','rating','timestamp'])
u2_base = u2_base.drop(labels=['timestamp'], axis=1)

u2_test = pd.read_csv(os.path.join(data_path, 'u2_test.csv'),sep='	', header=None,
                     names=['user_id','item_id','rating','timestamp'])
u2_test = u2_test.drop(labels=['timestamp'], axis=1)

u3_base = pd.read_csv(os.path.join(data_path, 'u3_base.csv'),sep='	', header=None,
                     names=['user_id','item_id','rating','timestamp'])
u3_base = u3_base.drop(labels=['timestamp'], axis=1)

u3_test = pd.read_csv(os.path.join(data_path, 'u3_test.csv'),sep='	', header=None,
                     names=['user_id','item_id','rating','timestamp'])
u3_test = u3_test.drop(labels=['timestamp'], axis=1)

u4_base = pd.read_csv(os.path.join(data_path, 'u4_base.csv'),sep='	', header=None,
                     names=['user_id','item_id','rating','timestamp'])
u4_base = u4_base.drop(labels=['timestamp'], axis=1)

u4_test = pd.read_csv(os.path.join(data_path, 'u4_test.csv'),sep='	', header=None,
                     names=['user_id','item_id','rating','timestamp'])
u4_test = u4_test.drop(labels=['timestamp'], axis=1)

u5_base = pd.read_csv(os.path.join(data_path, 'u5_base.csv'),sep='	', header=None,
                     names=['user_id','item_id','rating','timestamp'])
u5_base = u5_base.drop(labels=['timestamp'], axis=1)

u5_test = pd.read_csv(os.path.join(data_path, 'u5_test.csv'),sep='	', header=None,
                     names=['user_id','item_id','rating','timestamp'])
u5_test = u5_test.drop(labels=['timestamp'], axis=1)
