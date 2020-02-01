import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='pvlv_database',
    version='0.0.1',
    author='AbbestiaDC',
    author_email='',
    description='Database connector for Pavlov',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/The-Pavlov-Project/Pavlov-Database',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    python_requires='>=3.6',
)
