import pandas as pd
# DISTANCES_CODES_DATA = {
#     'Order': list(range(1,35)),
#     'Code': ['1-SC', '1-LC', '2-SC', '2-LC', '3-SC', '3-LC', '5-SC', '5-LC', '6-SC', '6-LC', '7-SC', '7-LC',
#              '9-SC', '9-LC', '10-SC', '10-LC', '11-SC', '11-LC', '12-SC', '12-LC', '13-SC', '13-LC', '14-SC', '14-LC',
#              '15-SC', '15-LC', '16-SC', '16-LC', '17-SC', '17-LC', '20-SC', '18-SC', '18-LC', '19-SC', '19-LC'],
#     'Distance': ['50m Free SC', '50m Free LC', '100m Free SC', '100m Free LC', '200m Free SC', '200m Free LC',
#                  '400m Free SC', '400m Free LC', '800m Free SC', '800m Free LC', '1500m Free SC', '1500m Free LC',
#                  '50m Back SC', '50m Back LC', '100m Back SC', '100m Back LC', '200m Back SC', '200m Back LC',
#                  '50m Breast SC', '50m Breast LC', '100m Breast SC', '100m Breast LC', '200m Breast SC',
#                  '200m Breast LC',
#                  '50m Fly SC', '50m Fly LC', '100m Fly SC', '100m Fly LC', '200m Fly SC', '200m Fly LC',
#                  '100m IM SC', '200m IM SC', '200m IM LC', '400m IM SC', '400m IM LC']}
#
#
# DISTANCES_CODES = pd.DataFrame(DISTANCES_CODES_DATA, columns=['Order', 'Code', 'Distance'])
#
#
#


df = pd.DataFrame({'Course': ['50 free SC', '50 free LC', '100 free SC'], 'Code': ['1-SC', '1-LC', '2-SC']}, columns=['Course', 'Code'])

x = list(range(1,36))
print(x)
print(len(x))
df = df[['Code','Course']]

print(df)


