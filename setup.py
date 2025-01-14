from setuptools import setup, find_packages

setup(
    name='rapidsms-xforms',
    version=__import__('rapidsms_xforms').__version__,
    license="BSD",

    install_requires = [
        "django>=1.5",
        "rapidsms==1.1.0",
        "django-uni-form",
        "python-digest==1.7",
        "django-digest==1.13"
    ],

    description='Interactive form builder for both XForms and SMS submissions into RapidSMS',
    long_description=open('README.rst').read(),

    author='Nicolas Pottier, Eric Newcomer',
    author_email='code@nyaruka.com',

    url='http://github.com/nyaruka/rapidsms-xforms',
    download_url='http://github.com/nyaruka/rapidsms-xforms/downloads',

    include_package_data=True,

    packages=find_packages(),

    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
