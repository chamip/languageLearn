from pygal_maps_world.i18n import COUNTRIES


def get_country_code(country_name):
    """根据国家名获取国别码"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None

#
# for country_code in sorted(COUNTRIES.keys()):
#     print(country_code, COUNTRIES[country_code])
#
# print(get_country_code('Zimbabwe'))

