import time

import keyboard

import input as Input
import midi_state as MIDI

TIMEOUT = 0.001

MAPPINGS: dict[int, Input.InputEvent] = {
    # Movement
    47: Input.KeyboardPress(Input.A),
    48: Input.KeyboardPress(Input.S),
    52: Input.KeyboardPress(Input.W),
    53: Input.KeyboardPress(Input.D),
    # Other keys
    49: Input.KeyboardPress(Input.SPACE),
    51: Input.KeyboardPress(Input.E),
    46: Input.KeyboardPress(Input.LEFT_SHIFT),
    73: Input.MousePress("left"),
    75: Input.MousePress("right"),
    # Mouse control
    71: Input.MouseMovement(-50, 0),
    72: Input.MouseMovement(0, 50),
    76: Input.MouseMovement(0, -50),
    77: Input.MouseMovement(50, 0),
}

if __name__ == "__main__":
    print("Starting program.")

    midi = MIDI.MIDIState(0)
    while True:
        if keyboard.is_pressed("shift+tab"):
            break
        for key, input in MAPPINGS.items():
            print(midi.GetKeyState(key))
            if midi.GetKeyState(key):
                input.hold()
            else:
                input.release()
        time.sleep(TIMEOUT)

    print("Ending program.")
