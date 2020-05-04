import math

EarthEquaRad = 6378.14      # Earth raduis on the equator
GeoRad = 42164.17           # Geostationary orbit raduis 
GeoAlt = 35786              # GSO altitude
EccOfEarth = 0.08182        # Eccentricity of the Earth

EarthStaLat = math.radians(float(input("Input your latitude in degrees: ")))
EarthStaLon = math.radians(float(input("Input your longitude in degrees: ")))
EarthStaAlt = float(input("Input your altitude in Kilometers: "))
SatStaLon = math.radians(float(input("Input the satellite longitude in degrees: ")))

B = EarthStaLon - SatStaLon
beta = math.acos(math.cos(B) * math.cos(EarthStaLat))

l = ((EarthEquaRad / math.sqrt(1 - pow(EccOfEarth, 2) * pow(math.sin(EarthStaLat), 2))) + EarthStaAlt) * math.cos(EarthStaLat)
z = ((EarthEquaRad * (1 - pow(EccOfEarth, 2)) / math.sqrt(1 - pow(EccOfEarth, 2) * pow(math.sin(EarthStaLat), 2))) + EarthStaAlt) * math.sin(EarthStaLat)

# Calculate the Raduis to the center of the Earth from the ground station
StaRad = math.sqrt(l ** 2 + z ** 2)
# Calculate the intermediate angle Ψᴇ
InterAnglePsi = math.atan(z/ l)
# Calculate the Range to the satellite
d = math.sqrt(pow(StaRad, 2) + pow(GeoRad, 2) - 2 * StaRad * GeoRad * math.cos(InterAnglePsi) *  math.cos(B))
# Calculate the Elevation Angle of the satellite
Elev = math.degrees(math.acos(((EarthEquaRad + GeoAlt) / d) * math.sqrt(1 - pow(math.cos(B), 2) * pow(math.cos(EarthStaLat), 2))))

# Print the results
print ("\nThe Range/distance to the satellite:\n\td = ", d, " km")
print ("\nThe Elevation Angle of the satellite:\n\tΦ = ", Elev, " degrees")

if EarthStaLat < 0:
    if EarthStaLon < SatStaLon:         # If the satellite is North East of the Earth station
        InterAngleAi = math.degrees(math.asin(math.sin(abs(B)) / math.sin(beta)))
        Azim = InterAngleAi
        print ("\nThe Azimuth of the satellite:\n\tφ = ", Azim, " degrees")
    elif EarthStaLon > SatStaLon:       # If the satellite is North West of the Earth station
        InterAngleAi = math.degrees(math.asin(math.sin(abs(B)) / math.sin(beta)))
        Azim = 360 - InterAngleAi
        print ("\nThe Azimuth of the satellite:\n\tφ = ", Azim, " degrees")
    else:                               # If the satellite is on the same longitude and North of the Earth station
        Azim = 0
        print ("\nThe Azimuth of the satellite:\n\tφ = ", Azim, " degrees")
elif EarthStaLat > 0:
    if EarthStaLon < SatStaLon:         # If the satellite is South East of the Earth station
        InterAngleAi = math.degrees(math.asin(math.sin(abs(B)) / math.sin(beta)))
        Azim = 180 - InterAngleAi
        print ("\nThe Azimuth of the satellite:\n\tφ = ", Azim, " degrees")
    elif EarthStaLon > SatStaLon:       # If the satellite is South West of the Earth station
        InterAngleAi = math.degrees(math.asin(math.sin(abs(B)) / math.sin(beta)))
        Azim = 180 + InterAngleAi
        print ("\nThe Azimuth of the satellite:\n\tφ = ", Azim, " degrees")
    else:                               # If the satellite is on the same longitude and South of the Earth station
        Azim = 180
        print ("\nThe Azimuth of the satellite:\n\tφ = ", Azim, " degrees")
else:
    if EarthStaLon > SatStaLon:         # If the satellite is on the same latitude and East of the Earth station
        Azim = 90
        print ("\nThe Azimuth of the satellite:\n\tφ = ", Azim, " degrees")
    elif EarthStaLon < SatStaLon:       # If the satellite is on the same latitude and West of the Earth station
        Azim = 270
        print ("\nThe Azimuth of the satellite:\n\tφ = ", Azim, " degrees")
    else:                               # If the satellite dirctly above the Earth station
        print ("\nThe Azimuth of the satellite is unidentefied\nsince the satellite is directly above the Earth station.\n")

