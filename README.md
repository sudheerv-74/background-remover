# Background Remover Tool

A web-based tool to remove backgrounds from images using deep learning with Flask and PyTorch. This tool uses the DeepLabV3 model for background removal and integrates the Remove.bg API for enhanced quality.

## Features

- Removes background from images.
- Simple and easy-to-use web interface.
- Enhanced background removal using Remove.bg API.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/background-remover-tool.git
    cd background-remover-tool
    ```

2. **Set up a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Add your Remove.bg API Key:**

    Replace `'your-api-key-here'` in `app.py` with your actual Remove.bg API key.

## Usage

1. **Run the Flask app:**

    ```bash
    python app.py
    ```

2. **Open your browser and go to:**

    ```
    http://127.0.0.1:5000
    ```

3. **Upload an image** to remove its background. The processed image will be available for download.

## Technology Stack

- **Frontend:** HTML, CSS (with Glassmorphism)
- **Backend:** Flask, Python
- **Model:** PyTorch DeepLabV3
- **API:** Remove.bg API

## File Structure

- `app.py`: Main application file.
- `templates/index.html`: HTML file for the frontend.
- `static/styles.css`: CSS for styling.
- `requirements.txt`: List of Python dependencies.

## Contributing

Feel free to fork this repository and contribute by submitting a pull request. Any contributions, issues, and feature requests are welcome!

