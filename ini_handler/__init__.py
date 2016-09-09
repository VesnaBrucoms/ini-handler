from pkgutil import extend_path

if __name__ == '__main__':
    __path__ = extend_path(__path__, __name__)

__version__ = '0.4.0'
__release__ = '0.4.0'

library_details = {
    __version__,
    __release__,
}
