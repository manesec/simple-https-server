from setuptools import setup, find_packages

def read_requirements(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line and not line.startswith('#')]

def install_requirements():
    all_requirements = []
    all_requirements.extend(read_requirements('src/requirements.txt'))
    return all_requirements

setup(
    name='simple-https-server',
    version='0.0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            "simple-https-server = src.start:start_server",
        ],
    },
    install_requires=install_requirements(),
    python_requires='>=3.6',
    author='ImpostorKeanu, manesec',
    author_email='ImpostorKeanu',
    description='It\'s a quick HTTPS server.',
    include_package_data=True,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/manesec/simple-https-server',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
