# goit-pythonweb-hw-04

# Asynchronous File Sorter

This script asynchronously sorts files from a source folder into subfolders within a target directory based on their extensions.

## Features

- Asynchronous file processing for improved performance
- Automatic subfolder creation for each file type
- Recursive file search in source folder and subfolders
- Detailed process logging
- Uses only Python standard library

## Requirements

- Python 3.7+
- No additional dependencies required

## Installation

```bash
git clone https://github.com/sandrey88/goit-pythonweb-hw-04.git
cd <repository-name>
```

## Usage

```bash
python3 file_sorter.py <source_folder> <destination_folder>
```

Example:

```bash
python3 file_sorter.py ~/Downloads ~/Sorted_Files
```

### Arguments

- `source_folder`: Path to the folder containing files to be sorted
- `destination_folder`: Path to the folder where sorted files will be placed

## How It Works

1. The script scans the source folder and all its subfolders
2. For each file found:
   - Determines the file extension
   - Creates corresponding subfolder in the target directory (if it doesn't exist)
   - Copies the file to the appropriate subfolder
3. All operations are performed asynchronously for optimal performance

## Logging

The script creates detailed logs that include:

- Start of the sorting process
- Copying of each file
- Any errors that occur during the process
- Process completion with summary