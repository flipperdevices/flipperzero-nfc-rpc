

def mydec(fn):
    print(f"mydec fn: {fn.__name__}")
    def wrapper(*args, **kw):
        print(f"was called with {args=}, {kw=}")
        return fn(*args, **kw)

    return wrapper

@mydec
def myfunc(a, b):
    return a+b


def main():
    print("yo")
    print(myfunc(3,4))

if __name__ == "__main__":
    main()