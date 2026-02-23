import json

def resolve(data, query):
    current = data

    for part in query.split('.'):
        
        while '[' in part:
            key, rest = part.split('[', 1)
            if key:  
                if not isinstance(current, dict) or key not in current:
                    return "NOT_FOUND"
                current = current[key]
            idx, part = rest.split(']', 1)
            idx = int(idx)
            if not isinstance(current, list) or idx >= len(current):
                return "NOT_FOUND"
            current = current[idx]
        if part:  
            if not isinstance(current, dict) or part not in current:
                return "NOT_FOUND"
            current = current[part]
    return json.dumps(current, separators=(',', ':'))

data = json.loads(input())
q = int(input())
for _ in range(q):
    query = input().strip()
    print(resolve(data, query))