# COMP3310 Group Project
This is the code for the Group Project (Assignment 2) for COMP3310 S1 2024.

This codebase implements a basic photo web application using python and the flask framework. Your task will be to modify the basic site to add new features focussing on secure application development principles.

# Setup

To setup the basic website you will need to have the following installed:

- python3
- pip

Pip is the package manager for Python.  You can install the remaining packages required for this task using pip. You will need to run the following:
To start you should create and activate a virtual environment:

 $ python -m venv env        # use `virtualenv env` for Python2, use `python3 ...` for Python3 on Linux & macOS   
 $ source env/bin/activate   # use `env\Scripts\activate` on Windows   
 $ pip install -r requirements.txt   

This web application has been tested on Python 3.10.13. If you have problems running this app, it is recommended that you downgrade to Python 3.10.13. Instructions on how to do this (on Mac with M1 chip) are here: https://stackoverflow.com/questions/62898911/how-to-downgrade-python-version-from-3-8-to-3-7-mac (replacing 3.7 with 3.10.13).

You will also need sqlite installed for the database backend.

# Initialising the database

You should first initialise the database as follows:
- python initialise_db.py

This should create an sqlite database under the instance directory. You can view the contents of the database using the sqlite command line interface as follows:

sqlite3 instance/photos.db   
> .schema    
CREATE TABLE photo (   
	id INTEGER NOT NULL,    
	name VARCHAR(50) NOT NULL,   
	caption VARCHAR(250) NOT NULL,   
	file VARCHAR(250) NOT NULL,   
	description VARCHAR(600),   
	PRIMARY KEY (id)  
);   

> select * from photo;  
1|William Warby|Gentoo penguin|william-warby-_A_vtMMRLWM.jpg|A penguin with an orange beak standing next to a rock.   
2|Javier Patino Loira|Common side-blotched lizard|javier-patino-loira-nortqDjv7ak.jpg|A close up of a lizard on a rock.   
3|Jordie Rubies|Griffin vulture flying|jordi-rubies-2wNkdL2oIyU.jpg|A large bird flying through a blue sky.   
4|Jakub Neskora|Jaguar|jakub-neskora-jloJvr74Fcc.jpg|A close up of a leopard near a rock.   
5|William Warby|Japanese macaque|william-warby-ndWikw_TPfc.jpg|A monkey sitting on top of a wooden post.   
6|Ahmed Ali|Berlin|ahmed-ali-Zl7bVVMEfg.jpg|An exciting part of Berlin. This place covers so many beautiful attractions in the city. From that spot you are already on the famous Oberbaumbrücke, you can see Molecule Man, and right behind me, you can see Berlin's beautiful skyline with the Fernsehturm right in the middle of it with the reflections of the spree.   
7|Hanvin Cheong|Nakano|hanvin-cheong-9rBj8QYOL1Q.jpg|A group of people walking across a street.   
8|Ekaterina Bogdan|Bologna|ekaterina-bogdan-BKJWsGB5h1s.jpg|A bike parked next to a pole.   
9|Damian Ochrymowicz|Nazare, Portugal|damian-ochrymowicz-GZQ7tKmEd9c.jpg|   
10|Dima DallAcqua|Alcatraz Island|dima-dallacqua-U8TAGVPFJc4.jpg|A close up of a green plant.   
11|Edgar|Oporto, Portugal|edgar-Q0g5Thf7Ank.jpg|A man sitting on a bench at a train station.   


# Run the website

You can run the website by typing:

- python run.py

You can now browse to the url http://localhost:8000/ to view the website.
