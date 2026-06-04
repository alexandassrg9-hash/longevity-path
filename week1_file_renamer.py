from pathlib import Path              #imports the Path class from the pathlib module, which provides an object-oriented interface for working with file paths
folder = Path('rename_test')      #creates a Path object for the folder named 'rename_test'

for file in folder.iterdir(): 
    stem = file.stem
    suffix = file.suffix
    clean_stem = stem.lower().strip().replace('(', '').replace(')','').replace(' ', '_')
    clean_suffix = suffix.lower().strip().replace(' ', '')
    cleaned = clean_stem + clean_suffix
    messy = file.name
    print(f"{messy} -> {cleaned}") 