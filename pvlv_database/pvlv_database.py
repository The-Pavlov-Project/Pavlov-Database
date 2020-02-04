from pvlv_database.user.user import User
from pvlv_database.guild.guild import Guild


class Database(object):

    def __init__(self, guild_id, user_id):

        self.user = User(guild_id, user_id)
        self.guild = Guild(guild_id)

    def set_data(self):
        self.user.set_data()
