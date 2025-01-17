**********************
OpenAPI Spec validator
**********************

.. image:: https://img.shields.io/pypi/v/openapi-spec-validator.svg
     :target: https://pypi.python.org/pypi/openapi-spec-validator
.. image:: https://travis-ci.org/python-openapi/openapi-spec-validator.svg?branch=master
     :target: https://travis-ci.org/python-openapi/openapi-spec-validator
.. image:: https://img.shields.io/codecov/c/github/python-openapi/openapi-spec-validator/master.svg?style=flat
     :target: https://codecov.io/github/python-openapi/openapi-spec-validator?branch=master
.. image:: https://img.shields.io/pypi/pyversions/openapi-spec-validator.svg
     :target: https://pypi.python.org/pypi/openapi-spec-validator
.. image:: https://img.shields.io/pypi/format/openapi-spec-validator.svg
     :target: https://pypi.python.org/pypi/openapi-spec-validator
.. image:: https://img.shields.io/pypi/status/openapi-spec-validator.svg
     :target: https://pypi.python.org/pypi/openapi-spec-validator

About
#####

OpenAPI Spec Validator is a Python library that validates OpenAPI Specs
against the `OpenAPI 2.0 (aka Swagger)
<https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md>`__,
`OpenAPI 3.0 <https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.3.md>`__
and `OpenAPI 3.1 <https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.1.0.md>`__
specification. The validator aims to check for full compliance with the Specification.


Documentation
#############

Check documentation to see more details about the features. All documentation is in the "docs" directory and online at `openapi-spec-validator.readthedocs.io <https://openapi-spec-validator.readthedocs.io>`__


Installation
############

.. code-block:: console

    pip install openapi-spec-validator

Alternatively you can download the code and install from the repository:

.. code-block:: bash

   pip install -e git+https://github.com/python-openapi/openapi-spec-validator.git#egg=openapi_spec_validator


Usage
#####

CLI (Command Line Interface)
****************************

Straight forward way:

.. code-block:: bash

    openapi-spec-validator openapi.yaml

pipes way:

.. code-block:: bash

    cat openapi.yaml | openapi-spec-validator -

docker way:

.. code-block:: bash

    docker run -v path/to/openapi.yaml:/openapi.yaml --rm p1c2u/openapi-spec-validator /openapi.yaml

or more pythonic way:

.. code-block:: bash

    python -m openapi_spec_validator openapi.yaml

For more details, read about `CLI (Command Line Interface) <https://openapi-spec-validator.readthedocs.io/en/latest/cli.html>`__.

Python package
**************

.. code:: python

    from openapi_spec_validator import validate_spec
    from openapi_spec_validator.readers import read_from_filename

    spec_dict, spec_url = read_from_filename('openapi.yaml')

    # If no exception is raised by validate_spec(), the spec is valid.
    validate_spec(spec_dict)

    validate_spec({'openapi': '3.1.0'})

    Traceback (most recent call last):
        ...
    OpenAPIValidationError: 'info' is a required property

For more details, read about `Python package <https://openapi-spec-validator.readthedocs.io/en/latest/python.html>`__.

Related projects
################

* `openapi-core <https://github.com/python-openapi/openapi-core>`__
   Python library that adds client-side and server-side support for the OpenAPI v3.0 and OpenAPI v3.1 specification.
* `openapi-schema-validator <https://github.com/python-openapi/openapi-schema-validator>`__
   Python library that validates schema against the OpenAPI Schema Specification v3.0 and OpenAPI Schema Specification v3.1.

License
#######

Copyright (c) 2017-2023, Artur Maciag, All rights reserved. Apache v2
