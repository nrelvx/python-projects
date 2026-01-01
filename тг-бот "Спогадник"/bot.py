from datetime import datetime
from telebot import types
import sqlite3
import telebot

bot = telebot.TeleBot("8253513379:AAFj50ZreXGLNhrucnyLKvWJ-doY5O2-150")


def init_db():
    conn = sqlite3.connect("memorybot.sql")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            text TEXT,
            created_at TEXT
        )
    """
    )
    conn.commit()
    cursor.close()
    conn.close()


init_db()


# COMMAND START
@bot.message_handler(commands=["start"])
def start(message):
    name = message.from_user.first_name
    bot.send_message(
        message.chat.id,
        f"👋 Привіт, {name}!\n\n"
        "Розкажи, що сталося з тобою сьогодні☺️\n"
        "натисни - /save",
    )


def save_memory(user_id, text):
    conn = sqlite3.connect("memorybot.sql")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO memories (user_id, text, created_at) VALUES (?, ?, ?)",
        (user_id, text, datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
    )
    conn.commit()
    cursor.close()
    conn.close()


# COMMAND SAVE
@bot.message_handler(commands=["save"])
def save_command(message):
    msg = bot.send_message(
        message.chat.id,
        "✍️ Напиши свій спогад одним повідомленням:\n"
        "(Що трапилось, що відчував, що запам'яталось)",
    )
    bot.register_next_step_handler(msg, process_save)


def process_save(message):
    user_id = message.from_user.id

    if not message.text or message.text is None:
        bot.send_message(message.chat.id, "❗ Спогад не може бути порожнім")
        return

    text = message.text.strip()

    if not text:
        bot.send_message(message.chat.id, "❗ Спогад не може бути порожнім")
        return

    save_memory(user_id, text)
    bot.send_message(message.chat.id, "✅ Спогад збережено! ✨")


# COMMAND HELP
@bot.message_handler(commands=["help"])
def help_command(message):
    help_text = (
        "📚 **Довідка по командам:**\n\n"
        "🎯 **Основні команди:**\n"
        "/start - початок роботи\n"
        "/help - ця довідка\n\n"
        "💾 **Робота з спогадами:**\n"
        "/save - зберегти новий спогад\n"
        "/random - отримати випадковий спогад\n"
        "/list - показати останні 5 спогадів\n"
        "/delete - видалити спогад\n"
        "/today - сьогоднішній спогад\n\n"
        "📝 **Як працює /save:**\n"
        "1. Натискаєш /save\n"
        "2. Пишеш свій спогад\n"
        "3. Бот зберігає його\n\n"
        "✨ Кожен спогад - це частинка твоєї історії!"
    )
    bot.send_message(message.chat.id, help_text, parse_mode="Markdown")


# COMMAND RANDOM
@bot.message_handler(commands=["random"])
def random_memory(message):
    user_id = message.from_user.id
    conn = sqlite3.connect("memorybot.sql")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT text, created_at FROM memories WHERE user_id = ? ORDER BY RANDOM() LIMIT 1",
        (user_id,),
    )

    memory = cursor.fetchone()
    cursor.close()
    conn.close()

    if memory:
        text, date = memory
        response = f"🎲 **Випадковий спогад:**\n\n💭 {text}\n\n📅 {date}"
        bot.send_message(message.chat.id, response, parse_mode="Markdown")
    else:
        response = "📭 У тебе ще немає спогадів.\nСтвори перший за допомогою /save"
        bot.send_message(message.chat.id, response)


# COMMAND LIST
@bot.message_handler(commands=["list"])
def list_memories(message):
    user_id = message.from_user.id
    conn = sqlite3.connect("memorybot.sql")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT text, created_at FROM memories WHERE user_id = ? ORDER BY created_at DESC LIMIT 5",
        (user_id,),
    )

    memories = cursor.fetchall()
    cursor.close()
    conn.close()

    if memories:
        response = "📋 **Останні спогади:**\n\n"
        for i, (text, date) in enumerate(memories, 1):
            short_text = text[:50] + "..." if len(text) > 50 else text
            response += f"{i}. {short_text}\n   📅 {date}\n\n"
    else:
        response = "📭 Список спогадів порожній.\nСтвори перший за допомогою /save"

    bot.send_message(message.chat.id, response, parse_mode="Markdown")


@bot.message_handler(commands=["delete"])
def delete_memory(message):
    user_id = message.from_user.id
    conn = sqlite3.connect("memorybot.sql")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, text FROM memories WHERE user_id = ? ORDER BY created_at DESC LIMIT 5",
        (user_id,),
    )

    memories = cursor.fetchall()
    cursor.close()
    conn.close()

    if not memories:
        bot.send_message(message.chat.id, "📭 Немає спогадів для видалення.")
        return

    markup = types.InlineKeyboardMarkup()
    for memory_id, text in memories:
        short_text = text[:30] + "..." if len(text) > 30 else text
        btn = types.InlineKeyboardButton(
            f"🗑️ {short_text}", callback_data=f"delete_memory:{memory_id}"
        )
        markup.add(btn)

    bot.send_message(
        message.chat.id,
        "🗑️ Оберіть спогад для видалення:",
        reply_markup=markup,
    )


@bot.callback_query_handler(
    func=lambda callback: callback.data.startswith("delete_memory:")
)
def delete_memory_callback(callback):
    memory_id = callback.data.replace("delete_memory:", "")

    conn = sqlite3.connect("memorybot.sql")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM memories WHERE id = ?", (memory_id,))
    conn.commit()
    cursor.close()
    conn.close()

    bot.answer_callback_query(callback.id, "✅ Спогад видалено")

    try:
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
    except:
        pass


@bot.message_handler(commands=["today"])
def today_memories(message):
    user_id = message.from_user.id
    today = datetime.now().strftime("%m-%d")

    conn = sqlite3.connect("memorybot.sql")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT text, created_at FROM memories WHERE user_id = ? AND strftime('%m-%d', created_at) = ? ORDER BY created_at DESC",
        (user_id, today),
    )

    memories = cursor.fetchall()
    cursor.close()
    conn.close()

    if memories:
        response = (
            f"📅 **Спогади на сьогодні ({datetime.now().strftime('%d.%m')}):**\n\n"
        )
        for i, (text, date) in enumerate(memories, 1):
            short_text = text[:50] + "..." if len(text) > 50 else text
            year = date.split("-")[0]
            response += f"{i}. {short_text} ({year})\n"
    else:
        response = (
            f"📅 На сьогодні ({datetime.now().strftime('%d.%m')}) спогадів ще немає."
        )

    bot.send_message(message.chat.id, response, parse_mode="Markdown")


bot.polling(none_stop=True)
