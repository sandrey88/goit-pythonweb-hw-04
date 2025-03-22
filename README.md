# goit-pythonweb-hw-04

# Asynchronous File Sorter

This script asynchronously sorts files from a source folder into subfolders within a target directory based on their extensions. It utilizes Python's built-in `asyncio` library for asynchronous operations.

## Features

- Asynchronous file processing using `asyncio.to_thread`
- Non-blocking I/O operations for improved performance
- Automatic subfolder creation for each file type
- Recursive file search in source folder and subfolders
- Detailed process logging
- Uses only Python standard library (asyncio, pathlib, shutil)

## Technical Implementation

- Uses `asyncio.to_thread` for non-blocking file operations
- Implements asynchronous file reading with `read_folder` function
- Parallel file copying using `asyncio.gather`
- Error handling and logging for all operations

## Requirements

- Python 3.7+ (tested on Python 3.12)
- No additional dependencies required

## Installation

```bash
git clone https://github.com/sandrey88/goit-pythonweb-hw-04.git
cd goit-pythonweb-hw-04
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

1. The script asynchronously scans the source folder and all its subfolders using `read_folder`:
   - Utilizes `pathlib.Path.rglob` for recursive file search
   - Makes I/O operations non-blocking with `asyncio.to_thread`

2. For each file found:
   - Determines the file extension
   - Creates corresponding subfolder in the target directory
   - Asynchronously copies the file using `shutil.copy2` wrapped in `asyncio.to_thread`

3. All copy operations are gathered and executed in parallel using `asyncio.gather`

## Logging

The script creates detailed logs that include:

- Start of the sorting process
- Individual file copy operations
- Any errors that occur during the process
- Process completion with summary of files processed