from distutils.core import setup

setup(
    name = 'ccdaviewer',         # How you named your package folder (MyLib)
    packages = ['ccdaviewer'],   # Chose the same as "name"
    version = '0.1.1',      # Start with a small number and increase it with every change you make
    license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description = 'This is the python client to the API hosted by https://www.ccdaviewer.com',   # Give a short description about your library
    author = 'Tanaka Chiromo',                   # Type in your name
    author_email = 'tanakachiromo@gmail.com',      # Type in your E-Mail
    url = 'https://github.com/tanaka-chiromo/ccdaviewer',   # Provide either the link to your github or to your website
    download_url = 'https://github.com/tanaka-chiromo/ccdaviewer/archive/refs/tags/v_011.tar.gz',    # I explain this later on
    keywords = ['ccdaviewer', 'API', 'Client'],   # Keywords that define your package best
    install_requires=[            # I get to this in a second
            'requests'
        ],
    classifiers=[
        'Development Status :: 5 - Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        'Programming Language :: Python :: 3'      #Specify which pyhton versions that you want to support
    ],
    )