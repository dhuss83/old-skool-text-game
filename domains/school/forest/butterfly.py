import creature
import thing

def clone():
    butterfly = creature.NPC('butterfly', __file__, thing.Thing.ID_dict['nulspace'].game)
    butterfly.set_description('butterfly', 'A pretty monarch butterfly')
    butterfly.add_script("""wh""")
    return butterfly