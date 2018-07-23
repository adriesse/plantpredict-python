.. _setup_guide:

Setup Guide
============

This SDK is written for Python 2.7. Future work includes developing a Python 3 version

"I'm a first time Python user."
-------------------------------

1. Install Python via Anaconda
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Install the **Python 2.7 version** of the Anaconda Distribution `here <https://www.anaconda.com/download/>`_.
Anaconda Distribution is a quick way to download the Python programming language bundled with useful data
and science libraries.

2. Install PyCharm Community Edition.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Install PyCharm Community Edition (free) `here <https://www.jetbrains.com/pycharm/download/#section=windows>`_. PyCharm is
an "Integrated Development Environment" (IDE) - it is a software package that allows for writing, editing, running,
and debugging code, and much more. The PyCharm website contains a lot of useful documentation, such as a
`QuickStart Guide <https://www.jetbrains.com/help/pycharm/quick-start-guide.html>`_.


3. Configure PyCharm project interpreter.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Follow `these steps <https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html#local-interpreter>`_. to
configure your Project Interpreter in PyCharm. Make sure you follow the steps for "Configuring a local interpreter". In
 simple terms, this is how you "tell" PyCharm to use your preferred installation of Python (Anaconda, in this case).

Move onto the next section once you have completed the above steps.

.. note::

    This is just one way to set up your Python environment. It is recommended to those who want a quick, simple
    'packaged' setup. Some developers might prefer to download Python directly, use pip to install Python packages, and use
    a text editor with a command line tool.

Confirm that your project interpreter is properly set up by `running your Python console
<https://www.jetbrains.com/help/pycharm/running-console.html>`_ or
`running a file <https://www.jetbrains.com/help/pycharm/creating-and-running-your-first-python-project.html>`_.


"I already have my Python environment set up."
----------------------------------------------

1. Download plantpredict-python package.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Download the source code for plantpredict-python from `GitHub <https://github.com/stephenkaplan/plantpredict-python>`_.

2. Add the plantpredict python package to your Project Structure in PyCharm.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Add the "plantpredict" folder as a content root in your current project following
`these steps <https://www.jetbrains.com/help/pycharm/configuring-content-roots.html#create-content-root>`_.


3. Get client credentials (link to OAuth2).
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Follow the steps in :ref:`authentication_oauth2` to obtain API credentials and authenticate with the server.


3. Enjoy automating all of your energy prediction-based analysis!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Don't forget to create a folder outside of the plantpredict-python directory to store your code. Add that folder
as a content root as you did in `2. Add the plantpredict python package to your Project Structure in PyCharm.`_.
