# Video Metadata to JSON Converter

This Python script reads video metadata from separate text files (title, description, tags, and key-value pairs) and combines them into a JSON file.

## Description

The script processes four input text files:

*   `title.txt`: Contains the video title.
*   `description.txt`: Contains the video description.
*   `tags.txt`: Contains comma-separated video tags.
*   `metadata.txt`: Contains additional metadata as key-value pairs.

It then generates a `metadata.json` file containing all the information in a structured JSON format.  The script handles comments (lines starting with `#`) and empty lines in `metadata.txt`. It also handles quoted values, boolean values (true/false), and replaces newlines in `tags.txt` with commas.

## Installation

No specific installation is required as this is a single Python script. Ensure you have Python 3 installed. You can download Python from [https://www.python.org/](https://www.python.org/).

## Usage

1.  **Clone the repository (optional):** If this project is in a repository (e.g., GitHub), you can clone it:

    ```bash
    git clone https://github.com/dkghosh2019/video_preparation
    ```

2.  **Create input files:** Create the following text files in the `data/videoMetadata` directory (create the directory if it doesn't exist):

    *   `title.txt`:  The video title.
    *   `description.txt`: The video description.
    *   `tags.txt`: The video tags, separated by commas or newlines.
    *   `metadata.txt`: Additional metadata in the format `key=value`.  You can include comments using `#` at the beginning of the line.

3.  **Run the script:** Navigate to the project directory in your terminal and execute the Python script:

    ```bash
    python <path_to_script>/jsonBuilder.py
    ```
    Replace `<path_to_script>` with the actual path to your Python script file.  If the script is named `jsonBuilder.py` and is in the current directory, you can simply run:

    ```bash
    python create_metadata_json.py
    ```

4.  **Output:** The script will create a `metadata.json` file in the same directory as the input files. This file will contain the combined metadata in JSON format.

## Example Input Files

**title.txt:**
My Awesome Video Title

**description.txt:**
This is a description of my awesome video.  It's very informative and entertaining.

**tags.txt:**
video, tutorial, python, json, metadata
**metadata.txt:**
This is a comment
video_id = "12345"
published = true
category = "Education"
"author" = "John Doe" # Example with quotes


## Example Output (metadata.json)

```json
{
    "video_title": "My Awesome Video Title",
    "video_description": "This is a description of my awesome video.  It's very informative and entertaining.",
    "video_keywords": "video, tutorial, python, json, metadata",
    "video_id": "12345",
    "published": true,
    "category": "Education",
    "author": "John Doe"
}

Markdown

# Video Metadata to JSON Converter

This Python script reads video metadata from separate text files (title, description, tags, and key-value pairs) and combines them into a JSON file.

## Description

The script processes four input text files:

*   `title.txt`: Contains the video title.
*   `description.txt`: Contains the video description.
*   `tags.txt`: Contains comma-separated video tags.
*   `metadata.txt`: Contains additional metadata as key-value pairs.

It then generates a `metadata.json` file containing all the information in a structured JSON format.  The script handles comments (lines starting with `#`) and empty lines in `metadata.txt`. It also handles quoted values, boolean values (true/false), and replaces newlines in `tags.txt` with commas.

## Installation

No specific installation is required as this is a single Python script. Ensure you have Python 3 installed. You can download Python from [https://www.python.org/](https://www.python.org/).

## Usage

1.  **Clone the repository (optional):** If this project is in a repository (e.g., GitHub), you can clone it:

    ```bash
    git clone https://github.com/dkghosh2019/video_preparation
    ```

2.  **Create input files:** Create the following text files in the `data/videoMetadata` directory (create the directory if it doesn't exist):

    *   `title.txt`:  The video title.
    *   `description.txt`: The video description.
    *   `tags.txt`: The video tags, separated by commas or newlines.
    *   `metadata.txt`: Additional metadata in the format `key=value`.  You can include comments using `#` at the beginning of the line.

3.  **Run the script:** Navigate to the project directory in your terminal and execute the Python script:

    ```bash
    python <path_to_script>/create_metadata_json.py
    ```
    Replace `<path_to_script>` with the actual path to your Python script file.  If the script is named `create_metadata_json.py` and is in the current directory, you can simply run:

    ```bash
    python create_metadata_json.py
    ```

4.  **Output:** The script will create a `metadata.json` file in the same directory as the input files. This file will contain the combined metadata in JSON format.

## Example Input Files

**title.txt:**

My Awesome Video Title


**description.txt:**

This is a description of my awesome video.  It's very informative and entertaining.


**tags.txt:**

video, tutorial, python, json, metadata


**metadata.txt:**

This is a comment
video_id = "12345"
published = true
category = "Education"
"author" = "John Doe" # Example with quotes


## Example Output (metadata.json)

```json
{
    "video_title": "My Awesome Video Title",
    "video_description": "This is a description of my awesome video.  It's very informative and entertaining.",
    "video_keywords": "video, tutorial, python, json, metadata",
    "video_id": "12345",
    "published": true,
    "category": "Education",
    "author": "John Doe"
}
Error Handling
The script includes basic error handling for file not found and invalid lines in the metadata.txt file.  It will print informative messages to the console if any errors occur.

Contributing
Contributions are welcome!  Please feel free to submit pull requests or open issues.

License
The project is distributed under MIT  (e.g., MIT, GPL, etc.) license.




