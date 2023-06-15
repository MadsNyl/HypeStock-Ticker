

def is_empty_file_line(line: list[str], start_index: int) -> bool:
    line = line[start_index:]
    return all(is_null(data) for data in line)


def is_null(data: str) -> bool:
    return data == "null"