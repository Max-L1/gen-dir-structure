#! /usr/bin/python3
import os
import random
import argparse
import sys
import shutil

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generates a dummy directory structure with random files up to a certain depth"
    )

    # Add command-line arguments
    parser.add_argument(
        "-p", "--path", type=str, help="Path to create the structure", required=True
    )
    parser.add_argument(
        "-d",
        "--max-depth",
        type=int,
        help="Maximum depth to create directories up to",
        required=True,
    )
    parser.add_argument(
        "-w",
        "--max-width",
        type=int,
        help="Maximum depth to create directories within a root directory",
        required=True,
    )
    parser.add_argument(
        "-f",
        "--max-files",
        type=int,
        help="Maximum amount of files to create in each directory",
        required=True,
    )

    parser.add_argument(
        "--delete", action="store_true", help="Delete directory if it already exists"
    )

    args = parser.parse_args()
    base_path = args.path
    max_depth = args.max_depth
    max_width = args.max_width
    max_files = args.max_files
    delete = args.delete

    if max_depth > 15 or max_width > 15:
        print("Nesting deeper than 15 not supported")
        sys.exit(1)

    def generate_directory_structure(base_path, max_depth, max_width, max_files):
        FILE_EXTENSIONS = [
            ".md",
            ".ini",
            ".yaml",
            ".xls",
            ".7z",
            ".java",
            ".r",
            ".conf",
            ".ttf",
            ".css",
            ".apk",
            ".sql",
            ".doc",
            ".xlsx",
            ".rpm",
            ".zip",
            ".mp4",
            ".html",
            ".iso",
            ".dll",
            ".psd",
            ".svg",
            ".deb",
            ".epub",
            ".ppt",
            ".wmv",
            ".c",
            ".odt",
            ".avi",
            ".mov",
            ".ods",
            ".js",
            ".odp",
            ".ai",
            ".php",
            ".ico",
            ".yml",
            ".csv",
            ".cfg",
            ".pptx",
            ".png",
            ".cpp",
            ".docx",
            ".h",
            ".exe",
            ".json",
            ".gif",
            ".tar",
            ".tsv",
            ".gz",
            ".mp3",
            ".py",
            ".bak",
            ".woff",
            ".rar",
            ".bmp",
            ".hpp",
            ".jpg",
            ".sh",
            ".mkv",
            ".log",
            ".bat",
            ".pdf",
            ".wav",
            ".txt",
            ".xml",
            ".jpeg",
            ".jar",
        ]

        if max_depth <= 0:
            return

        # Generate a random width for the current level
        width = random.randint(1, max_width)

        for i in range(width):
            subdirectory = os.path.join(base_path, f"dir_{i}")
            os.makedirs(subdirectory)

            # Generate a random number of files for the current directory
            num_files = random.randint(0, max_files)
            for j in range(num_files):
                file_path = os.path.join(
                    subdirectory, f"file_{j}{random.sample(FILE_EXTENSIONS, 1)[0]}"
                )
                with open(file_path, "w") as file:
                    file.write("AAAAA")

            generate_directory_structure(
                subdirectory, max_depth - 1, max_width, max_files
            )

    if os.path.exists(os.path.join(base_path, "dummy_structure")):
        if delete:
            shutil.rmtree(os.path.join(base_path, "dummy_structure"))
        else:
            print("Directory already exists, please delete before rerunning")
            sys.exit(2)
    os.mkdir("dummy_structure")
    generate_directory_structure(
        os.path.join(base_path, "dummy_structure"), max_depth, max_width, max_files
    )
