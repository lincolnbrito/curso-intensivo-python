from printing_functions import print_models, show_completed_models


unprinted_designs = ["iphone case", "robot pendant", "dodecahedron"]
completed_models = []

# avoid modify list passing a slice list
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

print("\n-----Original Unprinted Models: ")
print(unprinted_designs)