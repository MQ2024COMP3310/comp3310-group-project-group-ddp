from project import db, create_app, models
from project.models import Photo

def populate_db():
   
    session = db.session()

    photo = Photo(name = 'William Warby', caption = 'Gentoo penguin', description = 'A penguin with an orange beak standing next to a rock.', file = 'william-warby-_A_vtMMRLWM.jpg') 
    session.add(photo)
    session.commit()

    photo = Photo(name = 'Javier Patino Loira', caption = 'Common side-blotched lizard', description = 'A close up of a lizard on a rock.', file = 'javier-patino-loira-nortqDjv7ak.jpg') 
    session.add(photo)
    session.commit()

    photo = Photo(name = 'Jordie Rubies', caption = 'Griffin vulture flying', description = 'A large bird flying through a blue sky.', file = 'jordi-rubies-2wNkdL2oIyU.jpg') 
    session.add(photo)
    session.commit()

    photo = Photo(name = 'Jakub Neskora', caption = 'Jaguar', description = 'A close up of a leopard near a rock.', file = 'jakub-neskora-jloJvr74Fcc.jpg') 
    session.add(photo)
    session.commit()

    photo = Photo(name = 'William Warby', caption = 'Japanese macaque', description = 'A monkey sitting on top of a wooden post.', file = 'william-warby-ndWikw_TPfc.jpg') 
    session.add(photo)
    session.commit()

    photo = Photo(name = 'Ahmed Ali', caption = 'Berlin', description = 'An exciting part of Berlin. This place covers so many beautiful attractions in the city. From that spot you are already on the famous Oberbaumbrücke, you can see Molecule Man, and right behind me, you can see Berlin\'s beautiful skyline with the Fernsehturm right in the middle of it with the reflections of the spree.', file = 'ahmed-ali-Zl7bVVMEfg.jpg') 
    session.add(photo)
    session.commit()

    photo = Photo(name = 'Hanvin Cheong', caption = 'Nakano', description = 'A group of people walking across a street.', file = 'hanvin-cheong-9rBj8QYOL1Q.jpg') 
    session.add(photo)
    session.commit()

    photo = Photo(name = 'Ekaterina Bogdan', caption = 'Bologna', description = 'A bike parked next to a pole.', file = 'ekaterina-bogdan-BKJWsGB5h1s.jpg') 
    session.add(photo)
    session.commit()

    photo = Photo(name = 'Damian Ochrymowicz', caption = 'Nazare, Portugal', file = 'damian-ochrymowicz-GZQ7tKmEd9c.jpg') 
    session.add(photo)
    session.commit()

    photo = Photo(name = 'Dima DallAcqua', caption = 'Alcatraz Island', description = 'A close up of a green plant.', file = 'dima-dallacqua-U8TAGVPFJc4.jpg') 
    session.add(photo)
    session.commit()

    photo = Photo(name = 'Edgar', caption = 'Oporto, Portugal', description = 'A man sitting on a bench at a train station.', file = 'edgar-Q0g5Thf7Ank.jpg') 
    session.add(photo)
    session.commit()

if __name__ == '__main__':
  app = create_app()
  with app.app_context():
    db.drop_all()
    db.create_all()
    populate_db()

