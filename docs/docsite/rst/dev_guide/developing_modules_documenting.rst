.. _module_documenting:

Documenting Your Module
=======================

.. contents:: Topics

The online module documentation is generated from the modules themselves.
As the module documentation is generated from documentation strings contained in the modules, all modules included with Ansible must have a ``DOCUMENTATION`` string.
This string must be a valid YAML document
which conforms to the schema defined below. You may find it easier to
start writing your ``DOCUMENTATION`` string in an editor with YAML
syntax highlighting before you include it in your Python file.

All modules must have the following sections defined in this order:

1. ANSIBLE_METADATA
2. DOCUMENTATION
3. EXAMPLES
4. RETURNS
5. Python imports

.. note:: Why don't the imports go first?

  Keen Python programmers may notice that contrary to PEP8's advice we don't put ``imports`` at the top of the file. This is because the ``ANSIBLE_METADATA`` through ``RETURNS`` sections are not used by the module code itself; they are essentially extra docstrings for the file. The imports are placed after these special variables for the same reason as PEP8 puts the imports after the introductory comments and docstrings. This keeps the active parts of the code together and the pieces which are purely informational apart. The decision to exclude E402 is based on readability (which is what PEP8 is about). Documentation strings in a module are much more similar to module level docstrings, than code, and are never utilized by the module itself. Placing the imports below this documentation and closer to the code, consolidates and groups all related code in a congruent manner to improve readability, debugging and understanding.

.. warning:: Why do some modules have imports at the bottom of the file?

  If you look at some existing older modules, you may find imports at the bottom of the file. Do not copy that idiom into new modules as it is a historical oddity due to how modules used to be combined with libraries. Over time we're moving the imports to be in their proper place.



ANSIBLE_METADATA Block
----------------------

ANSIBLE_METADATA contains information about the module for use by other tools. At the moment, it informs other tools which type of maintainer the module has and to what degree users can rely on a module's behaviour remaining the same over time.

For new modules, the following block can be simply added into your module

.. code-block:: python

   ANSIBLE_METADATA = {'status': ['preview'],
                       'supported_by': 'community',
                       'version': '1.0'}

.. warning:: version field

   This is the version of the ``ANSIBLE_METADATA`` schema, *not* the version of the module.

.. warning::

   Promoting a module's ``status`` or ``supported_by`` status should only be done by members of the Ansible Core Team.

Version 1.0 of the metadata
+++++++++++++++++++++++++++

Structure
`````````

.. code-block:: python

  ANSIBLE_METADATA = {
      'version': '1.0',
      'supported_by': 'core|community|unmaintained|committer',
      'status': ['stableinterface|preview|deprecated|removed']
  }

Fields
``````

:version: An “X.Y” formatted string. X and Y are integers which
   define the metadata format version. Modules shipped with Ansible are
   tied to an Ansible release, so we will only ship with a single version
   of the metadata. We’ll increment Y if we add fields or legal values
   to an existing field. We’ll increment X if we remove fields or values
   or change the type or meaning of a field.
:supported_by: This field records who supports the module.
   Default value is community. Values are:

   :core: Maintained by the Ansible core team. Core team will fix
      bugs, add new features, and review PRs.
   :community: This module is maintained by the community at large,
      which is responsible for fixing bugs, adding new features, and
      reviewing changes.
   :unmaintained: This module currently needs a new community
      contributor to help maintain it.
   :committer: Committers to the Ansible repository are the
      gatekeepers for this module. They will review PRs from the community
      before merging but might not generate fixes and code for new features
      on their own.

:status: This field records information about the module that is
   important to the end user. It’s a list of strings. The default value
   is a single element list [“preview”]. The following strings are valid
   statuses and have the following meanings:

   :stableinterface: This means that the module’s parameters are
      stable. Every effort will be made not to remove parameters or change
      their meaning. It is not a rating of the module’s code quality.
   :preview: This module is a tech preview. This means it may be
      unstable, the parameters may change, or it may require libraries or
      web services that are themselves subject to incompatible changes.
   :deprecated: This module is deprecated and will no longer be
      available in a future release.
   :removed: This module is not present in the release. A stub is
      kept so that documentation can be built. The documentation helps
      users port from the removed module to new modules.

DOCUMENTATION Block
-------------------

See an example documentation string in the checkout under `examples/DOCUMENTATION.yml <https://github.com/ansible/ansible/blob/devel/examples/DOCUMENTATION.yml>`_.

Include it in your module file like this:

.. code-block:: python

    #!/usr/bin/python
    # Copyright header....

    DOCUMENTATION = '''
    ---
    module: modulename
    short_description: This is a sentence describing the module
    # ... snip ...
    '''


The following fields can be used and are all required unless specified otherwise:

:module:
  The name of the module. This must be the same as the filename, without the ``.py`` extension.
:short_description:
  * A short description which is displayed on the :doc:`../list_of_all_modules` page and ``ansible-doc -l``.
  * As the short description is displayed by ``ansible-doc -l`` without the category grouping it needs enough detail to explain its purpose without the context of the directory structure in which it lives.
  * Unlike ``description:`` this field should not have a trailing full stop.
:description:
  * A detailed description (generally two or more sentences).
  * Must be written in full sentences, i.e. with capital letters and fullstops.
  * Shouldn't mention the name module.
:version_added:
  The version of Ansible when the module was added.
  This is a `string`, and not a float, i.e. ``version_added: "2.1"``
:author:
  Name of the module author in the form ``First Last (@GitHubID)``. Use a multi-line list if there is more than one author.
:options:
  One per module argument:
  
  :option-name:

    * Declarative operation (not CRUD)–this makes it easy for a user not to care what the existing state is, just about the final state, for example `online:`, rather than `is_online:`.
    * The name of the option should be consistent with the rest of the module, as well as other modules in the same category.

  :description:

    * Detailed explanation of what this option does. It should be written in full sentences.
    * Should not list the options values (that's what ``choices:`` is for, though it should explain `what` the values do if they aren't obvious.
    * If an argument takes both True)/False and Yes)/No, the documentation should use True and False.
    * If an optional parameter is sometimes required this need to be reflected in the documentation, e.g. "Required when I(state=present)."
    * Mutually exclusive options must be documented as the final sentence on each of the options.
  :required:
    Only needed if true, otherwise it is assumed to be false.
  :default:

    * If `required` is false/missing, `default` may be specified (assumed 'null' if missing).
    * Ensure that the default parameter in the docs matches the default parameter in the code.
    * The default option must not be listed as part of the description.
  :choices:
    List of option values. Should be absent if empty.
  :aliases:
    List of option name aliases; generally not needed.
  :version_added:
    Only needed if this option was extended after initial Ansible release, i.e. this is greater than the top level `version_added` field.
    This is a string, and not a float, i.e. ``version_added: "2.3"``.
  :requirements:
    List of requirements, and minimum versions (if applicable)
  :notes:
    Details of any important information that doesn't fit in one of the above sections; for example if ``check_mode`` isn't supported, or a link to external documentation.


.. note::

   - The above fields are are all in lowercase.

   - There is no need to document the ``type:`` of an option.

   - If the module doesn't doesn't have any options (for example, it's a ``_facts`` module), you can use ``options: {}``.

EXAMPLES block
--------------

The EXAMPLES section is required for all new modules.

Examples should demonstrate real world usage, and be written in multi-line plain-text YAML format.

Ensure that examples are kept in sync with the options during the PR review and any following code refactor.

As per playbook best practice, a `name:` should be specified.

``EXAMPLES`` string within the module like this::

    EXAMPLES = '''
    - name: Ensure foo is installed
      modulename:
        name: foo
        state: present
    '''

If the module returns facts that are often needed, an example of how to use them can be helpful.

RETURN Block
------------

The RETURN section documents what the module returns, and is required for all new modules.

For each value returned, provide a ``description``, in what circumstances the value is ``returned``,
the ``type`` of the value and a ``sample``.  For example, from the ``copy`` module::

    RETURN = '''
    dest:
        description: destination file/path
        returned: success
        type: string
        sample: /path/to/file.txt
    src:
        description: source file used for the copy on the target machine
        returned: changed
        type: string
        sample: /home/httpd/.ansible/tmp/ansible-tmp-1423796390.97-147729857856000/source
    md5sum:
        description: md5 checksum of the file after running copy
        returned: when supported
        type: string
        sample: 2a5aeecc61dc98c4d780b14b330e3282
    ...
    '''

.. note::

   If your module doesn't return anything (apart from the standard returns), you can use ``RETURN = ''' # '''``.


Python Imports
--------------

Starting with Ansible version 2.2, all new modules are required to use imports in the form:

.. code-block:: python

   from module_utils.basic import AnsibleModule


.. warning::

   The use of "iwildcard" imports such as ``from module_utils.basic import *`` is no longer allowed.

Formatting options
------------------

These formatting functions are ``U()`` for URLs, ``I()`` for option names, ``C()`` for files and option values and ``M()`` for module names.
Module names should be specified as ``M(module)`` to create a link to the online documentation for that module.


Example usage::

    Or if not set the environment variable C(ACME_PASSWORD) will be used.
    ...
    Required if I(state=present)
    ...
    Mutually exclusive with I(project_src) and I(files).
    ...
    See also M(win_copy) or M(win_template).
    ...
    See U(https://www.ansible.com/tower) for an overview.


.. note::

  If you wish to refer a collection of modules, use ``C(..)``, e.g. ``Refer to the C(win_*) modules.``

Documentation fragments
-----------------------

Some categories of modules share common documentation, such as details on how to authenticate options, or file mode settings. Rather than duplicate that information it can be shared using ``docs_fragments``.

These shared fragments are similar to the standard documentation block used in a module, they are just contained in a ``ModuleDocFragment`` class.

All the existing ``docs_fragments`` can be found in ``lib/ansible/utils/module_docs_fragments/``.

To include, simply add in ``extends_documentation_fragment: FRAGMENT_NAME`` into your module.

Examples can be found by searching for ``extends_documentation_fragment`` under the Ansible source tree.

Testing documentation
---------------------

Put your completed module file into the ``lib/ansible/modules/$CATEGORY/`` directory and then
run the command: ``make webdocs``. The new 'modules.html' file will be
built in the ``docs/docsite/_build/html/$MODULENAME_module.html`` directory.

To test your documentation against your ``argument_spec`` you can use ``validate-modules``. Note that this option isn't currently enabled in Shippable due to the time it takes to run.

.. code-block:: bash

   # If you don't already, ensure you are using your local checkout
   source hacking/env-setup
   ./test/sanity/validate-modules/validate-modules --arg-spec --warnings  lib/ansible/modules/your/modules/

.. tip::

   If you're having a problem with the syntax of your YAML you can
   validate it on the `YAML Lint <http://www.yamllint.com/>`_ website.
