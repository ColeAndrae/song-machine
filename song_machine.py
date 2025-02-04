#!/usr/bin/env python3
import numpy as np
from scipy.io import wavfile
import random
from pydub import AudioSegment
import os
import click
from rich.console import Console
from rich.progress import Progress

class FriendlySongMachine:
    def __init__(self):
        self.sample_rate = 44100
        self.console = Console()
        
        # Define musical scales
        self.scales = {
            'major': [0, 2, 4, 5, 7, 9, 11],
            'minor': [0, 2, 3, 5, 7, 8, 10],
            'pentatonic': [0, 2, 4, 7, 9]
        }

    def generate_note(self, frequency, duration):
        """Generate a single note"""
        t = np.linspace(0, duration, int(self.sample_rate * duration))
        wave = np.sin(2 * np.pi * frequency * t)
        
        # Apply simple envelope
        attack = int(0.1 * len(wave))
        release = int(0.2 * len(wave))
        
        envelope = np.ones(len(wave))
        envelope[:attack] = np.linspace(0, 1, attack)
        envelope[-release:] = np.linspace(1, 0, release)
        
        return wave * envelope

    def generate_song(self, style='relaxing', duration=180, output_file=None):
        """Generate a song with the specified style"""
        if output_file is None:
            output_file = f"friendly_song_{style}_{random.randint(1000,9999)}.mp3"
            
        self.console.print(f"\n[bold green]🎵 Creating a {style} song...[/bold green]")
        
        # Style presets
        styles = {
            'relaxing': {'base_freq': 220, 'tempo': 70},
            'upbeat': {'base_freq': 440, 'tempo': 120},
            'ambient': {'base_freq': 110, 'tempo': 60}
        }
        
        style_settings = styles.get(style, styles['relaxing'])
        
        # Initialize the song array
        total_samples = int(duration * self.sample_rate)
        song = np.zeros(total_samples)
        
        # Generate layers
        num_layers = 3
        for layer in range(num_layers):
            self.console.print(f"[cyan]Creating layer {layer+1}...[/cyan]")
            
            # Generate a sequence of notes
            current_time = 0
            layer_samples = np.zeros(total_samples)
            
            while current_time < duration:
                # Generate a note
                note_duration = random.uniform(0.2, 1.0)
                if current_time + note_duration > duration:
                    note_duration = duration - current_time
                
                frequency = style_settings['base_freq'] * random.choice([0.5, 0.75, 1.0, 1.25, 1.5])
                note = self.generate_note(frequency, note_duration)
                
                # Add note to layer
                start_idx = int(current_time * self.sample_rate)
                end_idx = start_idx + len(note)
                if end_idx > total_samples:
                    note = note[:total_samples-start_idx]
                    end_idx = total_samples
                
                layer_samples[start_idx:end_idx] += note
                current_time += note_duration
            
            # Add layer to song
            song += layer_samples * 0.3  # Reduce volume of each layer
        
        # Normalize the song
        song = song / np.max(np.abs(song))
        
        # Convert to 16-bit integer
        song_int = np.int16(song * 32767)
        
        # Save as WAV first
        temp_wav = "temp_song.wav"
        wavfile.write(temp_wav, self.sample_rate, song_int)
        
        # Convert to MP3
        AudioSegment.from_wav(temp_wav).export(output_file, format="mp3")
        
        # Clean up
        try:
            os.remove(temp_wav)
        except:
            pass
        
        self.console.print(f"\n[bold green]✨ Song created successfully: {output_file}[/bold green]")
        return output_file

@click.command()
@click.option('--style', type=click.Choice(['relaxing', 'upbeat', 'ambient']), 
              default='relaxing', help='Style of the song')
@click.option('--duration', default=180, help='Duration in seconds')
@click.option('--output', help='Output file name (optional)')
def main(style, duration, output):
    """Generate a unique musical piece with SongMachine! 🎵"""
    machine = FriendlySongMachine()
    machine.generate_song(style=style, duration=duration, output_file=output)

if __name__ == "__main__":
    main()
