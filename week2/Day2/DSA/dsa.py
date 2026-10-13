
def best_route(routes):

    best_average = None
    best_name = None

    for name,average in routes.items():

        if not average:
            continue

        current_average = sum(average) / len(average)

        if best_average is None or current_average > best_average:
            best_average = current_average
            best_name = name

    return best_name
        
routes = {
    "thika" : [4000,5200,4800] ,
    "rongai" : [3500,3000], 
    "kitengela" : [5200]
    }  

print(best_route({}))  
print(best_route(routes))
print(best_route({"a": [100], "b": [100]}))
print(best_route({"a": [10, 20], "b": [30]}))