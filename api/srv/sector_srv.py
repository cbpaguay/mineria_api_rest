from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="news_app_locations")

sectores = ['neighbourhood','suburb','hamlet','village','country']

def find_sector(coordenadas):
    sector  = "No encontrado"
    try:
        location = geolocator.reverse(coordenadas)
        location = location.raw['address']
        for s in sectores:
            if s in location:
                sector = location[s] + ", " + location['county']
                break
    except Exception as e:
        print(e)
    finally:
        return sector