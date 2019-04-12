.. _setup_guide:

Setup Guide
============

This SDK is written for Python 2.7.x Future work includes developing a Python 3 version.


1. Install Python
^^^^^^^^^^^^^^^^^^^

If you do not already have Python 2.7.x on your computer you must install the Python programming language or the
Anaconda distribution of Python (both are free). If you are a scientist, engineer, researcher, or student, Anaconda is
recommended. It comes bundled with many useful Python scientific/numerical libraries, a GUI for managing the libraries,
and several open-source software development tools. If you want a more straightforward, lightweight software development
setup, the standard distribution of Python is recommended.

Installing Python
-----------------

Install `Python 2.7.16 <https://www.python.org/downloads/release/python-2716/>`_.

Installing Anaconda
--------------------

Install the **Python 2.7 version** of the `Anaconda Distribution <https://www.anaconda.com/download/>`_.


2. If you chose the standard distribution of Python 2.7, install pip.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

PIP is a Python package (library) manager. Follow these
`installation instructions <https://pip.pypa.io/en/stable/installing/>`_. (PIP comes with the Anaconda distribution.)


3. Create a virtual environment or conda environment (optional).
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

While not required, it is recommend that you use a virtual environment (or conda environment). A "virtual env" is
described in the Python documentation as follows:

::

    "virtualenv allows you to manage separate package installations for different projects. It essentially allows you to
    create a 'virtual' isolated Python installation and install packages into that virtual installation. When you switch
    projects, you can simply create a new virtual environment and not have to worry about breaking the packages
    installed in the other environments. It is always recommended to use a virtualenv while developing Python
    applications.

This concept is implemented slightly differently between standard Python and Anaconda. First create a directory for your
project, then follow the relevant instructions:

Instructions for Anaconda 2
----------------------------

Open the "Anaconda Prompt" terminal that comes with the Anaconda distribution, navigate to your project's directory and
follow instructions for `creating a conda environment
<https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands>`_
and `activating a conda environment
<https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment>`_.

Instructions for Python
------------------------

Open a terminal/command prompt, navigate to your new project's directory, and follow the instructions for
`installing and using virtualenv <https://docs.python-guide.org/dev/virtualenvs/#lower-level-virtualenv>`_.

4. Install plantpredict via pip
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

While in an activated virtualenv/conda enviornment, install the :py:mod:`plantpredict` package via pip:

.. code-block::

    pip install plantpredict

5. Get client credentials (link to OAuth2).
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Follow the steps in :ref:`authentication_oauth2` to obtain API credentials and authenticate with the server.

6. Enjoy automating all of your energy prediction-based analysis!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use the tutorials in :ref:`example_usage` as a starting point for your own scripting and analysis. Detailed
documentation on each class and method can be found in :ref:`sdk_reference`.