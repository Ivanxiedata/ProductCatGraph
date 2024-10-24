from exploreGraph import exploreGraph
from RevenuePath import revenuePath
def main():
    start_category = "Electronics"
    budget = 45

    print(f'The whole path will be {exploreGraph(start_category)}')
    print(f'The paths which are less the budget {budget} are {revenuePath(start_category, budget)}')

if __name__ == "__main__":
    main()


