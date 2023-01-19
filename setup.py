#!/usr/bin/env python

try:

    from setuptools import setup, find_packages
    import python4poets


    # read the description
    with open('README.md') as f: LONG_DESCRIPTION = f.read()
    with open("requirements.txt") as f:
        requirements = [x.strip() for x in f.read().split('\n') if x.strip()]



    CLASSIFIERS = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',        
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]

    test_requirements = [] #['pytest>=3.6', 'pytest-cov']
    setup_requires = [] # ['pytest-runner']

    setup(
        name='python4poets',
        version=python4poets.__version__,
        author='The Center for Digital Humanities at Princeton',
        author_email='cdhdevteam@princeton.edu',
        url='https://github.com/princeton-cdh/python4poets',
        license='Apache License, Version 2.0',
        packages=find_packages(),
        install_requires=requirements,
        setup_requires=setup_requires,
        tests_require=test_requirements,
        # extras_require={
            # 'test': test_requirements
        # },
        description='Code and resources for poets learning python',
        long_description=LONG_DESCRIPTION,
        long_description_content_type='text/markdown',
        classifiers=CLASSIFIERS,
    )


except Exception as e:
    print(f'installation failed: {e}')
