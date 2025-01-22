import os

name = os.environ.get("INPUT_NAME")
print(f"::set-output name=output_string:: Hello {name} We are looking forward to working with you")