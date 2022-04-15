from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    page_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='image-processing-rapha',
    version='0.0.1',
    author='Raphael Cavalcanti',
    author_email='raphaelcavalcantizero@gmail.com',
    description='Package for image processing',
    long_description=page_description,
    long_description_content_type='text/markdown',
    url='github.link',
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.10',
)
