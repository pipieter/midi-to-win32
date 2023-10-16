# MIDI to Win32

Python script to map MIDI press/release events to Win32 inputs. Mappings can be defined in `main.py`. The script is run by using:

```
python main.py
```

# How to use

You can define your key mappings in `main.py` in the `MAPPINGS` dict. An example layout is already given. The current supported input events are `KeyboardPress`, `MousePress`, and `MouseMovement`. The mappings are defined as MIDI keynote to InputEvent.

The program can be quit at any time by pressing shift and tab simultaneously. 
# Issues

- There might be an input delay between pressing the keys in the MIDI device and the input being processed as a Win32 event.
- Mapping a key to a MousePress event could result in the mouse button being pressed repeatedly, very quickly. This is due to how the SendInput function of the Win32 API behaves. This didn't prove to be an issue with games, but did occur inside text editors and web browsers.
