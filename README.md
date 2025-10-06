
# Jupyter notebook + Huey

Example project using Jupyter Notebook and the Huey queuing system configured
with Greenlet workers. The project includes basic examples and useful patterns
for running tasks with Huey.

The objective of the project is purely didactic.


## Set up dependencies

Create a python virtual environment:

```sh
python3 -m venv .venv
```

Activate the virtual environment:

```sh
source .venv/bin/activate
```

Install dependencies:

```sh
pip install -r requirements.txt
```

## Start Project

In a terminal with the virtual environment activated run the huey consumer:

```sh
huey_consumer.py consumer_entrypoint.huey -w 10 -k greenlet

```

In a different terminal, also with the virtual environment activated, run
the command to initialize the jupyter notebook:

```sh
jupyter notebook
```

You can open the examples from the notebook interface, the file name
is `huey_example.ipynb`.


## References


- <https://huey.readthedocs.io/en/latest/>
- <https://huey.readthedocs.io/en/latest/guide.html>
- <https://huey.readthedocs.io/en/latest/consumer.html#using-gevent>

