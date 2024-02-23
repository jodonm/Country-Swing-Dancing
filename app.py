import streamlit as st
import folium


def main():
    st.title("Best places for country swing dancing")
    
    # Define custom locations
    locations_data = [
        ([46.73489782122985, -117.00119446375352], "Moose Lodge: Dance hall popular with university students. Dancing every Wednesday night from 9PM-12AM when school is in session. $5 cover. <a href='https://www.facebook.com/Palousecountryswing' target='_blank'>Facebook</a>"),
        ([47.707297013906306, -117.03240164407349], "Nashville North: Country Bar. Live music and dancing Friday & Saturday night. $5 Cover. <a href='https://www.thenashvillenorth.com' target='_blank'>Website</a>"),
        ([43.620422691638765, -116.30959909439918], "CLOSED. The Buffalo Club: Country Bar. Live music and dancing. Older music. Also popular with other swing styles. <a href='http://thebuffaloclubboise.com/' target='_blank'>Website</a>"),
        ([43.49129480402318, -116.42184487417322], "127 Saloon: Popular country swing bar. Small dance floor but lots of talented dancers. <a href='http://127saloon.com/' target='_blank'>Website</a>"),
        ([48.371103555952686, -114.24033149339925], "Blue Moon Nite Club: Popular bar with locals. Not always a country band but still the best place to dance on weekends."),
        ([47.60170817943568, -122.63077979283953], "McClouds Grill House: Best bar in the Kitsap area for country swing dancing. <a href='https://mccloudsgrillhouse.com/' target='_blank'>Website</a>"),
        ([45.68771311088347, -111.04463165736743], "Bourbon: Popular spot for country swing dancing on Saturday nights <a href='http://www.bourbonmt.com/' target='_blank'>Website</a>"),
        ([43.61400379346505, -116.2012090487591], "Dirty Little Roddy's: Very popular night club with western theme. Not the best for country dancing but you might see some when it's less crowded. <a href='https://dirtylittleroddys.com/' target='_blank'>Website</a>"),
        ([39.795162070087386, -104.98699700682839], "The Grizzly Rose: Popular country bar with live country music Tuesday-Sunday. Frequently hosts concerts. Has lessons several times throughout the week. <a href='https://www.grizzlyrose.com/' target='_blank'>Website</a>"),
        ([39.6723121325138, -104.86528727753583], "Stampede: Large dance floor. Wednesday night is country night with line-dance lessons. <a href='https://www.stampedeclub.net/' target='_blank'>Website</a>"),
        ([40.69926787373029, -111.9392146616003], "Westerner Club: Popular for country swing and other swing styles. Lessons Wednesday through Saturday <a href='http://www.westernerslc.com/' target='_blank'>Website</a>"),
        ([46.20845072481442, -119.12093024559294], "Branding Iron: Live bands and line dance lessons Friday & Saturday <a href='https://brandingironnightclub.com/' target='_blank'>Website</a>"),
        ([45.3799076112494, -122.7608340607681], "Bushwackers: Largest country swing bar in Portland. Lessons Thursday through Saturday <a href='http://www.bushwhackerssaloon.com/' target='_blank'>Website</a>"),
        ([45.59734393114103, -122.66874347632411], "Ponderosa Bar & Grill (AKA Jubitz): Country swing dancing at a truck-stop bar. Old-timey feel. <a href='http://jubitz.com/ponderosa-lounge-country-bar/' target='_blank'>Website</a>"),
        # Add more custom locations with their descriptions
    ]


    # Display the map with custom markers
    display_map(locations_data)




def display_map(locations_data):
    # Extract only the locations for calculating map_center
    locations = [location for location, _ in locations_data if location]

    filtered_locations_data = [data for data in locations_data if data[0] is not None]

    if locations:
    

        # Calculate map center based on the mean of custom locations
        map_center = [sum([lat for lat, lon in locations]) / len(locations),
                    sum([lon for lat, lon in locations]) / len(locations)]

        my_map = folium.Map(location=map_center, zoom_start=4)

        # Function to add marker with popup to the map
        def add_marker(map_obj, location, popup_content):
            popup = folium.Popup(f"<p1>{popup_content}</p1>", max_width=300)
            marker = folium.Marker(location, draggable=False, title="", opacity=0.75, popup=popup)
            marker.add_to(map_obj)

        # Add custom markers to the map
        for location, popup_content in locations_data:
            add_marker(my_map, location, popup_content)

        # Display the map using Streamlit
        map_html = my_map._repr_html_()
        st.components.v1.html(
            f'<div style="display: flex; justify-content: center; align-items: center; height: 100%; width: 100%;">'
            f'{map_html}</div>', height=1000, width=1000)

if __name__ == "__main__":
    main()
