import telebot
import parsing

bot = telebot.TeleBot('1858231354:AAHRsNj24t8MjasD072F6Dn0SVZEcYsJ5b4')
heroes = [
    'abaddon',
    'alchemist',
    'ancient_apparition',
    'anti_mage',
    'arc_warden',
    'axe',
    'bane',
    'batrider',
    'beastmaster',
    'bloodseeker',
    'bounty_hunter',
    'brewmaster',
    'bristleback',
    'broodmother',
    'centaur_warrunner',
    'chaos_knight',
    'chen',
    'clinkz',
    'clockwerk',
    'crystal_maiden',
    'dark_seer',
    'dark_willow',
    'dawnbreaker',
    'dazzle',
    'death_prophet',
    'disruptor',
    'doom',
    'dragon_knight',
    'drow_ranger',
    'earth_spirit',
    'earthshaker',
    'elder_titan',
    'ember_spirit',
    'enchantress',
    'enigma',
    'faceless_void',
    'grimstroke',
    'gyrocopter',
    'hoodwink',
    'huskar',
    'invoker',
    'io',
    'jakiro',
    'juggernaut',
    'keeper_of_the_light',
    'kunkka',
    'legion_commander',
    'leshrac',
    'lich',
    'lifestealer',
    'lina',
    'lion',
    'lone_druid',
    'luna',
    'lycan',
    'magnus',
    'mars',
    'medusa',
    'meepo',
    'mirana',
    'monkey_king',
    'morphling',
    'naga_siren',
    'natures_prophet',
    'necrophos',
    'night_stalker',
    'nyx_assassin',
    'ogre_magi',
    'omniknight',
    'oracle',
    'outworld_destroyer',
    'pangolier',
    'phantom_assassin',
    'phantom_lancer',
    'phoenix',
    'puck',
    'pudge',
    'pugna',
    'queen_of_pain',
    'razor',
    'riki',
    'rubick',
    'sand_king',
    'shadow_demon',
    'shadow_fiend',
    'shadow_shaman',
    'silencer',
    'skywrath_mage',
    'slardar',
    'slark',
    'snapfire',
    'sniper',
    'spectre',
    'spirit_breaker',
    'storm_spirit',
    'sven',
    'techies',
    'templar_assassin',
    'terrorblade',
    'tidehunter',
    'timbersaw',
    'tinker',
    'tiny',
    'treant_protector',
    'troll_warlord',
    'tusk',
    'underlord',
    'undying',
    'ursa',
    'vengeful_spirit',
    'venomancer',
    'viper',
    'visage',
    'void_spirit',
    'warlock',
    'weaver',
    'windranger',
    'winter_wyvern',
    'witch_doctor',
    'wraith_king',
    'zeus']
heroes_command_str = ''


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Это бот который подбирает контрпики героям игры Dota 2\n'
                                      'Вы можете получить список героев при помощи команды /hero_list')


@bot.message_handler(commands=['hero_list'])
def start(message):
    bot.send_message(message.chat.id,
                     u'\u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u043d\u0430 \u043a\u043e\u043c\u0430\u043d\u0434\u0443 \u0441 \u0438\u043c\u0435\u043d\u0435\u043c \u0433\u0435\u0440\u043e\u044f, \u043a\u043e\u0442\u043e\u0440\u043e\u0433\u043e \u0432\u044b \u0445\u043e\u0442\u0438\u0442\u0435 \u0437\u0430\u043a\u043e\u043d\u0442\u0440\u0438\u0442\u044c\n' + heroes_command_str)


@bot.message_handler(commands=heroes)
def start(message):
    hero_name = str(message.text).replace('_', '-')
    ref = 'https://ru.dotabuff.com/heroes/' + hero_name + '/counters'
    send_counter_picks(message, ref)


def send_counter_picks(message, ref):
    for i in range(5):
        bot.send_message(message.chat.id, parsing.parse(ref, i))


def make_hero_list_str(heroes):
    string = ''
    for hero in heroes:
        string += '/' + str(hero) + '\n'
    else:
        return string


heroes_command_str = make_hero_list_str(heroes)
