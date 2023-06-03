# Generate Directory Structure

Generates a dummy directory structure with random files up to a certain depth

## Options

- `-h, --help`: Show this help message and exit
- `-p PATH, --path PATH`: Path to create the directory structure
- `-d MAX_DEPTH, --max-depth MAX_DEPTH`: Maximum depth to create directories up to
- `-w MAX_WIDTH, --max-width MAX_WIDTH`: Maximum depth to create directories within a root directory
- `-f MAX_FILES, --max-files MAX_FILES`: Maximum number of files to create in each directory
- `--delete`: Delete the directory if it already exists

## Example

`./generate-directory-structure.py --path . --max-depth 5 --max-width 5 --max-files 3 --delete`

Ensure permission set on script first:

`chmod u+x generate-directory-structure.py`

