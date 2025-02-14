import os
import json
import argparse  # For command-line arguments
from googletrans import Translator

def translate_files(project_root, language):
    """
    Translates text files to a single specified language.

    Args:
        project_root: The root directory of the project.
        language: The target language code (e.g., "fr").
    """

    data_dir = os.path.join(project_root, "data")
    #output_dir = os.path.join(project_root, "data", "videoMetadata", language) # output dir now includes the language
    output_dir = os.path.join(project_root, "data", "videoMetadata")
    os.makedirs(output_dir, exist_ok=True)

    files_to_translate = ["title.txt", "description.txt", "tags.txt"]
    ##metadata_file = "metadata.txt"

    translator = Translator()

    print(f"Translating to {language}...")

    for file_name in files_to_translate:
        input_file = os.path.join(data_dir, file_name)
        output_file = os.path.join(output_dir, file_name)

        try:
            with open(input_file, "r", encoding="utf-8") as infile:
                text = infile.read()

            translation = translator.translate(text, dest=language)
            translated_text = translation.text

            with open(output_file, "w", encoding="utf-8") as outfile:
                outfile.write(translated_text)
            print(f"Translated {file_name} to {language} and saved to {output_file}")

        except FileNotFoundError:
            print(f"Warning: {file_name} not found in {data_dir}")
        except Exception as e:
            print(f"Error translating {file_name} to {language}: {e}")
    

    # Handle metadata.txt as JSON
    """
    metadata_input_file = os.path.join(data_dir, metadata_file)
    metadata_output_file = os.path.join(output_dir, "metadata.json")

    try:
        with open(metadata_input_file, "r", encoding="utf-8") as infile:
            metadata_text = infile.read()

        try:
            metadata = json.loads(metadata_text)
        except json.JSONDecodeError:
            metadata = {"text": metadata_text}

        translated_metadata = {}
        for key, value in metadata.items():
            try:
                translation = translator.translate(value, dest=language)
                translated_metadata[key] = translation.text
            except Exception as e:
                print(f"Error translating metadata field '{key}': {e}")
                translated_metadata[key] = value

        with open(metadata_output_file, "w", encoding="utf-8") as outfile:
            json.dump(translated_metadata, outfile, indent=4, ensure_ascii=False)
        print(f"Translated {metadata_file} to {language} and saved to {metadata_output_file}")
    

    except FileNotFoundError:
        print(f"Warning: {metadata_file} not found in {data_dir}")
    except Exception as e:
        print(f"Error processing {metadata_file} to {language}: {e}")
    """

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Translate files to a specified language.")
    parser.add_argument("language", help="The target language code (e.g., 'fr', 'ja').")
    parser.add_argument("project_root", help="The root directory of the project.") # added project root to command line

    args = parser.parse_args()

    translate_files(args.project_root, args.language)

    print("Translation complete.")  # Added a final message