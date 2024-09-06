from setuptools import setup


setup(
  name='invoicing_for_pdfs',
  packages=['invoicing'],
  version='1.0.0',
  license='MIT',             # Type of licence. More here: https://help.github.com/articles/licensing-a-repository
  description='This is my package for converting Excel invoices to PDF '\
              'invoices. It is an example of package creation from Ardit '\
              'Sulce\'s course. Enjoy!',
  author='Orengasi Bassey',
  author_email='orengasi@gmail.com',
  url='https://github.com/renganomics',
  keywords=['invoice', 'excel', 'pdf'],
  install_requires=['pandas', 'fpdf', 'openpyxl'],
  classifiers=[
    'Development Status :: 3 - Alpha',          # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Type a licence again
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
  ],
)
