import math

EARTH_EQUA_RAD = 6378.14        # Earth raduis on the equator
EARTH_ECCENT = 0.08182          # Eccentricity of the Earth
GEO_RAD = 42164.17              # Geostationary orbit raduis 
GEO_ALT = 35786                 # GSO altitude

# Default values
azim = 0.0
earth_sta_lat = 100.0
earth_sta_lon = 200.0
sat_long = 200.0

# While and if control statments for user input errors
while earth_sta_lat < -90 or earth_sta_lat > 90:
    earth_sta_lat = float(input("Input your latitude in degrees: "))
    if earth_sta_lat < -90 or earth_sta_lat > 90:
        print("---Please input a valid latitude value---\n")
while earth_sta_lon < -180 or earth_sta_lon > 180:
    earth_sta_lon = float(input("Input your longitude in degrees: "))
    if earth_sta_lon < -180 or earth_sta_lon > 180:
        print("---Please input a valid longitude value---\n")
EarthStaAlt = float(input("Input your altitude in Kilometers: "))
while sat_long < -180 or sat_long > 180:
    sat_long = float(input("Input the satellite longitude in degrees: "))
    if sat_long < -180 or sat_long > 180:
        print("---Please input a valid longitude value---\n")

earth_sta_lat = math.radians(earth_sta_lat)
earth_sta_lon = math.radians(earth_sta_lon)
sat_long = math.radians(sat_long)

# Differential longitude
diff_lon = earth_sta_lon - sat_long

beta = math.acos(math.cos(diff_lon) * math.cos(earth_sta_lat))

l = ((EARTH_EQUA_RAD / math.sqrt(1 - pow(EARTH_ECCENT, 2) * pow(math.sin(earth_sta_lat), 2))) + EarthStaAlt) * math.cos(earth_sta_lat)
z = ((EARTH_EQUA_RAD * (1 - pow(EARTH_ECCENT, 2)) / math.sqrt(1 - pow(EARTH_ECCENT, 2) * pow(math.sin(earth_sta_lat), 2))) + EarthStaAlt) * math.sin(earth_sta_lat)

# Calculate the Raduis to the center of the Earth from the ground station
sta_rad = math.sqrt(l ** 2 + z ** 2)
# Calculate the intermediate angle Ψᴇ
inter_angle_psi = math.atan(z/ l)
# Calculate the Range to the satellite
range = math.sqrt(pow(sta_rad, 2) + pow(GEO_RAD, 2) - 2 * sta_rad * GEO_RAD * math.cos(inter_angle_psi) *  math.cos(diff_lon))
# Calculate the Elevation Angle of the satellite
elev = math.degrees(math.acos(((EARTH_EQUA_RAD + GEO_ALT) / range) * math.sqrt(1 - pow(math.cos(diff_lon), 2) * pow(math.cos(earth_sta_lat), 2))))

# Print the results
print (f"\nThe Range/distance to the satellite:\n\td = {range} km")
print (f"\nThe Elevation Angle of the satellite:\n\tθ = {elev}°")

if earth_sta_lat < 0:
    if earth_sta_lon < sat_long:         # If the satellite is North East of the Earth station
        inter_angle_ai = math.degrees(math.asin(math.sin(abs(diff_lon)) / math.sin(beta)))
        azim = inter_angle_ai
    elif earth_sta_lon > sat_long:       # If the satellite is North West of the Earth station
        inter_angle_ai = math.degrees(math.asin(math.sin(abs(diff_lon)) / math.sin(beta)))
        azim = 360 - inter_angle_ai
    else:                                # If the satellite is on the same longitude and North of the Earth station
        azim = 0
elif earth_sta_lat > 0:
    if earth_sta_lon < sat_long:         # If the satellite is South East of the Earth station
        inter_angle_ai = math.degrees(math.asin(math.sin(abs(diff_lon)) / math.sin(beta)))
        azim = 180 - inter_angle_ai
    elif earth_sta_lon > sat_long:       # If the satellite is South West of the Earth station
        inter_angle_ai = math.degrees(math.asin(math.sin(abs(diff_lon)) / math.sin(beta)))
        azim = 180 + inter_angle_ai
    else:                                # If the satellite is on the same longitude and South of the Earth station
        azim = 180
else:
    if earth_sta_lon > sat_long:         # If the satellite is on the same latitude and East of the Earth station
        azim = 90
    elif earth_sta_lon < sat_long:       # If the satellite is on the same latitude and West of the Earth station
        azim = 270
    else:                                # If the satellite dirctly above the Earth station
        print ("\nThe Azimuth of the satellite is unidentefied\nsince the satellite is directly above the Earth station.\n")

if earth_sta_lat != 0 or earth_sta_lon != sat_long:
    print (f"\nThe Azimuth of the satellite:\n\tφ = {azim}°")

