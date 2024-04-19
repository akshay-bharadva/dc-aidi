# QueryGenius: Ask Me Anything Extension

QueryGenius is a Chrome extension that allows you to ask anything about the active page and get intelligent responses powered by AI.

## Directory Structure

- ai-server/
- app/


## Getting Started

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Ensure you have an Open API key and add it to the `.env` file in the root directory.

### Building the Chrome Extension

1. Navigate to the `app/` directory.
2. Run `npm install` to install dependencies.
3. Run `npm run build` to generate the `dist` folder containing the Chrome extension files.

### Loading the Chrome Extension

1. Open Google Chrome.
2. Navigate to `chrome://extensions/`.
3. Enable Developer mode.
4. Click on "Load unpacked" and select the `dist` folder generated earlier.

### Setting Up the AI Server

1. Navigate to the `ai-server/` directory.
2. Install required Python packages by running:
    ```
    pip install -r requirements.txt
    ```
3. Run the Flask server by executing:
    ```
    python main.py
    ```

## Usage

Once the Chrome extension is loaded and the AI server is running, simply activate the extension on any webpage and start asking questions!