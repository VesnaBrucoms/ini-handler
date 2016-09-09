from invoke import run
from invoke import task


@task
def build_docs(ctx):
    """Cleans out the old output, then builds the HTML.
    """
    print('Building documentation...')
    ctx.run('make clean')
    ctx.run('make html')
    ctx.run('sphinx-apidoc -o ../release ../ini_handler')
    print('Complete')


@task
def run_unit_tests(ctx):
    """Runs the unittests in one go, with a coverage report.
    """
    print('Starting tests...')
    ctx.run('nosetests -v --with-coverage --cover-erase \
            --cover-package=./tests/unit-tests')
    print('Complete')
