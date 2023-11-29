# File Arranger

## Overview

The File Arranger is a Python script that arranges files based on their file extensions in a specified directory. It creates folders for each unique file extension and moves the corresponding files into their respective folders.

## Features

- **Arranging Files:** Files are grouped into folders based on their file extensions.
- **Folder Creation:** Unique folders are created for each file extension.

## Usage

1. Run the script:

    
    python file_arranger.py
 

2. Provide the path of the directory you want to arrange.

## Example

Suppose you have files in a directory like this:

file1.txt
file2.txt
document.docx
image.jpg
script.py
arduino
Copy code

After running the script, the directory will be organized as follows:

txt
file1.txt
file2.txt
docx
document.docx
jpg
image.jpg
py
script.py
