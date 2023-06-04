import glob
import os
import pandas as pd
import tensorflow as tf
import numpy as np

columns = [
    'Unnamed: 0',
    'version',
    'alive',
    'tagId',
    'success',
    'timestamp',
    'data__tagData__gyro__x',
    'data__tagData__gyro__y',
    'data__tagData__gyro__z',
    'data__tagData__magnetic__x',
    'data__tagData__magnetic__y',
    'data__tagData__magnetic__z',
    'data__tagData__quaternion__x',
    'data__tagData__quaternion__y',
    'data__tagData__quaternion__z',
    'data__tagData__quaternion__w',
    'data__tagData__linearAcceleration__x',
    'data__tagData__linearAcceleration__y',
    'data__tagData__linearAcceleration__z',
    'data__tagData__pressure',
    'data__tagData__maxLinearAcceleration',
    'data__anchorData',
    'data__acceleration__x',
    'data__acceleration__y',
    'data__acceleration__z',
    'data__orientation__yaw',
    'data__orientation__roll',
    'data__orientation__pitch',
    'data__metrics__latency',
    'data__metrics__rates__update',
    'data__metrics__rates__success',
    'data__coordinates__x',
    'data__coordinates__y',
    'data__coordinates__z',
    'reference__x',
    'reference__y']

if __name__ == '__main__':

    # Odczytanie danych do późniejszego przefiltrowania
    verif_data = pd.read_excel('./dane/pomiary/F10/f10_random_1p.xlsx')
    verif_measured_x = verif_data.pop('data__coordinates__x')
    verif_measured_y = verif_data.pop('data__coordinates__y')
    verif_reference_x = verif_data.pop('reference__x')
    verif_reference_y = verif_data.pop('reference__y')
    verif_measured = pd.concat([verif_measured_x, verif_measured_y], axis=1)
    verif_reference = pd.concat([verif_reference_x, verif_reference_y], axis=1)

    # Odczytanie danych potrzebnych do uczenia sieci neuronowej
    all_files = glob.glob(os.path.join('./dane/pomiary/F10/f10_stat_*.xlsx'))
    df_from_each_file = (pd.read_excel(f, names=columns) for f in all_files)
    concatenated_df = pd.concat(df_from_each_file, ignore_index=True)

    measured_x = concatenated_df.pop('data__coordinates__x')
    measured_y = concatenated_df.pop('data__coordinates__y')
    training_data = pd.concat([measured_x, measured_y], axis=1)

    reference_x = concatenated_df.pop('reference__x')
    reference_y = concatenated_df.pop('reference__y')
    reference_data = pd.concat([reference_x, reference_y], axis=1)

    # Zmiana wszystkich wartosci "nan" na zera
    verif_measured.fillna(0, inplace=True)
    verif_reference.fillna(0, inplace=True)
    training_data.fillna(0, inplace=True)
    reference_data.fillna(0, inplace=True)

    # Dodanie offsetu dla lepszego odczytu
    training_data = (training_data.astype('float32') + 2000) / 10000
    reference_data = (reference_data.astype('float32') + 2000) / 10000

    # Podzial danych treningowych na dane treningowe oraz walidacyjne
    rowCount = int(len(training_data))
    training_data_1 = training_data[:(9 * (rowCount//10))]
    reference_data_1 = reference_data[:(9 * (rowCount//10))]
    val_data_measured = training_data[(9 * (rowCount//10)):]
    val_data_reference = reference_data[(9 * (rowCount//10)):]
    val_data_measured.reset_index(drop=True, inplace=True)
    val_data_reference.reset_index(drop=True, inplace=True)

    # Dodanie offsetu dla lepszego odczytu
    verif_measured = (verif_measured.astype('float32') + 2000) / 10000
    verif_reference = (verif_reference.astype('float32') + 2000) / 10000

    # Utworzenie sieci
    model = tf.keras.Sequential([                                               #liczba epok - 150
        tf.keras.layers.Dense(64, activation=tf.nn.relu),                       #I warstwa ukryta - 64 neurony, funkcja aktywacyjna to ReLU
        tf.keras.layers.Dense(32, activation=tf.nn.relu),                       #II warstwa ukryta - 32 neurony, funkcja aktywacyjna to ReLU
        tf.keras.layers.Dense(16, activation=tf.nn.relu),                       #III warstwa ukryta - 16 neuronów, funkcja aktywacyjna to ReLU
        tf.keras.layers.Dense(8, activation=tf.nn.relu),                        #IV warstwa ukryta - 8 neuronów, funkcja aktywacyjna to ReLU
        tf.keras.layers.Dense(2, activation=tf.nn.sigmoid),                     #Warstwa wyjściowa - 2 neurony, funkcja aktywacyjna to funkcja sigmoidalna
    ])

    # Kompilacja sieci przy pomocy optymalizatora "Adam"
    model.compile(optimizer=tf.keras.optimizers.Adam(), loss=tf.keras.losses.MeanSquaredError(), metrics=['accuracy'])

    # Nauczanie sieci za pomoca danych statycznych
    model.fit(np.asarray(training_data_1), np.asarray(reference_data_1), epochs=150, batch_size=512,
              validation_data=(val_data_measured, val_data_reference))

    # Wypisanie wag neuronow
    model.evaluate(verif_measured, verif_reference, batch_size=512)
    weights = model.layers[0].get_weights()[0]
    print(weights)

    # Uzycie nauczonej juz sieci w celu przefiltrowania danych
    result = model.predict(verif_measured)
    result = result * 10000 - 2000
    result_df = pd.DataFrame(result)

    # Ulatwienie dostepu do danych poprzez przekazanie ich do list
    result_x_array = []
    result_y_array = []
    for x, y in result:
        result_x_array.append(x)
        result_y_array.append(y)
    reference_x_array = verif_reference_x.to_list()
    reference_y_array = verif_reference_y.to_list()
    measured_x_array = verif_measured_x.to_list()
    measured_y_array = verif_measured_y.to_list()

    # Blad pomiarowy
    error_filtered = []
    error_unfiltered = []
    for i in range(len(result_x_array)):
        buff_filtered = (np.sqrt(np.power(result_x_array[i] - reference_x_array[i], 2) + np.power(result_y_array[i] - reference_y_array[i], 2)))
        buff_unfiltered = (np.sqrt(np.power(measured_x_array[i] - reference_x_array[i], 2) + np.power(measured_y_array[i] - reference_y_array[i], 2)))
        error_filtered.append(buff_filtered)
        error_unfiltered.append(buff_unfiltered)
    result_df['error_filtered'] = error_filtered
    result_df['error_unfiltered'] = error_unfiltered

    # Wyeksportowanie danych do pliku excel
    result_df.to_excel('wynik_F10.xlsx', engine='xlsxwriter')
    print(result)