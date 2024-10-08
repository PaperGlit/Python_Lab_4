def write(data, filename):
    with open("Uploads/" + filename, 'w') as f:
        f.write(data)