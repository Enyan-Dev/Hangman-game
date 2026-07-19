# Responsive Hangman Game

A modern, desktop Hangman game built in Python using the Tkinter GUI framework. This project features a completely dynamic, percentage-based rendering layout, ensuring that both the on-screen keyboard interface and the visual hangman graphics scale fluidly when the application window is resized.

## Features

- **Dynamic Visuals:** The gallows and stick figure graphics are calculated using responsive screen percentages rather than fixed pixels.
- **Auto-Adapting Grid Keyboard:** Full A-Z virtual keyboard utilizing Tkinter's grid weighting system and `sticky="nsew"` configurations to scale smoothly across different resolutions.
- **Robust File I/O:** Safely reads secret word banks from an external `words.txt` file, automatically cleaning spaces and ignoring empty entries.
- **Smart Game State Tracking:** Tracks guessed characters dynamically, visually disabling used buttons while maintaining persistence even through layout updates.

## How It Works

The interface divides screen layouts across structural frames, using configuration events (`<Configure>`) to intercept real-time window adjustments:
- The base, post, and rope elements calculate absolute thickness dynamically via integer scaling (`width=max(2, int(w*0.015))`).
- The coordinate mappings ensure clean skeletal attachments for the stick figure's head, spine, limbs, and joints regardless of aspects ratios.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.

### Installation & Run Steps

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/enyan-dev/hangman-game.git
