from invoke import run
from invoke import task


@task
def clean(ctx):
    ctx.run('rd /S /Q .\\build')
    ctx.run('rd /S /Q .\\dist')
    ctx.run('del .coverage')


@task
def build_docs(ctx):
    print('Building documentation...')
    ctx.run('make clean')
    ctx.run('make html')
    ctx.run('sphinx-apidoc -o ../release ../ini_handler')
    print('Complete')


@task
def run_unit_tests(ctx):
    print('Starting tests...')
    ctx.run('nosetests -v --with-coverage --cover-erase \
            --cover-package ./tests/unit-tests')
    print('Complete')
