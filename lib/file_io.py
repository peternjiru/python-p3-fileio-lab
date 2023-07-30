def write_file(file_name='test_file', file_content="This is a test content."):
    log_file = open(f'{file_name}.txt', mode='w', encoding='utf-8')
    log_file.write(file_content)

def append_file(file_name="test_file", append_content="\nAppended content."):
    log_file = open(f'{file_name}.txt', mode='a', encoding='utf-8')
    log_file.write(append_content)

def read_file(file_name="test_file"):
    # write_file(file_name)
    log_file = open(f'{file_name}.txt', mode='r', encoding='utf-8')
    return log_file.read()
