import math

EarthEquaRad = 6378.14      # Earth raduis on the equator
GeoRad = 42164.17           # Geostationary orbit raduis 
GeoAlt = 35786              # GSO altitude
EccOfEarth = 0.08182        # Eccentricity of the Earth

# Default values
Azim = 0.0
EarthStaLat = 100.0
EarthStaLon = 200.0
SatLong = 200.0

# While and if control statments for user input errors
while EarthStaLat < -90 or EarthStaLat > 90:
    EarthStaLat = float(input("Input your  in degrees: "))
    if EarthStaLat < -90 or EarthStaLat > 90:
        print("---Please input a valid latitude value---\n")
while EarthStaLon < -180 or EarthStaLon > 180:
    EarthStaLon = float(input("Input your longitude in degrees: "))
    if EarthStaLon < -180 or EarthStaLon > 180:
        print("---Please input a valid longitude value---\n")
EarthStaAlt = float(input("Input your altitude in Kilometers: "))
while SatLong < -180 or SatLong > 180:
    SatLong = float(input("Input the satellite longitude in degrees: "))
    if SatLong < -180 or SatLong > 180:
        print("---Please input a valid longitude value---\n")

EarthStaLat = math.radians(EarthStaLat)
EarthStaLon = math.radians(EarthStaLon)
SatLong = math.radians(SatLong)

B = EarthStaLon - SatLong
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
print ("\nThe Elevation Angle of the satellite:\n\tθ = ", Elev, " degrees")

if EarthStaLat < 0:
    if EarthStaLon < SatLong:         # If the satellite is North East of the Earth station
        InterAngleAi = math.degrees(math.asin(math.sin(abs(B)) / math.sin(beta)))
        Azim = InterAngleAi
    elif EarthStaLon > SatLong:       # If the satellite is North West of the Earth station
        InterAngleAi = math.degrees(math.asin(math.sin(abs(B)) / math.sin(beta)))
        Azim = 360 - InterAngleAi
    else:                               # If the satellite is on the same longitude and North of the Earth station
        Azim = 0
elif EarthStaLat > 0:
    if EarthStaLon < SatLong:         # If the satellite is South East of the Earth station
        InterAngleAi = math.degrees(math.asin(math.sin(abs(B)) / math.sin(beta)))
        Azim = 180 - InterAngleAi
    elif EarthStaLon > SatLong:       # If the satellite is South West of the Earth station
        InterAngleAi = math.degrees(math.asin(math.sin(abs(B)) / math.sin(beta)))
        Azim = 180 + InterAngleAi
    else:                               # If the satellite is on the same longitude and South of the Earth station
        Azim = 180
else:
    if EarthStaLon > SatLong:         # If the satellite is on the same latitude and East of the Earth station
        Azim = 90
    elif EarthStaLon < SatLong:       # If the satellite is on the same latitude and West of the Earth station
        Azim = 270
    else:                               # If the satellite dirctly above the Earth station
        print ("\nThe Azimuth of the satellite is unidentefied\nsince the satellite is directly above the Earth station.\n")

if EarthStaLat != 0 or EarthStaLon != SatLong:
    print ("\nThe Azimuth of the satellite:\n\tφ = ", Azim, " degrees")

