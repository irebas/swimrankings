from functions import *

searched_swimmer = input('Provide swimmers LASTNAME FIRSTNAME: ')
swimmers_list_df = get_page_source(searched_swimmer)
print(swimmers_list_df.to_string(index=False))
swimmer_params = get_specific_swimmer(swimmers_list_df)
link_swimmer = swimmer_params[0]
swimmer = swimmer_params[1]
swimmer_distances = get_swimmer_distances(link_swimmer)
link_distance_details = link_swimmer + '&styleId='
print('\n\n')
print(swimmer_distances.to_string(index=False))
distances_str = input('Select distances to compare. Provide distance codes separated with comma: ')
distances_tab = get_distances(distances_str)[0]
df_labels = get_distances(distances_str)[1]
results = get_results(distances_tab, link_distance_details)
draw_plots(results, df_labels, swimmer)
#DRIVER.quit()