def dirReduc(arr):
    my_dict ={"NORTH" : "SOUTH",
              "SOUTH" : "NORTH",
              "EAST" : "WEST",
              "WEST" : "EAST"}
    route = []
    for i in arr:

        if route and my_dict[i] == route[-1]:
            print(route)
            route.pop()
        else:
            route.append(i)
        
    return route
