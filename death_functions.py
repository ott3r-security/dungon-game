import tcod as libtcod
from render_functions import RenderOrder
from game_messages import Message
from game_states import GameStates


def kill_player(player):
    player.char = '%'
    player.color = libtcod.dark_red

    return Message('You died!', libtcod.red), GameStates.PLAYER_DEAD


def kill_monster(monster):
    death_message = Message('The {0} is dead!'.format(monster.name.capitalize()), libtcod.orange)

    monster.char = 'X'
    monster.color = libtcod.dark_red
    monster.blocks = False
    monster.fighter = None
    monster.ai = None
    monster.name = 'You see remains of ' + monster.name
    monster.render_order = RenderOrder.CORPSE

    return death_message