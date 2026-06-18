def normalize_ticker(text):

    return (
        text.upper()
        .strip()
        .replace(".SA", "")
        .replace(" ", "")
        .replace("-", "")
    )
