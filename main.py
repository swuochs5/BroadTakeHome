import requests
import json

headers = {'x-api-key': 'c4b4bc81607a4693932e736441f6b0d2'}
usableRoutes = ('0', '1')


# Return all routes using the MBTA `/routes` endpoint
# Optionally accepts an arbitrary number of route types to filter on, corresponding inputs given below:
# '0'	Light Rail
# '1'	Heavy Rail
# '2'	Commuter Rail
# '3'	Bus
# '4'	Ferry
# Ex: Passing types ('0', '1') returns all routes of type "light rail" and "heavy rail"
def getRoutes(types=usableRoutes):
    queryParams = {}
    if types:
        typesConcat = ','.join(types)
        queryParams['filter[type]'] = typesConcat
    stopsPayload = requests.get(f'https://api-v3.mbta.com/routes', params=queryParams, headers=headers)
    return json.loads(stopsPayload.text).get('data')


# Return all stops for a route with the given ID
def getRouteStops(routeId):
    routeStopsPayload = requests.get(f'https://api-v3.mbta.com/stops?filter[route]={routeId}', headers=headers)
    return json.loads(routeStopsPayload.text).get('data')


def getCompletedPath(origin, destination, stops, routes):
    if origin == destination:
        return [origin]
    routeToDestination = stops.get(destination)
    stopToRoute = routes.get(routeToDestination)
    return getCompletedPath(origin, stopToRoute, stops, routes) + [routeToDestination, destination]

def findPathBetween(origin, destination, stopIntersections):
    stopQueue = [origin]
    allReachableStops = {origin: None}  # Map of Stop -> Route taken to reach it
    allReachableRoutes = {}  # Map of Route -> Stop taken to reach it
    pathToDestination = None
    while pathToDestination is None:
        # If there is no path to the destination, the queue of intersection stops will run out
        # without ever finding a valid path
        if len(stopQueue) == 0:
            print('Destination not reachable from given origin')
            return
        currentStop = stopQueue.pop(0)
        # Get routes that are reachable from the current stop, any new routes should be explored
        # to see if they can reach the destination or other intersection stops
        currentlyReachableRoutes = stopIntersections.get(currentStop)
        # If there are ever no reachable routes, the given origin does not lie on any route
        if currentlyReachableRoutes is None:
            print('Destination not reachable from given origin')
            return
        for route in currentlyReachableRoutes:
            # Guarantees that we find the shortest number of line changes required to reach each line
            if route not in allReachableRoutes:
                allReachableRoutes[route] = currentStop
            stopsOnRoute = list(map(lambda r: r.get('id'), getRouteStops(route)))
            # If destination is reachable from current route, we can construct the complete path from
            # origin -> destination
            if destination in stopsOnRoute:
                allReachableStops[destination] = route
                pathToDestination = getCompletedPath(origin, destination, allReachableStops, allReachableRoutes)
            # To continue searching, we consider only stops that are intersections and have not already been reached
            newIntersections = list(
                filter((lambda s: len(stopIntersections.get(s)) >= 2 and s not in allReachableStops), stopsOnRoute))
            for stop in newIntersections:
                allReachableStops[stop] = route
            stopQueue.extend(newIntersections)
    return pathToDestination

def main():
    # Problem 1
    routes = getRoutes()
    routeNamesLong = list(map(lambda r: r.get('attributes').get('long_name'), routes))
    print(f'Here are the long names of all subway routes: {", ".join(routeNamesLong)}')

    # Problem 2
    # (Route Name, Number of Stops)
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

        # Find and count each route that a stop intersects
        for s in routeStops:
            stopId = s.get('id')
            if stopId not in stopIntersections:
                stopIntersections[stopId] = [routeId]
            else:
                stopIntersections[stopId].append(routeId)
    print(f'The route with the most stops is the {maxStops[0]} with {maxStops[1]} stops.')
    print(f'The route with the least stops is the {minStops[0]} with {minStops[1]} stops.')
    for stop, intersections in stopIntersections.items():
        if len(intersections) >= 2:
            print(f'The {stop} stop is an intersection of the following routes: {", ".join(intersections)}')

    # Problem 3
    print(stopIntersections)
    origin = input('Please enter your origin stop ID: ')
    destination = input('Please enter your destination stop ID: ')
    pathToDestination = findPathBetween(origin, destination, stopIntersections)
    print(' -> '.join(pathToDestination))


if __name__ == '__main__':
    main()
