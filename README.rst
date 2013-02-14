collective.localfunctions
=========================

A sample package demonstrating how to allow use of modules and types in Restricted Python.

Background: "Scripts" and TALES "python:" expressions are limited to the modules and types that have been marked as (relatively) safe for use in through-the-web scripting. The list of modules is deliberately small, but may be expanded through explicit declarations.

This package demonstrates how to add modules and types to the Restricted Python allowed list.
The demonstration makes available a few modules that I've found particularly useful when working with PloneFormGen overrides and script adapters: rd, StringIO and csv.

Using collective.localfunctions
-------------------------------

Either download the package from github <https://github.com/collective/collective.localfunctions/archive/master.zip> or fork it from https://github.com/collective/collective.localfunctions.
Drop the distribution package in ./src and add it to your buildout develop and egg lists and make sure it works with your Zope/Plone. Then, add packages and types to meet your needs. Remember that everything you expose is a vulnerability, so weigh the advantages of exposure against the risks.

