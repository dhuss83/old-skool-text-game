import gametools
import room

def load():
    roomPath = gametools.findGamePath(__file__)
    exists = room.check_loaded(roomPath)
    if exists: return exists
    
    living_room = room.Room('living room', pref_id=roomPath, indoor=True)
    living_room.set_description('well-kept living room', 'This is a comfortable living room, while quite small. It has a couch on one wall.')
    living_room.add_exit('west', 'home.alex.house.btr31795')
    living_room.add_exit('up', 'home.alex.house.br31795')
    living_room.add_exit('south', 'home.alex.house.mr31795')
    living_room.add_names('room', 'space')
    living_room.add_adjectives('living', 'well-kept', 'comfortable')

    bookshelf = gametools.clone('home.alex.house.bookshelf')
    bookshelf.move_to(living_room, True)

    couch = gametools.clone('home.alex.house.couch')
    couch.move_to(living_room, True)

    return living_room
