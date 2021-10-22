from functions import *

searched_swimmer = input('Provide swimmers LASTNAME FIRSTNAME: ')
swimmers_list = get_page_source(searched_swimmer)
print(swimmers_list.to_string(index=False))
swimmer_params = get_specific_swimmer(swimmers_list)
link_swimmer = swimmer_params[0]
swimmer = swimmer_params[1]
swimmer_distances = get_swimmer_distances(link_swimmer)
link_distance_details = link_swimmer + '&styleId='
print('\n\n')
print(swimmer_distances.to_string(index=False))
distances_str = input('Select distances to compare. Provide distance codes separated with comma: ')
distances_params = get_distances_to_compare(distances_str)[0]
distances_labels = get_distances_to_compare(distances_str)[1]
results_all = get_results(distances_params, link_distance_details, 'multi-dist')
draw_plots(results_all, distances_labels, swimmer)
