# Validate Params

def validate_params(func):

    def wrapper(*args, **kwargs):
        errors = []
        for k, v in kwargs.items():
            arg_type = func.__annotations__[k]
            if not isinstance(v, arg_type):
                errors.append(f"{k} is not {arg_type}")
        if errors:
            print(errors)
            return None
        return func(*args, **kwargs)

    return wrapper


@validate_params
def demo_func(x: int, y: dict, z:float):
    print(x, y, z)


demo_func(x=1.0, y={"name": "Rahul"}, z=2)
