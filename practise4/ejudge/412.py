import json
import sys

def diff(a, b, path=""):
    differences = []

    keys = set(a.keys()) | set(b.keys())
    for key in sorted(keys):
        a_val = a.get(key, "<missing>")
        b_val = b.get(key, "<missing>")
        current_path = f"{path}.{key}" if path else key

        if isinstance(a_val, dict) and isinstance(b_val, dict):
            differences.extend(diff(a_val, b_val, current_path))
        elif a_val != b_val:
            def serialize(val):
                if val == "<missing>":
                    return "<missing>"
                return json.dumps(val, separators=(',',':'))

            differences.append(f"{current_path} : {serialize(a_val)} -> {serialize(b_val)}")

    return differences

a = json.loads(sys.stdin.readline())
b = json.loads(sys.stdin.readline())

result = diff(a, b)
if result:
    print("\n".join(result))
else:
    print("No differences")