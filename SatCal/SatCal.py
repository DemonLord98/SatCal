import math

EarthRad = 6378.14
GeoRad = 42164.17
GeoAlt = 35786
EccOfEarth = 0.08182

EarthStaLat = math.radians(float(input("Input your latitude in degrees: ")))
EarthStaLon = math.radians(float(input("Input your longitude in degrees: ")))
EarthStaAlt = float(input("Input your altitude in Kilometers: "))
SatStaAlt = math.radians(float(input("Input the satellite longitude: ")))


l = ((EarthRad / math.sqrt(1 - pow(EccOfEarth, 2) * pow(math.sin(EarthStaLat), 2))) + EarthStaAlt) * math.cos(EarthStaLat)
z = ((EarthRad * (1 - pow(EccOfEarth, 2)) / math.sqrt(1 - pow(EccOfEarth, 2) * pow(math.sin(EarthStaLat), 2))) + EarthStaAlt) * math.sin(EarthStaLat)

R = math.sqrt(l ** 2 + z ** 2)
InterAngle = math.atanh(z/ l)
B = EarthStaLon - SatStaAlt
d = math.sqrt(pow(R, 2) + pow(GeoRad, 2) - 2 * R * GeoRad * math.cos(InterAngle) *  math.cos(B))

print ("\nRaduis to the center of the Earth from the ground station:\n\tR = ",R)
print ("\nThe intermediate angle Ψ:\n\tΨ = ",InterAngle)
print ("\nThe distance to the satellite:\n\td = ",d)
