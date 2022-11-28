from controller import *
from telegram import Update,ReplyKeyboardRemove,ReplyKeyboardMarkup
import telegram.ext as te
import logging
async def hello(update: Update, context: te.ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')
global fle
text  = ''
fle = open('db.csv','a',encoding='UTF-8')
#####################
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

ADD, SURNAME, NAME, SECONDNAME,BIRTH, NUMBER, COMMENT = range(7)

async def start(update: Update, context: te.ContextTypes.DEFAULT_TYPE) -> str:
    reply_keyboard = [["Ввести новую запись", "Показать все","Удалить запись", "Поиск"]]
    
    await update.message.reply_text(
        "Hi!",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Меню"
        ),
    )
    return ADD
async def add(update: Update, context: te.ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    logger.info("Пользователь %s выбрал: %s", user.first_name, update.message.text)
    await update.message.reply_text(
        "Введите фамилию",
        reply_markup=ReplyKeyboardRemove(),
    )
    return SURNAME
async def surname(update: Update, context: te.ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    global text
    logger.info("Пользователь %s ввел фамилию: %s", user.first_name, update.message.text)
    await update.message.reply_text(
        "Введите имя",
        reply_markup=ReplyKeyboardRemove(),
    )
    text +=  update.message.text+','
    return NAME

async def name(update: Update, context: te.ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    global text
    logger.info("Пользователь %s ввел фамилию: %s", user.first_name, update.message.text)
    await update.message.reply_text(
        "Введите отчество",
        reply_markup=ReplyKeyboardRemove(),
    )
    text +=  update.message.text+','
    return SECONDNAME
async def secondName(update: Update, context: te.ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    global text
    logger.info("Пользователь %s ввел отчество: %s", user.first_name, update.message.text)
    await update.message.reply_text(
        "Введите дату рождения",
        reply_markup=ReplyKeyboardRemove(),
    )
    text +=  update.message.text+','
    return BIRTH
async def birth(update: Update, context: te.ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    global text
    logger.info("Пользователь %s ввел дату: %s", user.first_name, update.message.text)
    await update.message.reply_text(
        "Введите номер телефона",
        reply_markup=ReplyKeyboardRemove(),
    )
    text +=  update.message.text+','
    return NUMBER

async def number(update: Update, context: te.ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    global text
    logger.info("Пользователь %s ввел номер: %s", user.first_name, update.message.text)
    await update.message.reply_text(
        "Введите комментарий",
        reply_markup=ReplyKeyboardRemove(),
    )
    text +=  update.message.text+','
    return COMMENT

async def comment(update: Update, context: te.ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    global text
    logger.info("Пользователь %s ввел коммент: %s", user.first_name, update.message.text)
    await update.message.reply_text(
        "Завершено",
        reply_markup=ReplyKeyboardRemove(),
    )
    text +=  update.message.text+'\n'
    fle.write(text)
    text = ''
    fle.close()
    return te.ConversationHandler.END


async def cancel(update: Update, context: te.ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    global text
    logger.info("Пользователь %s отменил ввод.", user.first_name)
    await update.message.reply_text(
        "Ввод завершен.", reply_markup=ReplyKeyboardRemove()
    )

    return te.ConversationHandler.END



def main() -> None:
    app = te.ApplicationBuilder().token(
    "TOKEN").build()
    conv_handler = te.ConversationHandler(
        entry_points=[te.CommandHandler("start", start)],
        states={
            ADD: [te.MessageHandler(te.filters.TEXT, add)],
            NAME: [te.MessageHandler(te.filters.TEXT, name)],
            SURNAME: [te.MessageHandler(te.filters.TEXT,surname)],
            SECONDNAME: [te.MessageHandler(te.filters.TEXT,secondName)],
            BIRTH: [te.MessageHandler(te.filters.TEXT,birth)],
            NUMBER: [te.MessageHandler(te.filters.TEXT,number)],
            COMMENT: [te.MessageHandler(te.filters.TEXT,comment)]
        },
        fallbacks=[te.CommandHandler("cancel", cancel)],
    )

    app.add_handler(conv_handler)
    app.run_polling()

if __name__ == "__main__":
    main()