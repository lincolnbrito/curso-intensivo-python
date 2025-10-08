
def print_models(unprinted_designs, completed_models):
    """Simulate printing of each design until there is no more design
    Transfers each design to completed_models after the printing"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # Simulates the creation of 3D printing from design
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all finished designs"""
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

