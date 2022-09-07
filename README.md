if u want to use enironment varibale to set the color then in the python file do changes and while creating container u have to give the environment varibale
after containersing the app.py , while we are creating a contaienr out of it we need to give the value for environment variable APP_COLOR
ex: $docker run -e APP_COLOR = red  <image name> 
  $ dokcer run -e APP_COLR = green  <image name>
