# Packman
The multi platform data usage monitoring GUI no one decided to make until now 

![preview1](images/preview.png)
![tray](images/tray.png)

## Requirements
`pyqt5`

`psutil` 

You will need pyuic5 installed on your system for    `makegui.py` to work properly, otherwise it has to be done manually.

## Running
`make run` on systems with make installed

On Windows, run start.bat or type `py packman\packman.py`

### Installing dependencies with make
>make deps

### Installing dependencies manually
>python3 -m pip install -r requirements.txt

# How to use
The backlog level is a field that is subtracted from the GB and MB values
This was added in case the user wanted to keep track of how much data they used beyond a threshold or values that were larger and therefore harder to keep track of.

`makegui.py`: This creates python files in the gui directory of any ui file in the ui directory

Note that this app makes use of the psutil `net_io_counters` method to grab data based on the network interface 

## Milestone
- [x] Minimize to tray option
- [ ] Graph feature
- [ ] Ability to install
- [x] Data uploaded view
- [ ] Data usage limits/alarms
