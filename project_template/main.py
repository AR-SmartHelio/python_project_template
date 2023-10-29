import os
import subprocess
import click

@click.command()
@click.argument('path')
def create_project_structure(path):
    base_path = os.path.abspath(path)
    os.makedirs(base_path, exist_ok=True)

    # Create directories
    dirs = [
        'src',
        'tests',
        'data/raw',
        'data/processed',
        'notebooks',
        'docs'
    ]

    for directory in dirs:
        os.makedirs(os.path.join(base_path, directory), exist_ok=True)

    # Create main.py in src
    with open(os.path.join(base_path, 'src', 'main.py'), 'w') as f:
        f.write('def main():\n    print("Hello, world!")\n\n\nif __name__ == "__main__":\n    main()')

    # Create utils.py in src
    with open(os.path.join(base_path, 'src', 'utils.py'), 'w') as f:
        f.write('''def sample_utility_function():
    print("This is a sample utility function. Update this with actual utilities!")
''')

    # Create consts.py in src
    with open(os.path.join(base_path, 'src', 'consts.py'), 'w') as f:
        f.write('''# Sample constant
SAMPLE_CONSTANT = "This is a sample constant. Update this with actual constants!"
''')

    # Create config.yaml
    with open(os.path.join(base_path, 'config.yaml'), 'w') as f:
        f.write('# Configuration for the project\n')

    # Create requirements.txt
    with open(os.path.join(base_path, 'requirements.txt'), 'w') as f:
        f.write('numpy\npandas\nplotly\nflake8\nblack\npytest\n')

    # Generate a sample test in the tests directory
    test_content = """
def test_sample():
    assert True, "Sample test. Please replace with your own tests!"
"""
    with open(os.path.join(base_path, 'tests', 'test_sample.py'), 'w') as f:
        f.write(test_content)

    # Initialize git
    subprocess.run(['git', 'init'], cwd=base_path)

    # Create .gitignore
    gitignore_content = """
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*.pyd
*.pyo
*.egg
*.egg-info/
dist/
build/

# Virtual environment
venv/
"""
    with open(os.path.join(base_path, '.gitignore'), 'w') as f:
        f.write(gitignore_content)

    # Create .flake8
    flake8_content = """
[flake8]
ignore = E203, E266, E501, W503
max-line-length = 88
"""
    with open(os.path.join(base_path, '.flake8'), 'w') as f:
        f.write(flake8_content)

    # Create pyproject.toml
    pyproject_content = """
[tool.black]
line-length = 88
include = '\\.pyi?$'
exclude = '''
/(
    \.git
  | \.venv
  | \.env
  | _build
  | buck-out
  | build
  | dist
)/
'''
"""
    with open(os.path.join(base_path, 'pyproject.toml'), 'w') as f:
        f.write(pyproject_content)

    # Initial commit
    subprocess.run(['git', 'add', '.'], cwd=base_path)
    subprocess.run(['git', 'commit', '-m', 'Initial project setup'], cwd=base_path)

    print("Project setup complete!")


if __name__ == "__main__":
    create_project_structure()
