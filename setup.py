from distutils.core import setup

setup(
    name = 'ccdaviewer',     
    packages = ['ccdaviewer'],  
    version = '0.1.1', 
    license='MIT',      
    description = 'This is the python client to the API hosted by https://www.ccdaviewer.com', 
    author = 'Tanaka Chiromo',                   
    author_email = 'tanakachiromo@gmail.com',   
    url = 'https://github.com/tanaka-chiromo/ccdaviewer',  
    download_url = 'https://github.com/tanaka-chiromo/ccdaviewer/archive/refs/tags/v_011.tar.gz',
    keywords = ['ccdaviewer', 'API', 'Client'],  
    install_requires=[      
            'requests'
        ],
    classifiers=[
        'Development Status :: 5 - Stable',    
        'Intended Audience :: Developers',     
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License', 
        'Programming Language :: Python :: 3'  
    ],
    python_requires='>=3.6',
    )