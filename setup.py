from setuptools import find_packages,setup

setup(
    name="Ecommerce bot",
    version="1.0.0",
    author="Debdoot",
    packages=find_packages(),
    install_requires=['langchain-astradb','langchain','langchain_groq','datasets','python-dotenv','flask']
    
)