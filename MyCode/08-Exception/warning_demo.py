from warnings import filterwarnings, warn

filterwarnings("ignore")
warn("This is a warning message")
filterwarnings("error")
warn("This is a second warning message")
filterwarnings("default")
warn("This is a third warning message")
