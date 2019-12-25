.. HKJournalist documentation master file, created by
   sphinx-quickstart on Fri Dec 20 16:29:31 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to HKJournalist's documentation!
========================================

|Python_Versions|_ |PyPI_Version|_ |GitHub|_ |TexLive|_

.. |Python_Versions| image:: https://img.shields.io/pypi/pyversions/hkjournalist.svg
.. _Python_Versions: https://pypi.org/project/hkjournalist

.. |PyPI_Version| image:: https://img.shields.io/pypi/v/hkjournalist.svg
.. _PyPI_Version: https://pypi.org/project/hkjournalist

.. |GitHub| image:: https://img.shields.io/github/forks/li-xin-yi/hk-journalist?style=social.svg
.. _GitHub: https://github.com/li-xin-yi/hk-journalist/fork

.. |TexLive| image:: https://img.shields.io/badge/TeXLive-2018/2019-important.svg
.. _TexLive: https://www.tug.org/texlive/

* Slides for sharing: `Download Link <https://github.com/li-xin-yi/HK-journalist/raw/master/slides/slides.pdf>`_

It is a light and useful Python module, helping you generate a small size, pretty report as PDF slides (or any other format documents which human can directly read and hand out) each time after your programs finish. All you need to do is to customize a report template using ``MarkDown`` with variables name which used in your Python program, and maintain a ``dict`` to store those variables. Then, A few lines of code added before end of programs can automatically fetch and display them in final report file. Also, code deal with frequent structure/arguments changes or data source changes can benefit from the package if the report can play a role of 'snapshot' (with timestamp) of each code version.

.. toctree::
   :maxdepth: 2
   :caption: Home:

   Quick Start<source/quick-start.md>
   Auto Generate Template<source/template-generate.md>
   Tutorial 1: Run a prophet model on time series<source/tutorial_1.md>
   Tutorial 2: EDA and select feature<source/tutorial_2.md>
   API<source/hkjournalist.rst>



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
