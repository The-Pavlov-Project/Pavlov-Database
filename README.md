# Pavlov Database
A database connector to speed up the develop of chat bots.
It use mongo Database, you can host an instance locally or use the free mondo Atlas service.

## Configuration of the package
Create the folder '/configs' in the root of the project,
inside the folder add a file named database.cgf

obligatory params:
- MONGO_CONNECTION_STRING: connection string to the remote db,
must be manually created, see mongo documentation
- DATABASE_NAME: name of database
- USERS_TABLE_NAME: name of the table where save users obj
- GUILDS_TABLE_NAME: name of the table where save guild obj
```
[connection]
MONGO_CONNECTION_STRING = mongodb+srv://<username>:<pwsd>@<connection>.mongodb.net/test?retryWrites=true

[database]
DATABASE_NAME = test
USERS_TABLE_NAME = users
GUILDS_TABLE_NAME = guilds

[debug]
DEBUG = True

[cache]
DB_SAVE_INTERVAL = 600  # time in seconds
MAX_CACHE_ITEMS = 100  # max items saved per type, this will use ram

[values]
# Max data log retention, after the time specified the data for the stats will be deleted
# Don't keep an high retention on high granularitis cause il will slow down a lot
MAX_RETENTION_HOUR = 72  # user logs by hour, after 72 hours the data with that eta will be deleted
MAX_RETENTION_DAY = 90
MAX_RETENTION_MONTH = 120

# Time spent calculation config
# This mean that in 11 seconds you ca write a message 30 chars long.
# Others values are calculated with proprortion (there is an anti spam meccanism)
SAMPLE_STRING_LEN = 30
TIME_SAMPLE_VALUE = 11

# XP gain calculation config
# This mean that you can gain 12 in a normal message (logaritmic gain)
# 15 at max (anti spam meccanism). 
# If you send 1 char message you'll gain at least 1 xp
XP_SAMPLE_VALUE = 12
XP_MAX_VALUE = 15
XP_NEXT_LEVEL = 300  # each new level have 300 xp more than his predecessor.

Same as for XP
BITS_SAMPLE_VALUE = 5
BITS_MAX_VALUE = 2
```

## Base Usage
This is an example of use. 
Do not care about efficiency!

You don't have to call once and pass the db object cause is cached internally 
so it will not generate a new call to the remote db.
```python
from pvlv_database import Database

# It will automatically sync the local cache with the remote DB
guild_id = 123456789
user_id = 123456789
db = Database(guild_id, user_id)

db.user.username = 'User'
print(db.user.username)

# use this only if really needed, the db have an auto-saving demon, change the interval in the cfg file
# This can be called for example at the exit of the program, to manually sync un-synced data.
db.force_set_data() 
```
## Usage, Updaters
To easily update the user stats all in one.
 - xp
 - time spent
 - bits
 - username
 - chat name 
```python
from pvlv_database import Database
from pvlv_database import BaseStatsUpdater

guild_id = 123456789
user_id = 123456789
db = Database(guild_id, user_id)


bsu = BaseStatsUpdater(db, timestamp)
bsu.text(message_text)
bsu.username(username)
bsu.guild_name(guild_name)
bsu.update_text()
```
## Efficiency
Let's suppose that you have to interrogate multiple times the db in different modules of the code.
Test this code by yourself.
```python
from time import time
from pvlv_database import Database

guild_id = 123456789
user_id = 123456789

t1 = time()
db = Database(guild_id, user_id)  # first call 800/2000 ms (on MongoDB Atlas cloud)
t2 = time()
t = (t2 - t1) * 1000
print('Execution time {} ms'.format(int(t)))

# other calls in different modules
t1 = time()
db_1 = Database(guild_id, user_id)  # 1 ms
db_2 = Database(guild_id, user_id)  # 1 ms
t2 = time()
t = (t2 - t1) * 1000
print('Execution time {} ms'.format(int(t)))
```
The saving demon in on another thread. So il will not affect the program speed.
It's not thread safe.