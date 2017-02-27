# Error： #
> SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 45-46: truncated \uXXXX escape


# Codes： #
    # compile by python 3.5.1
    path='F:\PythonProjects\usagov_bitly_data2012-03-16-1331923249.txt'
    print(open(path).readline())

# Solution： #

 Python will try to interpret \usagov... as a Unicode escape sequence (like \uBEEF) which fails for obvious reasons.

You need to use a raw string

    path=r'F:\PythonProjects\usagov_bitly_data2012-03-16-1331923249.txt'
or escape the backslashes
    
    path='F:\PythonProjects\\usagov_bitly_data2012-03-16-1331923249.txt'
or use forward slashes

    path='F:\PythonProjects/usagov_bitly_data2012-03-16-1331923249.txt'
