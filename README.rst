This is an example Turbogears project to show how to implement server-side events (SSE, browsers use it as EventSource) for event streaming.

If you you want to use the controllers in plain Pylons, make sure to get rid of Turbogear's decorators sugar.

There are two example controllers: One for simple event streaming, one for server-side asynchronous stuff using the gevent library.

Installation and Setup
======================

Create a virtual Python environment and activate it::

    $ virtualenv --no-site-packages -p python2.6 turbogears-eventstream-examples
    $ cd turbogears-eventstream-examples
    $ source bin/activate

Clone this project::

    $ git clone git://github.com/nh2/eventstreamexamples.git

Install ``eventstreamexamples`` using the setup.py script::

    $ cd eventstreamexamples
    $ python setup.py install

Start the paste http server::

    $ paster serve development.ini

Or for the gevent example::

    $ paster serve development-gunicorn.ini

While developing you may want the server to reload after changes in package files (or its dependencies) are saved. This can be achieved easily by adding the --reload option, but only works for the non-gevent example::

    $ paster serve --reload development.ini

Then you are ready to go.
Thanks to Alexandre Bourget for his blog post about `HTML5's EventSource in Pylons`_.

.. _`HTML5's EventSource in Pylons`: http://blog.abourget.net/2010/6/16/html5-eventsource-in-pylons-read-comet-ajax-polling/
