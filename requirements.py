import sys

def check():

    print(sys.version)

    try:
        import aiohttp 
        import jinja2
        import aiomysql

    except ImportError as e:
        print(e.__class__.__name__+ ':' + e.msg )

    #print(dir(ImportError))

    print('Check Succeeds! aiohttp, jinja2, aiomysql are all installed.')

if __name__ == '__main__':
    check()
