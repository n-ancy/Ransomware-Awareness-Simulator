# Ransomware-Awareness-Simulator

A Python-based desktop simulator designed to visually demonstrate the impact of disruptive cyber incidents in a safe and controlled environment.

## Features

- Full-screen immersive interface
- Custom background support
- Simulated file activity logs
- Dynamic progress bar
- Countdown timer
- Focus monitoring
- Automatic exit
- Standalone EXE packaging

## Technologies Used

- Python 3
- Tkinter
- Pillow
- PyInstaller

## Installation

### Clone Repository

```bash
git clone https://github.com/n-ancy/Ransomware-Awareness-Simulator.git
cd Ransomware-Awareness-Simulator
```

### Install Dependencies

```bash
pip install pillow
```

## Running the Application

```bash
python main.py
```

## Building an EXE

```bash
py -m PyInstaller --onefile --noconsole --add-data "background.png;." main.py
```

The executable will be generated inside:

```
dist/
```

## Safety Notice

This application is intended solely for educational demonstrations and awareness activities.

It does not:

- Encrypt files
- Modify user data
- Change system settings
- Disable security features
- Establish persistence
- Perform network communication

## Project Structure

```
Ransomware-Awareness-Simulator/
├── main.py
├── background.png
├── requirements.txt
├── README.md
└── dist/
```

## License

MIT License
