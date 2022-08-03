'''pip package for a internal use of data-table.com'''
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='data_table_utils',
    version='0.0.2',
    author='Sachin Patney',
    author_email='admin@nope.com',
    description='Utils for data-table.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/spatney/data-table-utils',
    project_urls={
        "Bug Tracker": "https://github.com/spatney/data-table-utils/issues"
    },
    license='MIT',
    packages=['data_table_utils'],
    install_requires=['redis==4.3.4', 'pika==1.3.0'],
)
