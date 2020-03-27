def find_ordering(dependencies):
    results = []
    # Set initial courses
    for key in list(dependencies):
        if not dependencies[key]:
            results.append(key)
            del dependencies[key]
    
    while dependencies:
        for key in list(dependencies):
            if all(prereq in results for prereq in dependencies[key]):
                results.append(key)
                del dependencies[key]
                
    return results

if __name__ == "__main__":
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

    result = find_ordering(dependencies)
    print(result)