# names = ["halima abdi" , "halima osman" , "amina ali"]

# find_name = input("Search name: ")
# clean_find = find_name.strip().lower()


# found = 0

# for name in names:
#     if clean_find in name:
#         print(f"Found: {name}")
#         found += 1

# if found == 0:
#     print("Not found.")


# def find_largest(numbers):

#     largest = numbers[0]

#     for number in numbers:
#         if number > largest:
#             largest = number
#     return largest

# print(find_largest(([8,0,4])))
# print(find_largest(([-5,-1,-8])))

numbers = [3,1,4,1,5]

def running_max(numbers):

    max_num_so_far = numbers[0]
    max_list = []

    for number in numbers:
        if number > max_num_so_far:
            max_num_so_far = number
            
        max_list.append(max_num_so_far)
    
    return max_list

print(running_max(numbers))
print(running_max([2,2,1]))


counts = {}
for word in ["a", "b", "a"]:
    counts[word] = counts.get(word, 0) + 1
print(counts)  


def get_player_score(games):

    scores = {}

    for name,score in games:

        scores[name] = scores.get(name,0) + score

    return scores

games_data = [("Binyamin",25),("Khalid",30),("Binyamin",60),("Khalid",20)]
print(get_player_score(games_data))
