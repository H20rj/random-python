# ApplicationTracker - H20rj
## Must have: Python 3.13, pip

## How to use:
### Clone the git repository into a folder on computer
### Open python in the directory and run 
### Windows: `py main.py`
### macOS: `python3 main.py`


### Required Modules:
  
- `colorama`: For colorful terminal output
- `pwinput`: For securely handling password input

To install these dependencies, run the setup.sh file in the directory.
This will automagically install the needed modules.



## Usage

The application uses a default username and password:

- **Username**: `user`
- **Password**: `password`

After entering the correct credentials, you will be able to use the application to track acceptances.
Once successful authentication with the default credentials, the user will be able to change the pass word to their own.

### Inside the application you can:
1. View your statuses for applications (once set)
2. Change application statuses
3. Stay secure with a username and password

## Installation and Running the Program

1. Clone or download the repository.
2. Install the required modules (as mentioned above).
3. Open the cloned directory in terminal.
4. Run the Python script using the run.sh file.



## Currently experimenting with GUI. Just for viewing status and changing statuses right now. Must set statuses in main.py first, then run test_gui.py with:
Windows: `py test_gui.py`\
macOS: `python3 test_gui.py`
## All save files work, so the GUI and CLI are interchangeable; however, you can only change the username and password in the CLI. 
## About

This project was created on a sick day at school. It may not be fully optimized, but it’s a good starting point for tracking acceptances.
