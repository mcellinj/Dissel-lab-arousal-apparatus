This repository is a collection of code used to determine arousal threshold for Drosophila melanogaster. The preprint for this can be found at https://www.biorxiv.org/content/10.1101/2024.04.10.588925v1

buzzpulse.py is the main code with the rest subprocesses to control clock and camera setting.

The included code controls the stimulus for arousal and the recording of fly behavior. Arousal stimulus was provided by three coreless vibration motors (7x25mm) capable of 8,000-16,000rmp vibration. Vibration pattern and intensity were controlled by a DRV2605 haptic controller (Adafruit) paired with a Raspberry Pi 3 Model B+. The fly behavor was recorded using a Raspberry Pi NoIR camera.  
