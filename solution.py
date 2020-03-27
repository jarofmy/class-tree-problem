def find_ordering(dependencies):
    results = []

    while dependencies:
        for key in list(dependencies):
            if all(prereq in results for prereq in dependencies[key]):
                results.append(key)
                del dependencies[key]

    return results