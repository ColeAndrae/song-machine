# Song Machine

A Python-based random music generator that creates unique musical pieces in different styles, including a completely chaotic mode!

## Features

- Multiple song styles:
  - Relaxing: Gentle, soothing melodies
  - Upbeat: Higher energy, faster tempo
  - Ambient: Spacious, atmospheric sounds
  - Chaos: Completely random, experimental sounds
- Customizable duration
- Musical note generation based on scales
- Multiple layered composition
- MP3 output format

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ColeAndrae/song-machine.git
cd song-machine
```

2. Create a virtual environment and activate it:
```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install numpy scipy pydub click rich
```

4. Install ffmpeg:
- On macOS: `brew install ffmpeg`
- On Ubuntu/Debian: `sudo apt-get install ffmpeg`
- On Windows: Download from [ffmpeg website](https://www.ffmpeg.org/download.html)

## Usage

Generate a song:
```bash
python3 song_machine.py
```

Options:
- `--style`: Choose between 'relaxing', 'upbeat', 'ambient', or 'chaos' (default: relaxing)
- `--duration`: Set the length of the song in seconds (default: 180)
- `--output`: Specify the output filename (optional)

Examples:
```bash
# Generate a 2-minute upbeat song
python3 song_machine.py --style upbeat --duration 120

# Generate an ambient song with custom filename
python3 song_machine.py --style ambient --output my_ambient_song.mp3

# Generate a chaotic experimental piece
python3 song_machine.py --style chaos
```

## Chaos Mode

The chaos mode generates completely random experimental music with:
- Random frequencies and wave shapes
- Unpredictable modulation effects
- Variable number of layers
- Random volume changes
- Occasional reversed sections
- Surprise sound effects

Perfect for creating unique experimental soundscapes!

## License

MIT License - feel free to use and modify as you like!