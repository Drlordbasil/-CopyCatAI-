# Self-Replicating AI Python Project

This Python project is a self-replicating AI program that allows you to create copies of itself and run them. The project utilizes the `os`, `shutil`, and `subprocess` libraries to achieve its functionality.

## Program Description

The `Replicator` class in the program facilitates the creation of copies of the main program file (`replicator.py`). The `create_copy` method creates a copy of the program file by using the `shutil.copyfile` function. It ensures that the copy is not created if the program is executed on itself. The `run_copy` method executes the copied program using the `subprocess.call` function.

## Installation

To use this program, follow the steps below:

1. Clone this repository to your local machine.
2. Ensure you have Python installed on your system.
3. Install the required dependencies by running the following command:
```
pip install -r requirements.txt
```

## Usage

1. Navigate to the project directory.

2. Create a copy of the program by running the following command:
```
python replicator.py create
```
If successful, it will display a message indicating the creation of the program copy.

3. Run the copied program by executing the following command:
```
python copy_replicator.py
```
This will execute the replicated version of the program.

## Contributing

Contributions to this project are welcome! If you encounter any issues or have suggestions for improvement, please feel free to open a new issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- The `os` library: https://docs.python.org/3/library/os.html
- The `shutil` library: https://docs.python.org/3/library/shutil.html
- The `subprocess` library: https://docs.python.org/3/library/subprocess.html