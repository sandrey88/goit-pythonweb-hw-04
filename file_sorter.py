import asyncio
import logging
import shutil
from argparse import ArgumentParser
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def copy_file(source_file: Path, dest_folder: Path, executor: ThreadPoolExecutor):
    """
    Asynchronously copy a file to its corresponding extension folder.
    """
    try:
        # Get file extension (lowercase) or 'no_extension' if none exists
        extension = source_file.suffix.lower()[1:] or 'no_extension'
        
        # Create extension folder if it doesn't exist
        ext_folder = dest_folder / extension
        ext_folder.mkdir(exist_ok=True)
        
        # Generate destination path
        dest_path = ext_folder / source_file.name
        
        # Copy the file using ThreadPoolExecutor
        await asyncio.get_event_loop().run_in_executor(
            executor, shutil.copy2, source_file, dest_path
        )
        logger.info(f"Copied {source_file.name} to {ext_folder}")
        
    except Exception as e:
        logger.error(f"Error copying {source_file}: {str(e)}")

async def process_files(source_folder: Path, dest_folder: Path):
    """
    Process all files in the source folder and its subfolders asynchronously.
    """
    try:
        # Create a ThreadPoolExecutor for file operations
        with ThreadPoolExecutor() as executor:
            tasks = []
            
            # Recursively find all files
            for entry in source_folder.rglob('*'):
                if entry.is_file():
                    task = asyncio.create_task(
                        copy_file(entry, dest_folder, executor)
                    )
                    tasks.append(task)
            
            if tasks:
                await asyncio.gather(*tasks)
                logger.info(f"Processed {len(tasks)} files")
            else:
                logger.warning(f"No files found in {source_folder}")
                
    except Exception as e:
        logger.error(f"Error processing folder {source_folder}: {str(e)}")

async def main():
    # Parse command line arguments
    parser = ArgumentParser(description='Sort files by extension asynchronously')
    parser.add_argument('source', type=str, help='Source folder path')
    parser.add_argument('destination', type=str, help='Destination folder path')
    args = parser.parse_args()

    # Convert to Path objects
    source_path = Path(args.source)
    dest_path = Path(args.destination)

    # Validate source folder exists
    if not source_path.exists():
        logger.error(f"Source folder {args.source} does not exist")
        return

    # Create destination folder if it doesn't exist
    dest_path.mkdir(exist_ok=True)

    # Start processing
    logger.info(f"Starting to process files from {args.source}")
    await process_files(source_path, dest_path)
    logger.info("File processing completed")

if __name__ == "__main__":
    asyncio.run(main())
