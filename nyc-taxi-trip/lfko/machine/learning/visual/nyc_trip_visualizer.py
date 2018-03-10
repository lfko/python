'''
Created on Feb 3, 2018

@author: lfko
'''

'''
 Um ein besseres Verstaendnis des Datensets zu erlangen, sollen hier einige Visualisierungen getestet werden
'''

# Laden der Daten
import pandas as pd
# Verarbeitung
import numpy as np
# Darstellung (Plotten)
from matplotlib import pyplot as plt


def main():
    data_uri = "../csv/yellow_tripdata_2017-01.csv"
    dataset = pd.read_csv(data_uri)
    
    # Konvertiere beide Spalten in ein DateTime
    dataset['pickup_datetime'] = pd.to_datetime(dataset['pickup_datetime'])
    dataset['dropoff_datetime'] = pd.to_datetime(dataset['dropoff_datetime'])

    print(dataset.dtypes)

    # Die ersten 10 Zeilen ausgeben
    print(dataset.head(10))
    # plot_categorical_data(dataset)
    plot_correlation_data(dataset)


def plot_categorical_data(dataset):
    
    # unnoetige Spalten entfernen
    drop_list = ['pickup_datetime', 'dropoff_datetime', 'trip_distance', 'PULocationID', 'DOLocationID', 'fare_amount', 'extra', 'mta_tax', 'tip_amount', 'tolls_amount', 'improvement_surcharge', 'total_amount' ]
    dataset.drop(drop_list, inplace=True, axis=1)
    
    # print(dataset.head(10))
    
    dataset['VendorID'].value_counts().plot(kind='bar')
    # plt.show()
    # Wartet hier, bis Plot geschlossen wurde

    dataset['passenger_count'].value_counts(sort=True).plot(kind='bar').set_title('Passenger count')
    plt.show()
    
    dataset['RatecodeID'].value_counts(sort=True).plot(kind='bar').set_title('Ratecode ID')
    plt.show()
    
    dataset['payment_type'].value_counts(sort=True).plot(kind='bar').set_title('Payment type')
    plt.show()
    
    None

    
def plot_correlation_data(dataset):
    
    # Berechne die Differenz und konvertie zu Sekunden
    # dataset['trip_time_in_sec'] = (dataset['dropoff_datetime'] - dataset['pickup_datetime']) / np.timedelta64(1, 's')
    # in Minuten
    dataset['trip_time_in_sec'] = (dataset['dropoff_datetime'] - dataset['pickup_datetime'])
    print(dataset['trip_time_in_sec'][1].total_seconds())
    print(dataset['trip_distance'].head(10))
    
    # plt.scatter(dataset['trip_time_in_sec'], dataset['trip_distance'], color='r', marker='^', alpha=.4)
    # plt.show()
    None    


if __name__ == '__main__':
    main()
