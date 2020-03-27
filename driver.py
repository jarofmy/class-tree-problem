from solution import find_ordering

def main():
    dependencies = {
        "C1": [], 
        "C2": ["C1"],
        "C3": ["C2"],
        "LA": ["C2"],
        "DM": ["C2"],
        "DE": ["C3"],
        "AML": ["DE", "LA", "AA"],
        "P1": [],
        "P2": ["P1"],
        "AA": ["P2", "DM"]
        }

    result_1 = find_ordering(dependencies)

    print("Result 1: {}".format(result_1))


if __name__ == "__main__":
    main()