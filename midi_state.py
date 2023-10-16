# Utility class to keep track of a MIDI device's state
# Mutexes are required to allow processing of many events at once, otherwise some events
# might get lost.

from threading import Lock

import rtmidi


class MIDIState:
    mutex = Lock()
    pressedKeys: set[int] = set()
    midiin = rtmidi.RtMidiIn()

    def __init__(self, midiPort: int) -> None:
        self.midiin.openPort(midiPort)
        self.midiin.setCallback(self.ProcessEvent)
        print(f"Connected to port {midiPort}.")

    def ProcessEvent(self, midi) -> None:
        with self.mutex:
            note = midi.getNoteNumber()
            if midi.isNoteOn():
                self.pressedKeys.add(note)
            else:
                self.pressedKeys.remove(note)

    def GetKeyState(self, key: int) -> bool:
        with self.mutex:
            return key in self.pressedKeys
