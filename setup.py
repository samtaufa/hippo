from distutils.core import setup

long_description = """
Hippo is a host repository for tracking system configuration files.

Hippo is a thin layer built on top of Git that simplifies managing a host-wide repository of files with metadata (permissions and ownership). Conceptually, Hippo simply serializes metadata before certain Git commands are run, and restores file metadata after others. By default, the host-wide git repository lives in /var/hippo/.git, metadata is tracked in /var/hippo/manifest.

Hippo requires Python 2.6 or newer.
"""

version = "0.1.0"

setup(
        name = "hippo",
        version = version,
        description = "Hippo is a host repository for tracking system configuration files.",
        long_description = long_description,
        author = "Aldo Cortesi",
        author_email = "aldo@corte.si",
        url = "http://dev.nullcube.com",
        download_url="http://dev.nullcube.com/download/hippo-%s.tar.gz"%version,
        packages = ["libhippo"],
        scripts = ["hippo"],
        classifiers = [
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Development Status :: 4 - Beta",
            "Programming Language :: Python",
            "Operating System :: OS Independent",
            "Topic :: Software Development :: Testing",
            "Topic :: Software Development :: Quality Assurance",
        ]
)
