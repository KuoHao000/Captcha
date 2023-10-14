# def test(a, *args):
#     print(a, type(args))
#
#     for arg in args:
#         print(arg)
#
#
# test(5, 22, 10, 10)

def test(a, *args, **kwargs):
    print(a, type(args), type(kwargs))

    for arg in args:
        print(arg)


test(5, 22, 10, 10, b=1, c=20)
