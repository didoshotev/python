

obj = {'Dido': [51], 'Aikola': [50], 'Ivan': [3, 4, 5]}


ordered = dict(sorted(obj.items(), key=lambda x: (-sum(x[1]), x[0])))
print(ordered)

txt = "ThisIsMyString"
start = 1
end = 4

old_part = txt[start+1:end+1]

part = txt[end:start:-1]


txt = txt.replace(old_part, part)



