import math

EarthRad = 6378.14          # Earth raduis on the equator
GeoRad = 42164.17           # Geostationary orbit raduis 
GeoAlt = 35786              # GSO altitude
EccOfEarth = 0.08182        # Eccentricity of the Earth

EarthStaLat = math.radians(float(input("Input your latitude in degrees: ")))
EarthStaLon = math.radians(float(input("Input your longitude in degrees: ")))
EarthStaAlt = float(input("Input your altitude in Kilometers: "))
SatStaLon = math.radians(float(input("Input the satellite longitude: ")))


l = ((EarthRad / math.sqrt(1 - pow(EccOfEarth, 2) * pow(math.sin(EarthStaLat), 2))) + EarthStaAlt) * math.cos(EarthStaLat)
z = ((EarthRad * (1 - pow(EccOfEarth, 2)) / math.sqrt(1 - pow(EccOfEarth, 2) * pow(math.sin(EarthStaLat), 2))) + EarthStaAlt) * math.sin(EarthStaLat)

# Calculate the Raduis to the center of the Earth from the ground station
StaRad = math.sqrt(l ** 2 + z ** 2)
# Calculate the intermediate angle ΨE
InterAngle = math.tanh(z/ l)
B = EarthStaLon - SatStaLon
# Calculate the Range to the satellite
d = math.sqrt(pow(StaRad, 2) + pow(GeoRad, 2) - 2 * StaRad * GeoRad * math.cos(InterAngle) *  math.cos(B))


print ("\nThe Range/distance to the satellite:\n\td = ",d)

