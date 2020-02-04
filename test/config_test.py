from datetime import datetime

from pvlv_database import Database


def creation_test():
    db = Database(123456789, 123456789)  # guild_id, user_id
    db.set_data()


def user_test():
    db = Database(123456789, 123456789)  # guild_id, user_id

    # test command
    db.user.guild.commands.increment_command_interactions('command_1', datetime.now())
    db.user.guild.commands.increment_command_interactions('command_2', datetime.now())

    # test message_logs
    db.user.guild.msg.update_msg_log((datetime.now(), 1, 10))
    db.user.guild.msg.update_img_log((datetime.now(), 1, 6))
    db.user.guild.msg.update_vocals_log((datetime.now(), 1, 6))
    db.user.guild.msg.update_links_log((datetime.now(), 1, 6))
    db.user.guild.msg.update_swear_words_log((datetime.now(), 1, 6))

    # test xp_logs
    db.user.guild.xp.xp_value += 8

    # test bits_logs
    db.user.guild.bill.bits += 2

    db.set_data()


def main():
    try:
        creation_test()
        print('database creation test PASS')
    except Exception as exc:
        print(exc)
        print('DATABASE CREATION TEST FAILED')

    try:
        user_test()
        print('user data edit test PASS')
    except Exception as exc:
        print(exc)
        print('USER DATA EDIT TEST FAILED')


if __name__ == '__main__':
    main()




