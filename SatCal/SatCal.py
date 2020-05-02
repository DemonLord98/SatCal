import math

EarthEquaRad = 6378.14          # Earth raduis on the equator
GeoRad = 42164.17           # Geostationary orbit raduis 
GeoAlt = 35786              # GSO altitude
EccOfEarth = 0.08182        # Eccentricity of the Earth

EarthStaLat = math.radians(float(input("Input your latitude in degrees: ")))
EarthStaLon = math.radians(float(input("Input your longitude in degrees: ")))
EarthStaAlt = float(input("Input your altitude in Kilometers: "))
SatStaLon = math.radians(float(input("Input the satellite longitude: ")))

B = EarthStaLon - SatStaLon

l = ((EarthEquaRad / math.sqrt(1 - pow(EccOfEarth, 2) * pow(math.sin(EarthStaLat), 2))) + EarthStaAlt) * math.cos(EarthStaLat)
z = ((EarthEquaRad * (1 - pow(EccOfEarth, 2)) / math.sqrt(1 - pow(EccOfEarth, 2) * pow(math.sin(EarthStaLat), 2))) + EarthStaAlt) * math.sin(EarthStaLat)

# Calculate the Raduis to the center of the Earth from the ground station
StaRad = math.sqrt(l ** 2 + z ** 2)
# Calculate the intermediate angle ΨE
InterAngle = math.atan(z/ l)
# Calculate the Range to the satellite
d = math.sqrt(pow(StaRad, 2) + pow(GeoRad, 2) - 2 * StaRad * GeoRad * math.cos(InterAngle) *  math.cos(B))
# Calculate the Elevation Angle of the satellite
phi = math.acos(((EarthEquaRad + GeoAlt) / d) * math.sqrt(1 - pow(math.cos(B), 2) * pow(math.cos(EarthStaLat), 2)))

# Print the results
print ("\nThe Range/distance to the satellite:\n\td = ", d)
print ("\nThe Elevation Angle of the satellite:\n\tΦ = ", math.degrees(phi))

