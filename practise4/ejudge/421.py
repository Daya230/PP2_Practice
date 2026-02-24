n = int(input())
for _ in range(n):
    module_path, attr_name = input().split()
    try:
        mod = __import__(module_path)
        parts = module_path.split(".")
        for p in parts[1:]:
            mod = getattr(mod, p)
        if not hasattr(mod, attr_name):
            print("ATTRIBUTE_NOT_FOUND")
        else:
            if callable(getattr(mod, attr_name)):
                print("CALLABLE")
            else:
                print("VALUE")
    except ModuleNotFoundError:
        print("MODULE_NOT_FOUND")