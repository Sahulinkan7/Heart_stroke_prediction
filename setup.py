from setuptools import setup,find_packages

HYPHEN_E_DOT= "-e ."
PROJECT_NAME = "Heart_Stroke_Prediction"
VERSION="0.0.1"

def get_requirements(r_file="requirements.txt"):
    with open(r_file) as file:
        requirements=file.readlines()
        requirements = [ r.replace("\n","") for r in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        return requirements

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author="Linkan Kumar Sahu",
    author_email="sahulinkan7@gmail.com",
    install_requires = get_requirements(),
    packages=find_packages()
)