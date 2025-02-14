import json
import os

# Determine the directory of the current script
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))

TITLE_FILE = os.path.join(SCRIPT_DIR, "../../data/videoMetadata/title.txt")
DESCRIPTION_FILE = os.path.join(SCRIPT_DIR, "../../data/videoMetadata/description.txt")  
TAGS_FILE = os.path.join(SCRIPT_DIR, "../../data/videoMetadata/tags.txt")
METADATA_FILE = os.path.join(SCRIPT_DIR, "../../data/videoMetadata/metadata.txt")
OUTPUT_JSON_FILE = os.path.join(SCRIPT_DIR, "../../data/videoMetadata/metadata.json")



def create_metadata_json(title_file, description_file, tags_file, metadata_file, output_json_file):
    """Combines text files into a metadata.json file."""

    try:
        metadata = {}

        # Read title
        with open(title_file, 'r', encoding='utf-8') as f:
            metadata['video_title'] = f.read().strip()

        # Read description
        with open(description_file, 'r', encoding='utf-8') as f:
            metadata['video_description'] = f.read().strip()

        # Read tags (comma-separated)
        with open(tags_file, 'r', encoding='utf-8') as f:
            tags_str = f.read().strip()
            metadata['video_keywords'] = tags_str.replace('\n', ',') # Replace newlines with commas

        # Read metadata from metadata.txt (key-value pairs)
        with open(metadata_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):  # Skip empty lines and comments
                    try:
                        key, value = line.split("=", 1)
                        key = key.strip()
                        value = value.strip()

                        # Remove quotes if present
                        if value.startswith('"') and value.endswith('"'):
                            value = value[1:-1]

                        # Convert boolean strings to booleans
                        if value.lower() == "true":
                            value = True
                        elif value.lower() == "false":
                            value = False
                        
                        metadata[key] = value
                    except ValueError:
                        print(f"Warning: Invalid line in metadata.txt: {line}")

        # Write to JSON file
        with open(output_json_file, 'w', encoding='utf-8') as json_file:
            json.dump(metadata, json_file, indent=4, ensure_ascii=False)

        print(f"Metadata written to {output_json_file}")

    except FileNotFoundError as e:
        print(f"Error: File not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage:
if __name__ == "__main__":
    title_file = TITLE_FILE
    description_file = DESCRIPTION_FILE
    tags_file = TAGS_FILE
    metadata_file = METADATA_FILE
    output_json_file = OUTPUT_JSON_FILE

    create_metadata_json(title_file, description_file, tags_file, metadata_file, output_json_file)