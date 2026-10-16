**## Day 2 best_route(14/10/2026) ##**

**Problem** - Find the route with the highest average value without using `max()`.

**My plan** - Go through each route and calculate its average by adding all the numbers and dividing by how many numbers there are. Remember the route with the highest average so far and replace it whenever I find a route with a higher average.

**Tests**

`print(best_route({}))`

`print(best_route(routes))`

`print(best_route({"a": [100], "b": [100]}))`

`print(best_route({"a": [10, 20], "b": [30]}))`

**What tripped me**

Using `None` to initialise `best_average` and `best_name`. I learnt that `None` means there is no value yet. This helps me handle the first route because I don't have an average to compare against yet.

Understanding `if best_average is None or current_average > best_average:`. The first part handles the first valid route, while the second part checks whether the current route has a higher average than the best one I have remembered.

Understanding `if not average: continue`. This skips routes with empty lists because I cannot calculate an average when there are no numbers to divide by.

**What I learnt**

I can find the route with the highest average without using `max()`. First, I initialise `best_average` and `best_name` with `None`. Then I use a `for` loop with `.items()` to access each route name and its list of values. I calculate the average using `sum(average) / len(average)`, compare it with the best average so far, and update both the average and route name whenever I find a better one.

I also learnt that when two routes have the same average, my function keeps the first route it encounters because I used `>` instead of `>=`. If all routes are empty, or the dictionary itself is empty, the function returns `None`.