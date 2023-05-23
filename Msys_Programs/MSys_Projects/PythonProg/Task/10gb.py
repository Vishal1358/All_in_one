with open('large_file.txt', 'w') as f:
    while True:
        chunk = f.read(1024*1024*1024*10) # 10gb
        if not chunk:
            break
        # process the chunk of data