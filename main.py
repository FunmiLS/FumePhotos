#Running website
from fumewebsite import create_app

app = create_app()

if __name__ == '__main__': #only if we run main.py directly
    app.run(debug=True) #debug = True runs everytime we make a python change
