from pprint import pprint

import osmnx as ox
import geopandas as gpd
import networkx as nx


BASE="http://127.0.0.1:5000/"

def find_route(CITY: str = 'North York, Toronto, Canada',
               FROM: str = "648 Sheppard Ave W, North York, ON M3H 2S1",
               TO: str = "5100 Yonge St, North York, ON M2N 5V7",
               mode: str = 'drive',
               build_map: bool = False):

    def geocode_address(address, crs=4326):
        geocode = gpd.tools.geocode(address, provider='nominatim',
                                    user_agent="drive time demo").to_crs(crs)
        return (geocode.iloc[0].geometry.y, geocode.iloc[0].geometry.x)

    G = ox.graph_from_place(CITY, network_type=mode)

    G = ox.add_edge_speeds(G)
    G = ox.add_edge_travel_times(G)

    origin_point = geocode_address(FROM)
    destination_point = geocode_address(TO)

    orig_node = ox.distance.nearest_nodes(G, origin_point[1], origin_point[0])
    destination_node = ox.distance.nearest_nodes(G, destination_point[1], destination_point[0])
    # print(orig_node)
    # print(destination_node)
    route = nx.shortest_path(G, orig_node, destination_node, weight='travel_time')

    #############################################################
    edge_lengths = ox.utils_graph.get_route_edge_attributes(
        G, route, 'length')
    edge_travel_time = ox.utils_graph.get_route_edge_attributes(
        G, route, 'travel_time')
    total_route_length = sum(edge_lengths)
    route_travel_time = sum(edge_travel_time)
    #############################################################
    route_cord = {}
    for i in route:
        route_cord[G.nodes[i]['y']] = G.nodes[i]['x']

    if build_map:
        ox.plot_graph_route(G, route, node_size=0, figsize=(40, 40))

    return {
        'route_length': round(total_route_length / 1000,3),
        'travel_time': round(route_travel_time / 60,3),
        'route': route_cord
    }


# pprint(find_route(CITY='San Francisco, California, United States', FROM='1669 Fillmore St',
#                     TO='1831 Market St',mode='drive', build_map=True), sort_dicts=False)
