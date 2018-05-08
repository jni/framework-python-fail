from setuptools import setup

descr = """Show off validators in Gooey."""

DISTNAME            = 'framework-python-fail'
DESCRIPTION         = descr
LONG_DESCRIPTION    = descr
MAINTAINER          = 'Juan Nunez-Iglesias'
MAINTAINER_EMAIL    = 'juan.nunez-iglesias@monash.edu'
URL                 = 'https://github.com/jni/framework-python-fail'
LICENSE             = 'BSD 3-clause'
DOWNLOAD_URL        = 'https://github.com/jni/framework-python-fail'
VERSION             = '0.0.1-dev'
PYTHON_VERSION      = (3, 6)
INST_DEPENDENCIES   = []


if __name__ == '__main__':

    setup(name=DISTNAME,
        version=VERSION,
        url=URL,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        author=MAINTAINER,
        author_email=MAINTAINER_EMAIL,
        license=LICENSE,
        classifiers=[
            'Development Status :: 1 - Planning',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: BSD 3-clause',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Topic :: Scientific/Engineering',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: POSIX',
            'Operating System :: Unix',
            'Operating System :: MacOS',
        ],
        packages=['framework'],
        package_data={},
        install_requires=INST_DEPENDENCIES,
        entry_points = {
            'console_scripts': ['framework-fail=framework.example:main']
        }
    )

