# This is un-used code for our Tensor flow model with statistical normalization.
# It was rejected; as it is less eficient and more complicated than our SciKitLearn code, while performing similarly.
#
# It is included at the professors request (12/13/2021 Office Hours); but not used in the final version.


#IMPORTS
#-----------------------------------------------------------------------------------------------------------
import pandas as pd
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras import layers
#-----------------------------------------------------------------------------------------------------------

#DEFINITIONS
#-----------------------------------------------------------------------------------------------------------
#This takes a pandas dataframe; batches it, and prepares it for use with "get_isNorm" and keras
def pandastokeras(dataframe, shuffle=True, batch_size=32):
  df = dataframe.copy()
  labels = df.pop('blue_win')
  df = {key: value[:,tf.newaxis] for key, value in dataframe.items()}
  ds = tf.data.Dataset.from_tensor_slices((dict(df), labels))
  if shuffle:
    ds = ds.shuffle(buffer_size=len(dataframe))
  ds = ds.batch(batch_size)
  ds = ds.prefetch(batch_size)
  return ds

#This takes a dataset column, and normalises it. Returns normalised column.
def get_isNorm(name, dataset):
  normalizer = layers.Normalization(axis=None)
  feature_ds = dataset.map(lambda x, y: x[name])
  normalizer.adapt(feature_ds)
  return normalizer
#-----------------------------------------------------------------------------------------------------------

#DATASET PREPERATION
#-----------------------------------------------------------------------------------------------------------
data = pd.read_csv('https://raw.githubusercontent.com/quentingourier/c478_dnq/main/MatchTimelinesFirst15.csv')
data = data.drop(columns = ['matchId','blueDragonKills', 'redDragonKills'])

train, validation, test = np.split(data.sample(frac=1), [int(0.8*len(data)), int(0.9*len(data))])

train2 = pandastokeras(train, batch_size=256)
validation2 = pandastokeras(validation, shuffle=False, batch_size=256)
test2 = pandastokeras(test, shuffle=False, batch_size=256)

allin = []
normFeat = []
for header in ['blueGold', 'blueMinionsKilled', 'blueJungleMinionsKilled', 'blueAvgLevel', 'redGold', 'redMinionsKilled', 'redJungleMinionsKilled', 'redAvgLevel', 'blueChampKills', 'blueHeraldKills', 'blueTowersDestroyed', 'redChampKills', 'redHeraldKills', 'redTowersDestroyed']:
  numeric_col = tf.keras.Input(shape=(1,), name=header)
  isNorm = get_isNorm(header, train2)
  isEnconded = isNorm(numeric_col)
  allin.append(numeric_col)
  normFeat.append(isEnconded)

allFeat = tf.keras.layers.concatenate(normFeat)
x = tf.keras.layers.Dense(32, activation="relu")(allFeat)
x = tf.keras.layers.Dropout(0.5)(x)
output = tf.keras.layers.Dense(1)(x)
#-----------------------------------------------------------------------------------------------------------

#MODEL FITTING AND TESTING
#-----------------------------------------------------------------------------------------------------------
model = tf.keras.Model(allin, output)

model.compile(optimizer='adam',
              loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
              metrics=["accuracy"])

tf.keras.utils.plot_model(model, show_shapes=True, rankdir="LR")

model.fit(train2, epochs=8, validation_data=validation2, verbose = False)

loss, accuracy = model.evaluate(test2)
print("TEST Accuracy", accuracy, "  TEST LOSS", loss)
#-----------------------------------------------------------------------------------------------------------





