import math

height = 5
max_range = 101
range = range(max_range)
base_radius = 1
cylinder_section_height = height/max_range
run_once = False

print('cone will be split into ', max_range, ' estimated cylinders')

#array format:
#radius, current_height, area, volume, cumulative_volume
section_array = []

def area_circle(r):
    area = math.pi*(r*r)
    print('area is: ', area)
    return area

def volume_cylinder(height, area):
    volume = area*height
    print('volume of cylinder with height:', height, 'm and area: ', area, 'm^2')
    print(':', volume, 'm^3')
    return volume

def radius_cone_section(distance_from_base):
    radius = (-0.2 * distance_from_base) + 1
    radius = round(radius, 3)
    return radius

position_up_cone = 0

for i in range:
    position_up_cone = round(position_up_cone, 2)
    section_data = []
    #calculate the radius at each position up cone
    radius = radius_cone_section(position_up_cone)
    section_data.append(radius)
    print('at ', position_up_cone, 'm up cone, the radius is: ', radius)
    section_data.append(position_up_cone)
    position_up_cone += cylinder_section_height


    #area calculation
    area = area_circle(radius)
    section_data.append(round(area, 5))

    #volume calculation
    volume = volume_cylinder(round(cylinder_section_height, 2), area)
    section_data.append(round(volume, 5))

    #calculate cumulative volume
    if run_once:
        section_data.append(volume + section_array[-1][4])
    else:
        section_data.append(volume)
        run_once = True

    section_array.append(section_data)

    print()

print(section_array)

for i in section_array:
    print(i)
