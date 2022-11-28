from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext
import model_div
import model_logger
import model_minus
import model_mult
import model_sum
file = 'val.csv'


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')
async def calc_simple(update: Update, context: CallbackContext):
    msg = update.message.text.split()
    result = ''
    if msg[2] == "+":
        result = model_sum.do_it(float(msg[1]),float(msg[3]))
    elif msg[2] == '*':
        result = model_mult.do_it(float(msg[1]),float(msg[3]))
    elif msg[2] == '-':
        result = model_minus.do_it(float(msg[1]),float(msg[3]))
    elif msg[2] == '/':
        result = model_div.do_it(float(msg[1]),float(msg[3]))
    model_logger.Logger(msg[1],msg[3],msg[2],result)
    await update.message.reply_text(str(result))

async def calc_complex(update: Update, context: CallbackContext):
    msg = update.message.text.split()
    result = ''
    if msg[2] == "+":
        result = model_sum.do_it(complex(msg[1]),complex(msg[3]))
    elif msg[2] == '*':
        result = model_mult.do_it(complex(msg[1]),complex(msg[3]))
    elif msg[2] == '-':
        result = model_minus.do_it(complex(msg[1]),complex(msg[3]))
    elif msg[2] == '/':
        result = model_div.do_it(complex(msg[1]),complex(msg[3]))
    model_logger.Logger(msg[1],msg[3],msg[2],result)
    await update.message.reply_text(str(result))

app = ApplicationBuilder().token(
    "TOKEN").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("simple", calc_simple))
app.add_handler(CommandHandler("complex", calc_complex))

app.run_polling()
