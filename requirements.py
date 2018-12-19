import sys

def check():

    print(sys.version)

    try:
        import aiohttp 
        import jinja2
        import aiomysql

        print('Check Succeeds! aiohttp, jinja2, aiomysql are all installed.')
    except ImportError as e:
        print(e.__class__.__name__+ ':' + e.msg )

    #print(dir(ImportError))

if __name__ == '__main__':
    check()
