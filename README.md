# hexagonal-template
Just a model of my design of what is a hexagonal architecture, built in python 
using tree adapters, one input two outputs 
fastApi as input and sqlAlchemy as output for the bdd and InMemory as output for tests and mock data.

i'm just an student so if  u see this project be indulgent whit my code 🤕

if u want to start this Api 

clone the code here (ssh) 

```bash
git@github.com:Baptiste-Ferrand/hexagonal-template.git
```

Now u can use uv sync for install the dependency in an venv 

```bash
uv sync
```

Now enter in you venv whit this command (linux)

```bash
source venv/bin/activate
```

If you are in windows... wait why you are in windows? you like to make things difficult for yourself, so look for yourself!

Now u can start the project whit this command 
```bash
uvicorn src.main:app --reload --host 127.0.0.1 --port 8000
```

U want to exit the venv and touch the grass (linux)
```bash
deactivate
```

And if those commands don't work... maybe try google it, and that's what the Internet is for 🤨.

Now, enjoy and take a deep breath because my code is 🤢


