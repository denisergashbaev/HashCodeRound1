def get_line(line):
    return map(lambda s: int(s), line.split(' '))

def get_line_first(line):
    return get_line(line)[0]
