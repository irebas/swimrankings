import pandas as pd

DISTANCES_IDS_DATA = {'Distance': ['50m Libre', '100m Libre', '200m Libre', '400m Libre',
                                   '800m Libre', '1500m Libre', '50m Espalda', '100m Espalda',
                                   '200m Espalda', '50m Braza', '100m Braza', '200m Braza',
                                   '50m Mariposa', '100m Mariposa', '200m Mariposa', '100m Estilos',
                                   '200m Estilos', '400m Estilos', '50m Dowolny', '100m Dowolny', '200m Dowolny',
                                   '400m Dowolny', '800m Dowolny', '1500m Dowolny', '50m Grzbietowy', '100m Grzbietowy',
                                   '200m Grzbietowy', '50m Klasyczny', '100m Klasyczny', '200m Klasyczny',
                                   '50m Motylkowy', '100m Motylkowy', '200m Motylkowy', '100m Zmienny',
                                   '200m Zmienny', '400m Zmienny', '50m Freestyle', '100m Freestyle', '200m Freestyle',
                                   '400m Freestyle', '800m Freestyle', '1500m Freestyle', '50m Backstroke',
                                   '100m Backstroke', '200m Backstroke', '50m Breaststroke', '100m Breaststroke',
                                   '200m Breaststroke', '50m Butterfly', '100m Butterfly', '200m Butterfly', '100m IM',
                                   '200m IM', '400m IM'],
                      'ID': [1, 2, 3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 20, 18, 19, 1, 2, 3, 5, 6, 7, 9, 10,
                             11, 12, 13, 14, 15, 16, 17, 20, 18, 19, 1, 2, 3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16,
                             17, 20, 18, 19]}

DISTANCES_CODES_DATA = {
    'Order': list(range(1, 36)),
    'Code': ['1-SC', '1-LC', '2-SC', '2-LC', '3-SC', '3-LC', '5-SC', '5-LC', '6-SC', '6-LC', '7-SC', '7-LC',
             '9-SC', '9-LC', '10-SC', '10-LC', '11-SC', '11-LC', '12-SC', '12-LC', '13-SC', '13-LC', '14-SC', '14-LC',
             '15-SC', '15-LC', '16-SC', '16-LC', '17-SC', '17-LC', '20-SC', '18-SC', '18-LC', '19-SC', '19-LC'],
    'Distance': ['50m Free SC', '50m Free LC', '100m Free SC', '100m Free LC', '200m Free SC', '200m Free LC',
                 '400m Free SC', '400m Free LC', '800m Free SC', '800m Free LC', '1500m Free SC', '1500m Free LC',
                 '50m Back SC', '50m Back LC', '100m Back SC', '100m Back LC', '200m Back SC', '200m Back LC',
                 '50m Breast SC', '50m Breast LC', '100m Breast SC', '100m Breast LC', '200m Breast SC',
                 '200m Breast LC',
                 '50m Fly SC', '50m Fly LC', '100m Fly SC', '100m Fly LC', '200m Fly SC', '200m Fly LC',
                 '100m IM SC', '200m IM SC', '200m IM LC', '400m IM SC', '400m IM LC']}

DISTANCES_IDS = pd.DataFrame(DISTANCES_IDS_DATA, columns=['Distance', 'ID'])
DISTANCES_CODES = pd.DataFrame(DISTANCES_CODES_DATA, columns=['Order', 'Code', 'Distance'])

COLORS = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']

MONTHS_EN = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
MONTHS_PL = ['Sty', 'Lut', 'Mar', 'Kwi', 'Maj', 'Cze', 'Lip', 'Sie', 'Wrz', 'Paź', 'Lis', 'Gru']
