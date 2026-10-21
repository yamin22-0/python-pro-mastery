def count_items(items):

    count = {}

    for item in items:
        count[item] = count.get(item, 0) + 1
    return count

counted_items = ["a","b","c","a","b","a","a"]
print(count_items(counted_items))
print(count_items([]))
print(count_items(["x","y"]))
print(count_items(["x","y","y"]))

def most_common(items):
    counts = count_items(items)

    most_appearing_item = None
    most_counted = 0

    for item, count in counts.items():
        if count > most_counted:
            most_counted = count
            most_appearing_item = item

    return most_appearing_item   

counted_items = ["a","b","c","a","b","a","a"]

print(most_common(counted_items))
print(most_common([]))
print(most_common(["x","y"]))
print(most_common(["x","y","y"]))
