Engineering Pipelines
=====================

A web app designed to help engineers with doing the mundane numerical work 
needed for solving engineering problems.


Usage
-----

Docker Machine
^^^^^^^^^^^^^^

To get started with developing, I usually use spin up a digitalocean VM with 
`docker-machine`, then kill it afterwards. In this example, I've decided to
call my machine "docker-sandbox", feel free to name yours whatever you want. 
To spin the machine up you can do::

    docker-machine create --driver digitalocean \
        --digitalocean-access-token $DIGITAL_OCEAN_KEY \
        --digitalocean-image ubuntu-16-04-x64 \
        --digitalocean-size "2gb" \
        docker-sandbox

(substituting in your own digitalocean API key, obviously)

Spinning up a new machine may take a couple seconds. Afterwards, to check which
machines are available you can do::

    docker-machine ls

Then if you want to use a particular machine, you just need to set the correct
environment variables so docker knows who to talk to. ::

    docker-machine use docker-sandbox

You can get access to the other machine with::

    docker-machine ssh docker-sandbox

Now that docker is set up to automatically provision other boxes, you can build
and run the containers necessary for this app.

.. note::
    For more information, check out `digitalocean's official tutorial`_ for
    setting up a remote host with docker-machine.

Starting The Containers
^^^^^^^^^^^^^^^^^^^^^^^

Web applications are often complex things with many moving parts. Docker allows
us to separate these moving parts and package them into "standard" containers.
Want an SQL database? Just spin up the official `postgres container`_. Need
redis to do some caching, use the `redis container`_. You get the idea.

Using this methodology allows you to spin up a database in under a second and
then point your app at it. You don't have to worry about anything else, and
your development set-up will be identical to what you're running in 
production. The `docker-compose` tool allows you to link several containers 
together without needing to expose ports on the host machine.

To spin up and configure everything with one command run from the project root. 

::
    docker-compose up

Docker, docker-compose, and docker-machine will do the rest.

You should now be able to point your web browser at the digitalocean VMs IP
address (`docker-machine ip docker-sandbox`), and access the app like normal.


Help
----

The way the project is designed based on `this blog post`_. For both testing
and production, `docker` and `docker-machine` will be used extensively to make
it easy link the actual web app up with other things like a postgres database,
or the nginx web proxy.



.. _this blog post: https://realpython.com/blog/python/django-development-with-docker-compose-and-machine/
.. _postgres container: https://hub.docker.com/_/postgres/
.. _redis container: https://hub.docker.com/_/redis/
.. _digitalocean's official tutorial: https://www.digitalocean.com/community/tutorials/how-to-provision-and-manage-remote-docker-hosts-with-docker-machine-on-ubuntu-16-04
