from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext
import nulls_crosses
file = 'val.csv'


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')
async def new(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    nulls_crosses.new_game()
    await update.message.reply_text(f'New game!')

async def init(update: Update, context: CallbackContext):
    matrix = nulls_crosses.init_empty(file)
    await update.message.reply_text(f'Sucessfully init')
    i = 0
    str = ''
    while i < 3:
        j = 0
        while j < len(matrix[i]):
            str += matrix[i][j]
            j += 1
        str+="\n"
        i += 1
    await update.message.reply_text(str)


async def step(update: Update, context: CallbackContext):
    msg = update.message.text.split()
    x = msg[1]
    y = msg[2]
    val = msg[3]
    matrix = nulls_crosses.InitField(x, y, val)
    if matrix == "win x" or matrix == "win 0":
        await update.message.reply_text(matrix)
    else:
        i = 0
        j = 0
        str = ''
        while i < 3:
            j = 0
            while j < len(matrix[i]):
                str += matrix[i][j]
                j += 1
            i += 1
        await update.message.reply_text(str)


app = ApplicationBuilder().token(
    "TOKEN").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("init", init))
app.add_handler(CommandHandler("step", step))
app.add_handler(CommandHandler("new", new))
app.run_polling()
