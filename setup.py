from setuptools import find_packages,setup

setup(
    name='text_gen',
    version='0.0.1',
    author='Gourav Dwivedi',
    author_email='gourav.dwivedi@gmail.com',
    install_requires=["pytesseract","pillow","streamlit","python-dotenv","pandas"],
    packages=find_packages()
)