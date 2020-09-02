# Packman
The multi platform data usage monitoring GUI no one decided to make until now 

![preview1](images/preview.png)
![tray](images/tray.png)

## Requirements
`pyqt5`

`psutil` 

You will need pyuic5 installed on your system for `makegui.py` to work properly in case you want to contribute to the 
development of Packman. You will need `pyqt5-dev-tools` which can be installed with `sudo apt install pyqt5-dev-tools` on linux

## Running
`make run` on systems with make installed

On Windows, run packman.bat or type `py packman\packman.py`

### Installing dependencies with make 
>make deps

### Installing dependencies manually
>python3 -m pip install -r requirements.txt

# How to use
The backlog level is a field that is subtracted from the GB and MB values
This was added in case the user wanted to keep track of how much data they used beyond a threshold or values that were larger and therefore harder to keep track of. For example, if your Download is 550 MB, setting a backlog of 550 will reset it to 0 and but will continue increasing like before.

`makegui.py`: This creates python files in the gui directory of any ui file in the ui directory (for contributors)

Note that this app makes use of the psutil `net_io_counters` method to grab data based on the network interface 

## Milestone
- [x] Minimize to tray option
- [ ] Graph feature
- [ ] Ability to install
- [x] Data uploaded view
- [ ] Data usage limits/alarms
