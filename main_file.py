from functions import *

swimmer_surname = input('Provide swimmers LASTNAME FIRSTNAME: ')
swimmers_list_df = get_page_source(swimmer_surname)
print(swimmers_list_df.to_string(index=False))

df_length = len(swimmers_list_df)
if df_length > 1:
    swimmer_nb = input('\nThere are more results for this search. Select specific swimmer: ')
    link_swimmer = swimmers_list_df.iloc[int(swimmer_nb) - 1, 4]
    swimmer = swimmers_list_df.iloc[int(swimmer_nb) - 1, 1]
elif df_length == 1:
    link_swimmer = swimmers_list_df.iloc[0, 4]
    swimmer = swimmers_list_df.iloc[0, 1]
else:
    print('No results found')
    quit()


swimmer_distances = get_swimmer_distances(link_swimmer)
link_distance_details = link_swimmer + '&styleId='
print('\n\n')
print(swimmer_distances.to_string(index=False))
distances_str = input('Select distances to compare. Provide distance codes separated with comma: ')
# distances_str = '20-SC,2-SC'
distances_tab = get_distances(distances_str)[0]
df_labels = get_distances(distances_str)[1]
results = get_results(distances_tab, link_distance_details)
draw_plots(results, df_labels, swimmer)
