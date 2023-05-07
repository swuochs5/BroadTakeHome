import requests
import json


# Return all routes using the MBTA `/routes` endpoint
# Optionally accepts an arbitrary number of route types to filter on, corresponding inputs given below:
# '0'	Light Rail
# '1'	Heavy Rail
# '2'	Commuter Rail
# '3'	Bus
# '4'	Ferry
# Ex: Passing types ('0', '1') returns all routes of type "light rail" and "heavy rail"
def getRoutes(*types):
    if not types:
        return requests.get('https://api-v3.mbta.com/routes')
    typesConcat = ','.join(types)
    routesPayload = requests.get(f'https://api-v3.mbta.com/routes?filter[type]={typesConcat}')
    return json.loads(routesPayload.text).get('data')

# Return all stops for a route with the given ID
def getRouteStops(routeId):
    stopsPayload = requests.get(f'https://api-v3.mbta.com/stops?filter%5Broute%5D={routeId}')
    return json.loads(stopsPayload.text).get('data')


def main():
    # Problem 1
    routes = getRoutes('0', '1')
    routeNamesLong: list = list(map(lambda r: r.get('attributes').get('long_name'), routes))
    print(f'Here are the long names of all subway routes: {", ".join(routeNamesLong)}')

    # Problem 2
    maxStops = (None, None)
    minStops = (None, None)
    stopIntersections = {}
    for r in routes:
        routeId = r.get('id')
        routeName = r.get('attributes').get('long_name')
        routeStops = getRouteStops(routeId)
        numStops = len(routeStops)

        # Find the route with the most and least number of stops
        if maxStops[1] is None or numStops > maxStops[1]:
            maxStops = (routeName, numStops)
        if minStops[1] is None or numStops < minStops[1]:
            minStops = (routeName, numStops)

        # Find and count the number of routes that each stop intersects
        for s in routeStops:
            stopName = s.get('attributes').get('name')
            if stopName not in stopIntersections:
                stopIntersections[stopName] = [routeName]
            else:
                stopIntersections[stopName].append(routeName)
    print(f'The route with the most stops is the {maxStops[0]} with {maxStops[1]} stops.')
    print(f'The route with the least stops is the {minStops[0]} with {minStops[1]} stops.')
    for stop, intersections in stopIntersections.items():
        if len(intersections) >= 2:
            print(f'The {stop} stop is an intersection of the following routes: {", ".join(intersections)}')

    # Problem 3
    origin = input(f'Please enter your origin stop ID: ')
    destination = input(f'Please enter your destination stop ID: ')



if __name__ == '__main__':
    main()
