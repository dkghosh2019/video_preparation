import os
import argparse
import re

def make_metadata_text(project_root, language):
    """
    Substitutes "en" with the given language code in metadata.txt.

    Args:
        project_root: The root directory of the project.
        language: The target language code (e.g., "fr").
    """

    input_file = os.path.join(project_root, "data", "metadata.txt")
    output_file = os.path.join(project_root, "data", "videoMetadata", "metadata.txt")
    output_dir = os.path.join(project_root, "data", "videoMetadata") # make sure output dir exists
    os.makedirs(output_dir, exist_ok=True)


    try:
        with open(input_file, "r", encoding="utf-8") as infile:
            metadata_content = infile.read()

        # Use regular expressions for more robust substitution
        new_metadata_content = re.sub(r'video_language = "en"', f'video_language = "{language}"', metadata_content)
        new_metadata_content = re.sub(r'title_language = "en"', f'title_language = "{language}"', new_metadata_content)

        with open(output_file, "w", encoding="utf-8") as outfile:
            outfile.write(new_metadata_content)

        print(f"Metadata updated for {language} and saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update metadata.txt with language code.")
    parser.add_argument("language", help="The target language code (e.g., 'fr', 'ja').")
    parser.add_argument("project_root", help="The root directory of the project.")

    args = parser.parse_args()
    make_metadata_text(args.project_root, args.language)