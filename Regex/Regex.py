import re
text = """ Cyclones have also been seen on planets other than the Earth, such as Mars, Jupiter, and Neptune.[5][6] Cyclogenesis is the process of cyclone formation and intensification.[7]\n
Extratropical cyclones begin as waves in large regions of enhanced mid-latitude temperature contrasts called baroclinic zones. These zones contract and form weather fronts as the cyclonic circulation closes and intensifies. Later in their life cycle, extratropical cyclones occlude as cold air masses undercut the warmer air and become cold core systems. A cyclone's track is guided over the course of its 2 to 6 day life cycle by the steering flow of the subtropical jet stream. Dyclone\rWeather a2 fronts mark \\ marks the boundary between two masses of air of different temperature, humidity, and densities, and are associated with the most prominent meteorological phenomena. Strong cold fronts typically feature narrow bands of thunderstorms and severe weather, and may on occasion be preceded by squall lines or dry lines. Such fronts form west of the circulation center and generally move from west to east; warm fronts form east of the cyclone center and are usually preceded by stratiform precipitation and fog. Warm fronts move poleward ahead of the cyclone path. Occluded fronts form late in the cyclone life cycle near the center of the cyclone and often wrap around the storm center.
333-555-777
123.456.789
"""
# pattern="[A-Z]+yclone"

# matches = re.search(pattern,text)   #this search for the pattern or word then stop when find the word
# Only the first occurance

# matches = re.finditer(pattern,text)
# for match in matches:
#     print(match)
# for match in matches:
#     print(type(match))
#     print(match.span())
#     # print(text[match.span()[0]:match.span()[1]])
#     print(match.group()) #that groupe up the whole word like cyclone
# # print(matches)

# matche=re.findall(pattern, text)
# print(matche)
#print the pattern in the form of the list

# print(re.findall(r"c......s",text))

# pattern = r"\\"
# print(re.findall(pattern,text))

# # print(re.findall(r"^Cyclones ", text))     # ✅
# # print(re.findall(r"Cyclones", text))
# print(text)

# pattern = re.compile(r"[89]00[-.]\d\d\d[-.]\d\d\d")
# pattern = re.compile(r"[^A-Za-z]")
# print(re.findall(pattern, text))

# pattern=re.compile(r"[^b]at") #here the ^ is acting as not inside the []

# pattern= re.compile(r"\d{3}.\d{3}.\d{4}")   #quantifier {3} Exact Number


# pattern=re.compile(r"M(r|rs|s)\.?\s[A-Z]\w*")  #? check whether having the character or One
# + qunatifiers that add 1 or more character present in the text
# * quantifier that matck the 0 or more character 
#() group the charter that want to match
#| either org

pattern = re.compile(r'[\w]+@[\w]+\.com')
with open(r'Regex\data.txt','r')as f:
    content= f.read()

    matches = pattern.finditer(content)

    for match in matches:
        print(match)

