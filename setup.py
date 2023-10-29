from setuptools import setup, find_packages

setup(
    name="project_template_generator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "generate_project = project_template.main:create_project_structure",
        ],
    },
    author="AR",
    author_email="roy.aalekh@gmail.com",
    description="A tool to generate a Python project template",
    license="MIT",
    keywords="python project template generator",
    url="https://github.com/yourusername/project_template_generator",  # GitHub repo URL or other URL
)
