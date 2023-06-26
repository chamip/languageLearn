import json
from country_codes import get_country_code
import pygal
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS

filename = 'population.json'
with open(filename) as f:
    pop_data = json.load(f)

cc_population = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == 2010:
        country_name = pop_dict['Country Name']
        population = int(pop_dict['Value'])
        code = get_country_code(country_name)
        if code:
            cc_population[code] = population
        # if code:
        #     print(code + ": " + str(population))
        # else:
        #     print("Error - " + country_name)
        # print(country_name + ": " + str(population))

cc_pop1, cc_pop2, cc_pop3 = {}, {}, {}
for cc, pop in cc_population.items():
    if pop < 1e7:
        cc_pop1[cc] = pop
    elif pop < 1e9:
        cc_pop2[cc] = pop
    else:
        cc_pop3[cc] = pop

wm_style = RS('#336633', base_style=LCS)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World Population in 2010, by Country'

# wm.add('2010', cc_population)
wm.add('0-10m', cc_pop1)
wm.add('10m-1bn', cc_pop2)
wm.add('>1bn', cc_pop3)
wm.render_to_file('world_population.svg')
