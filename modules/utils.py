def replacingInvalid(string: str) -> str:
    string = string.replace('null', '"null"')
    string = string.replace('false', 'False')
    string = string.replace('true', 'True')
    return string
