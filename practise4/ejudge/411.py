import json

def apply_patch(a,b):
    for key in b:
        if b[key] is None:
            a.pop(key,None)
        elif key in a and isinstance(a[key], dict) and isinstance(b[key], dict):
            apply_patch(a[key],b[key])
        else:
            a[key] = b[key]
    return a

a = json.loads(input())
b = json.loads(input())

result = apply_patch(a, b)
print(json.dumps(result, separators=(',', ':'), sort_keys=True))