
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         group = []
#         for i in range (len(strs)) : 
#             for j in range(1, len(strs)):
#                 if sorted(strs[i]) != sorted(strs[j]):
#                     break
#                 elif sorted(strs[i]) == sorted(strs[j]):
#                     group.append([i,j])
#         return group                                   


# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         group = []
#         visited = set()

#         for i in range(len(strs)):
#             if i in visited:
#                 continue

#             current = [strs[i]]

#             for j in range(i + 1, len(strs)):
#                 if sorted(strs[i]) == sorted(strs[j]):
#                     current.append(strs[j])
#                     visited.add(j)

#             group.append(current)

#         return group
#  time exceeded here so the right answer is this (cant be comparing when there are too many elements)


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in group:
                group[key] = []

            group[key].append(word)

        return list(group.values())
