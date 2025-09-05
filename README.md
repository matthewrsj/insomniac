# Insomniac

Keep your computer awake by simulating mouse movement.

## Installation

```bash
git clone https://github.com/matthewrsj/insomniac.git
cd insomniac
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

```bash
python3 insomniac.py
```

Press `Ctrl+C` to stop.

## How it works

Insomniac moves your mouse cursor by a few pixels every 3-5 seconds, preventing your system from going to sleep or showing you as idle. The movements are small and random to avoid interfering with your work.

## Requirements

- Python 3.6+
- pyautogui

## License

MIT