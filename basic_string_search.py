Search = "fsdnagndfgnsdjkfgsndfJackfgdnfgnengs"
Target = "Jack"

def basicStringSearch(S, T):
    searchIndex = 0
    while searchIndex + len(T) <= len(S):
        targetIndex = 0
        while targetIndex < len(T) and T[targetIndex] == S[searchIndex + targetIndex]:
            targetIndex += 1
            if targetIndex == len(Target):
                return Target + ' found at iteration ' + str(searchIndex)
        if targetIndex == len(T):
            return searchIndex
        searchIndex += 1
    return - 1


print(basicStringSearch('per ardua ad alta', 'per'))
print(basicStringSearch('per ardua ad alta', 'lta'))
print(basicStringSearch('per ardua ad alta', 'ad'))
print(basicStringSearch('per ardua ad alta', 'astra'))
print(basicStringSearch(Search,Target))
