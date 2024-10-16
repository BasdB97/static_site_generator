def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.lstrip().startswith("# "):
            return line.lstrip("# ").strip()
    raise ValueError("No h1 header found in the markdown")