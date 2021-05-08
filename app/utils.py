def get_hashtags(text):
    import re
    return re.findall('#([A-Za-z0-9_]+)', text)
