from setuptools import setup, find_packages

setup(name='libbuild',
      version='0.1',
      description='Libbuild that does not require antipackage',
      url='https://github.com/appscodelabs/libbuild',
      py_modules=['libbuild', 'pydotenv'],
      packages=find_packages(),
      install_requires=['pyyaml'],
      include_package_data=True,
      zip_safe=False)
