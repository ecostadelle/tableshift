#!/usr/bin/env python

from distutils.core import setup

setup(name='tableshift',
      version='0.1',
      url='https://tableshift.org',
      description='A tabular data benchmarking toolkit.',
      long_description='A benchmarking toolkit for tabular data under distirbution shift. '
                       'For more details, see the paper '
                       '"Benchmarking Distribution Shift in Tabular Data with TableShift", '
                       'Gardner, Popovic, and Schmidt, 2023.',
      author='Josh Gardner',
      author_email='jpgard@cs.washington.edu',
      packages=['tableshift'],
      data_files=[('tableshift/datasets',
                   ['tableshift/datasets/nhanes_data_sources.json',
                    'tableshift/datasets/icd9-codes.json'])],
      install_requires=[
          'numpy==1.23.5',
          'ray==2.2.0',
          'torch==1.13.0',
          'torchvision==0.14.0',
          'scikit-learn==1.1.3',
          'pandas==1.3.5',
          'fairlearn==0.8.0',
          'folktables',
          'frozendict==2.3.4',
          'rtdl==0.0.13',
          'xport==3.6.1',
          'tqdm==4.64.1',
          'hyperopt==0.2.7',
          'h5py==3.8.0',
          'tables==0.2.1',
          'category_encoders==1.2',
          'einops==0.6.0',
          'tab-transformer-pytorch==0.2.1',
          'openpyxl==3.1.2',
          'optuna==3.1.1',
          'kaggle==1.5.13',
          'datasets==2.11.0',
          'torchinfo==1.8.0'
      ]
      )
