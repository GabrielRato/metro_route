#Here, we created a new Manager instance to handle all of the manager commands from the command line.


from flask_script import Manager

from project import app


manager = Manager(app)


if __name__ == '__main__':
        manager.run()
