# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages
updated_damages = []
for i in damages:
  if i == 'Damages not recorded':
    updated_damages.append('Damages not recorded')
  elif "B" in i[-1]:
    remove_B = float(i.replace("B",""))
    conversion_for_B = float(conversion.get("B"))
    updated_damages.append(remove_B * conversion_for_B)
  elif "M" in i[-1]:
    remove_M = float(i.replace("M",""))
    conversion_for_M = float(conversion.get("M"))
    updated_damages.append(remove_M * conversion_for_M)
print(updated_damages)

# 2 Create a Table
# Create and view the hurricanes dictionary
def create_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
  hurricanes = {}
  num_hurricanes = len(names)

  for i in range(num_hurricanes):
    hurricanes[names[i]] = {"Name": names[i], "Month": months[i], "Year": years[i], "Max Sustained Wind": max_sustained_winds[i], "Areas Affected": areas_affected[i], "Damage": updated_damages[i], "Deaths": deaths[i]}
  return hurricanes

hurricanes = create_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
#print(hurricanes)
print(hurricanes['Cuba I'])
print(hurricanes['Irma'])


# 3 Organizing by Year
# create a new dictionary of hurricanes with year and key

#cannot direct copy the function above as the years sometimes duplicate, which make the function skips the duplicated year for one of the different hurricanes.
# https://gist.github.com/codecademydev/5abbb8b1ad2c2d41b9e977bc1bb9fad1

#3 method 1
def hurricane_year(dict):
  new_dict = {}
  for i in dict: # i includes items of {canes:cane data}
    current_year = dict[i]['Year'] #cane year
    current_cane = dict[i]  #{canes:cane data}
    if current_year not in new_dict:
      new_dict[current_year] = [current_cane] # Add dict[i] as new {key:value) to new_dict[i]
    else: # if the year already exists in new_dict
      new_dict[current_year].append(current_cane) # Append dict[i] to a existing new_dict[i]
  return new_dict
hurricane_by_year = hurricane_year(hurricanes)
#print(hurricane_by_year[1932])

#3 method 2
def year_dict(dict):
    hurricane_years = {}   
    #for loop that checks if year in hurricane_years, and adds data 
    for data in dict.values():
        for year, lst in hurricane_years.items():
            if data['Year'] == year:
                lst.append(data)
        hurricane_years.update({data['Year']: [data]})
    return hurricane_years
hurricane_by_year_v2 = year_dict(hurricanes)
#print(hurricane_by_year[1932])

# 4 Counting Damaged Areas
# create dictionary of areas to store the number of hurricanes involved in

def area_count(dict):
  affected_count = {}
  for data in dict.values(): # i includes {key:value} for each {cane:cane data} in canes dict.
      for area in data['Areas Affected']: # i include values of "Areas Affected" in each cane.
          if area not in affected_count:
              affected_count[area] = 1
          else:
              affected_count[area] += 1 
  return affected_count
count_affected_areas = area_count(hurricanes)
print(count_affected_areas)

# 5 Calculating Maximum Hurricane Count
# find most frequently affected area and the number of hurricanes involved in

#https://stackoverflow.com/questions/13669252/what-is-lambda-in-python-code-how-does-it-work-with-key-arguments-to-sorte
# https://github.com/timbohmert/dev_courses/blob/master/Codecademy/hurricaneAnalysis/script.py#L100
# https://blogboard.io/blog/knowledge/python-sorted-lambda/
#https://gist.github.com/nktnlx/fc3f3e6f40d34c061d2bfcfe9a1ea367#file-hurricane_analysis-py-L93
#https://blogboard.io/blog/knowledge/python-tuples/

# 5 method 1 - k=lambda
def max_count():
    #uses max(dict_name.items(), key=lambda x: x[1])
    return max(count_affected_areas.items(), key=lambda i: i[1])
print(max_count()) # the output is tuple

# 5 method 2 - for loop + if
def most_affected_areas(count_affected_areas):
  most_affected = {}
  count = 0
  for k, v in count_affected_areas.items():
    if v > count:
      most_affected[k] = v
      count = v
  return most_affected
print(most_affected_areas(count_affected_areas)) # output remains {dict}

# 6 Calculating the Deadliest Hurricane
# find highest mortality hurricane and the number of deaths
#https://gist.github.com/nktnlx/fc3f3e6f40d34c061d2bfcfe9a1ea367#file-hurricane_analysis-py-L108

def greatest_death(dict):
  max_death = ""
  count = 0
  for i in dict:
    if dict[i]["Deaths"] > count:
      max_death = i # key in {hurricanes}
      count = dict[i]["Deaths"] # int in {hurricanes}["Deaths"]
  return max_death, count
max_death, count = greatest_death(hurricanes)
print("The greatest death is :" + str(greatest_death(hurricanes)))

# 7 Rating Hurricanes by Mortality
# categorize hurricanes in new dictionary with mortality severity as key
# https://gist.github.com/codecademydev/b0d3f9aac093e4e58b43d1b0b92d9d2b#file-script-py-L121

# 7 method 1
def mortality_scale(hurricanes):
  m_scale = {}
  zero_list = []
  one_list = []
  two_list = []
  three_list = []
  four_list = []
  for k, v in hurricanes.items():
    if hurricanes[k]["Deaths"] == 0:
     zero_list.append(v)
     m_scale[0] = zero_list
    elif hurricanes[k]["Deaths"] <= 100:
     one_list.append(v)
     m_scale[1] = one_list
    elif hurricanes[k]["Deaths"] <= 500:
     two_list.append(v)
     m_scale[2] = two_list
    elif hurricanes[k]["Deaths"] <= 1000:
     three_list.append(v)
     m_scale[3] = three_list
    elif hurricanes[k]["Deaths"] <= 10000:
     four_list.append(v)
     m_scale[4] = four_list
  return m_scale

m_scale = mortality_scale(hurricanes)
#for key in sorted(m_scale):
    #print("\n{} -- {}".format(key, m_scale[key]))

# 7 method 2 
def mortality_scale(dict):
  hurricane_by_mortality = {0:[], 1:[], 2:[], 3:[], 4:[]}
  for k, v in dict.items():
    if dict[k]["Deaths"] == 0:
     hurricane_by_mortality[0].append(v['Name']) 
    elif dict[k]["Deaths"] <= 100:
     hurricane_by_mortality[1].append(v['Name'])
    elif dict[k]["Deaths"] <= 500:
     hurricane_by_mortality[2].append(v['Name']) 
    elif dict[k]["Deaths"] <= 1000:
     hurricane_by_mortality[3].append(v['Name']) 
    elif dict[k]["Deaths"] <= 10000:
     hurricane_by_mortality[4].append(v['Name']) 
  return hurricane_by_mortality

mortality_scale_cat = mortality_scale(hurricanes)
for k, v in mortality_scale_cat.items():
  print("Category {category}: {hurricanes}".format(category = k, hurricanes = v))

# 8 Calculating Hurricane Maximum Damage
# find highest damage inducing hurricane and its total cost

def greatest_damage(dict):
  max_damage_cane = ""
  max_damage = 0
  for i in dict:
    if dict[i]["Damage"] == 'Damages not recorded':
      continue
    if dict[i]["Damage"] > max_damage:
      max_damage_cane = i # key in {hurricanes}
      max_damage = dict[i]["Damage"] # int in {hurricanes}["Value"]
  return max_damage_cane, max_damage
max_damage_cane, max_damage = greatest_damage(hurricanes)
print("The greatest damage is :" + str(greatest_damage(hurricanes)))

# 9 Rating Hurricanes by Damage
# categorize hurricanes in new dictionary with damage severity as key
def damage_scale(dict):
  damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}
  hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for i in dict: # using keys in {hurricanes}
    if dict[i]["Damage"] == 'Damages not recorded':
      hurricanes_by_damage[0].append(i)    
    elif dict[i]["Damage"] == damage_scale[0]:
      hurricanes_by_damage[0].append(i)
    elif dict[i]["Damage"] <= damage_scale[1]:
      hurricanes_by_damage[1].append(i) 
    elif dict[i]["Damage"] <= damage_scale[2]:
      hurricanes_by_damage[2].append(i) 
    elif dict[i]["Damage"] <= damage_scale[3]:
      hurricanes_by_damage[3].append(i) 
    elif dict[i]["Damage"] <= damage_scale[4]:
      hurricanes_by_damage[4].append(i) 
    elif dict[i]["Damage"] > damage_scale[4]:
      hurricanes_by_damage[5].append(i) 
  return hurricanes_by_damage

dam_scale = damage_scale(hurricanes)
for i in sorted(dam_scale):
  print("\n Damage scale {cat} ---> {cane}".format(cat = i, cane = dam_scale[i]))


