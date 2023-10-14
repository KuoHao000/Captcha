with open('templates/verify.html', 'r') as file:
    url = 'index'

    # url = f"""
    #     <p>請點選下方的連結進行驗證 ：</p>
    #     <p><a href="{url}">認證</a></p>
    #     """

    file_data = ''

    content = file.readlines()

    for line in content:
        if '<p></p>' in line:
            line = line.replace('<p></p>', f"<p><a href=\"140.131.115.165:5000/{url}\">認證</a></p>")
        file_data += line
    print(file_data)
    # content = file.read()
    # file_data = ''
    # for line in content:
    #     if 'b' in line:
    #         line = line.replace('b', 'test')
    #     file_data += line


# import functools
#
#
# def auth(func):
#     @functools.wraps(func)
#     def inner(*args, **kwargs):
#         return func(*args, **kwargs)
#     return inner

# import functools
# from flask import Flask, redirect, session
#
# def auth(func):
#     @functools.wraps(func)
#     def inner(*args, **kwargs):
#         username = session.get('a')
#         if not username:
#             return redirect('/')
#         return func(*args,**kwargs)
#     return inner
