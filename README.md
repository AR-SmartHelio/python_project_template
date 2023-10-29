#### Project Template Generator

Easily set up a new Python project with a structured directory, virtual environment, and essential configuration files.

🚀 Installation

To install the Project Template Generator, simply run the following command in your terminal:

Make sure you have Python 3.6 or higher installed with pip.
To check your Python and pip versions, run the following commands in your terminal:

``` python```
```
python --version
pip --version
```

```Python```
```
pip install git+https://github.com/AR-SmartHelio/python_project_template.git
```


💼 Usage

Once installed, run the following command in your terminal:

Make sure to give the absolute path to the directory where you want to create your project.

```Python```
```
generate_project "D:\test_project"
```

This will scaffold a project in the directory D:\test_project with the structure:

```
test_project/                      # The directory you provide
│
├── src/
│   ├── main.py                    # Contains your main application code
│   ├── utils.py                   # Sample utility functions
│   └── consts.py                  # Constants for your project
│
├── tests/                         # Unit tests go here
│
├── data/
│   ├── raw/                       # Raw data storage
│   └── processed/                 # Processed data storage
│
├── notebooks/                     # Jupyter notebooks for analysis
│
├── docs/                          # Documentation (empty by default)
│
├── config.yaml                    # Configuration settings
├── requirements.txt               # Project dependencies
├── .gitignore                     # Specifies which files Git should ignore
├── .flake8                        # flake8 linting config
└── pyproject.toml                 # black code formatter config
```

🔥 Bonus:

If git is accessible in your environment, the tool will also initialize a Git repository in the project directory and make an initial commit titled "Initial project setup."

Happy coding! 🎉