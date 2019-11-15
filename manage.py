from news_app import create_app
from flask_script import Manager,Server

NB=create_app('development')

manager=Manager(NB)
manager.add_command('server',Server)

if __name__=='__main__':
  manager.run()