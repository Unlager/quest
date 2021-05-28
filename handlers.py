from main import bot, dp
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from config import admin_id
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, Command
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
import loader
from text_quest import *
import time
from work_base import *

group_flag = 0
mychatFlag = 'str'
timesTimeSec = 5
timePeredZad = 4


class Quest(StatesGroup):
    Q0 = State()
    Q1 = State()
    Q1_1 = State()
    Q1_2 = State()
    Q1_3 = State()
    Q1_4 = State()
    Q1_5 = State()
    Q1_6 = State()
    Q1_7 = State()
    Q1_8 = State()
    Q1_9 = State()
    Q1_10 = State()
    Q2 = State()
    Q2_1 = State()
    Q2_2 = State()
    Q2_3 = State()
    Q2_4 = State()
    Q2_5 = State()
    Q2_6 = State()
    Q2_7 = State()
    Q2_8 = State()
    Q2_9 = State()
    Q3 = State()
    Q3_1 = State()
    Q3_2 = State()
    Q3_3 = State()
    Q3_4 = State()
    Q3_5 = State()
    Q3_6 = State()
    Q3_7 = State()
    Q3_8 = State()
    Q3_9 = State()
    Q3_10 = State()
    Q4 = State()
    Q4_fail = State()
    Q5 = State()
    Q5_1 = State()
    Q5_2 = State()
    Q5_3 = State()
    Q5_4 = State()
    Q5_5 = State()
    Q5_6 = State()
    Q5_7 = State()
    Q5_8 = State()
    Q5_9 = State()
    Q5_10 = State()
    Q5_11 = State()
    Q6 = State()

async def send_to_admin(*args):
    await bot.send_message(chat_id=admin_id, text="Бот запущен", reply_markup=menu)

@dp.message_handler(Text(equals=["Управление", "Пользователи", "Логи", "Очистить"]))
async def admin_control(message: types.Message):
    if message.from_user.id == admin_id:
        if message.text != "Очистить" and message.text != "Пользователи": await message.answer(f"Вы выбрали {message.text}.")
        elif message.text == "Пользователи":
            text_from_takeFromBase = ''
            for i in workWithBase.takeFromBase(): text_from_takeFromBase = text_from_takeFromBase + str(i) + '\n'
            await message.answer(text=str(text_from_takeFromBase))
        else: await message.answer("Панель очищена", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(commands=['admin'], state=None)
async def admin_enter(message: types.Message):
    if message.from_user.id == admin_id: await message.answer("Админ панель", reply_markup=menu)
    else: await message.answer("Тибе низя :(")

@dp.message_handler(commands=['start'], state=None)
async def enter_test(message: types.Message):
    await message.answer("Добро пожаловать! Это квест бот, для начала нажмите кнопку", reply_markup=menuQuest)
    workWithBase.addToBase(str(message.from_user.id), str(message.from_user.username))

@dp.message_handler(Text(equals=["Начать квест"]), state=None)
async def start_q(message: types.Message):
    await message.answer(text=startQuest_1, reply_markup=ReplyKeyboardRemove())
    time.sleep(25)
    with open('images/doky.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption=startQuest_2)
    time.sleep(16)
    await message.answer(text="Задание 1: расшифруй послание своего деда.")
    morze
    await message.answer(text="Фраза зашифрованная азбукой морзе:\n" + str(morze))
    await Quest.Q0.set()

@dp.message_handler(commands=['quest123'], state=None)
async def enter_test(message: types.Message):
    await message.answer(text=startQuest_1, reply_markup=ReplyKeyboardRemove())
    time.sleep(timesTimeSec)
    with open('images/doky.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption=startQuest_2)
    time.sleep(timePeredZad)
    await message.answer(text="Задание 1: расшифруй послание своего деда.", reply_markup=nextReplica)
    await Quest.Q0.set()

@dp.message_handler(commands=['correction'])
async def enter_test(message: types.Message):
    await message.answer(text="Редактирование", reply_markup=nextReplica)
    await Quest.Q0.set()

@dp.message_handler(state=Quest.Q0)
async def answer_q0(message: types.Message, state: FSMContext):
    arrayForFirst = ['НАШЕДЕЛОПРАВОЕ—МЫПОБЕДИЛИ','Наше дело правое мы победили','Наше дело правое - мы победили','Наше дело правое мы победили!','наше дело правое - мы победили','Наше дело правое - мы победили!','наше дело правое - мы победили!','нашеделоправое-мыпобедили','Нашеделоправое-мыпобедили','нашеделоправое-мыпобедили!','Нашеделоправое-мыпобедили!','НАШЕДЕЛОПРАВОЕ-МЫПОБЕДИЛИ','НАШЕДЕЛОПРАВОЕ МЫПОБЕДИЛИ','НАШЕДЕЛОПРАВОЕМЫПОБЕДИЛИ',"Нашеделоправоемыпобедили","нашеделоправоемыпобедили", "наше дело правое мы победили"]
    answerTrue = True
    for i in arrayForFirst:
        if message.text == str(i):
            answerTrue = False
    if answerTrue:
        await message.answer(text="Где-то ошибка!")
        await Quest.Q0.set()
    else:
        await message.answer(text=after_first_mission)
        time.sleep(22)
        with open('images/warehouse.jpg', 'rb') as photo:
            await message.reply_photo(photo, caption=after_first_mission1)
        time.sleep(16)
        with open('images/bread.jpg', 'rb') as photo:
            await message.reply_photo(photo, caption="Задание 2: реши задачу, чтобы помочь пекарям.")
        time.sleep(1)
        await message.answer(text="При выпечке хлеба из килограмма ржаной муки пекарь получает 1,4 кг хлеба, сколько киллограммов муки расходуется на выпечку 21 ц хлеба?")
        await Quest.Q1.set()

@dp.message_handler(state=Quest.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    if message.text != '1500':
        await message.answer(text="Нет, нет, нет!")
        await Quest.Q1.set()
    else:
        await message.answer(text=after_second_mission, reply_markup=ReplyKeyboardRemove())
        time.sleep(7)
        await message.answer(text=after_second_mission1)
        time.sleep(15)
        with open('images/cars.jpg', 'rb') as photo:
            await message.reply_photo(photo, caption=after_second_mission2)
        time.sleep(14)
        with open('images/mina.jpg', 'rb') as photo:
            await message.reply_photo(photo, caption="Задание 3: помоги водителю с дорогой и обнаружь все мины.\n Доберись с первой клетки до двенадцатой.", reply_markup=mina_place)
        await Quest.Q1_2.set()

@dp.message_handler(state=Quest.Q1_1)
async def answer_q1_1(message: types.Message, state: FSMContext):
    with open('images/mina.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption="Задание 3: помоги водителю с дорогой и обнаружь все мины.\n Доберись с первой клетки до двенадцатой.", reply_markup=mina_place)
    await Quest.next()

@dp.message_handler(state=Quest.Q1_2)
async def answer_q1_2(message: types.Message, state: FSMContext):
    if message.text != '1':
        await message.answer(text="БАХ!", reply_markup=nextReplica)
        await Quest.Q1_1.set()
    else:
        await message.answer(text="Мины нет...")
        await Quest.next()

@dp.message_handler(state=Quest.Q1_3)
async def answer_q1_3(message: types.Message, state: FSMContext):
    if message.text != '2':
        await message.answer(text="БАХ!", reply_markup=nextReplica)
        await Quest.Q1_1.set()
    else:
        await message.answer(text="Мины нет...")
        await Quest.next()

@dp.message_handler(state=Quest.Q1_4)
async def answer_q1_4(message: types.Message, state: FSMContext):
    if message.text != '4':
        await message.answer(text="БАХ!", reply_markup=nextReplica)
        await Quest.Q1_1.set()
    else:
        await message.answer(text="Мины нет...")
        await Quest.next()

@dp.message_handler(state=Quest.Q1_5)
async def answer_q1_5(message: types.Message, state: FSMContext):
    if message.text != '6':
        await message.answer(text="БАХ!", reply_markup=nextReplica)
        await Quest.Q1_1.set()
    else:
        await message.answer(text="Мины нет...")
        await Quest.next()

@dp.message_handler(state=Quest.Q1_6)
async def answer_q1_6(message: types.Message, state: FSMContext):
    if message.text != '8':
        await message.answer(text="БАХ!", reply_markup=nextReplica)
        await Quest.Q1_1.set()
    else:
        await message.answer(text="Мины нет...")
        await Quest.next()

@dp.message_handler(state=Quest.Q1_7)
async def answer_q1_7(message: types.Message, state: FSMContext):
    if message.text != '7':
        await message.answer(text="БАХ!", reply_markup=nextReplica)
        await Quest.Q1_1.set()
    else:
        await message.answer(text="Мины нет...")
        await Quest.next()

@dp.message_handler(state=Quest.Q1_8)
async def answer_q1_8(message: types.Message, state: FSMContext):
    if message.text != '9':
        await message.answer(text="БАХ!", reply_markup=nextReplica)
        await Quest.Q1_1.set()
    else:
        await message.answer(text="Мины нет...")
        await Quest.next()

@dp.message_handler(state=Quest.Q1_9)
async def answer_q1_9(message: types.Message, state: FSMContext):
    if message.text != '11':
        await message.answer(text="БАХ!", reply_markup=nextReplica)
        await Quest.Q1_1.set()
    else:
        await message.answer(text="Мины нет...")
        await Quest.next()

@dp.message_handler(state=Quest.Q1_10)
async def answer_q1_10(message: types.Message, state: FSMContext):
    if message.text != '12':
        await message.answer(text="БАХ!", reply_markup=nextReplica)
        await Quest.Q1_1.set()
    else:
        await message.answer(text="...", reply_markup=nextReplica)
        await Quest.next()

@dp.message_handler(state=Quest.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    await message.answer(text=after_third_mission, reply_markup=ReplyKeyboardRemove())
    time.sleep(13)
    await message.answer(text=after_third_mission1)
    with open('images/music.jpg', 'rb') as photo:
        await message.reply_photo(photo)
    time.sleep(22)
    await message.answer(text="Задание 4: вспомни знаменитые военные песни по мелодии, пока едешь к следующему пункту.")
    with open('songs/audio1.mp3', 'rb') as audio:
        await message.answer_audio(audio=audio, reply_markup=song_1)
    await Quest.next()

@dp.message_handler(state=Quest.Q2_1)
async def answer_q3_2(message: types.Message, state: FSMContext):
    if message.text != 'День победы':
        await message.answer(text="Неправильно")
        await Quest.Q2_1.set()
    else:
        with open('songs/audio2.mp3', 'rb') as audio:
            await message.answer_audio(audio=audio, reply_markup=song_2)
        await Quest.next()

@dp.message_handler(state=Quest.Q2_2)
async def answer_q3_2(message: types.Message, state: FSMContext):
    if message.text != 'Прощание славянки':
        await message.answer(text="Неправильно")
        await Quest.Q2_2.set()
    else:
        with open('songs/audio3.mp3', 'rb') as audio:
            await message.answer_audio(audio=audio, reply_markup=song_3)
        await Quest.next()

@dp.message_handler(state=Quest.Q2_3)
async def answer_q3_2(message: types.Message, state: FSMContext):
    if message.text != 'Катюша':
        await message.answer(text="Неправильно")
        await Quest.Q2_3.set()
    else:
        with open('songs/audio4.mp3', 'rb') as audio:
            await message.answer_audio(audio=audio, reply_markup=song_4)
        await Quest.next()

@dp.message_handler(state=Quest.Q2_4)
async def answer_q3_2(message: types.Message, state: FSMContext):
    if message.text != 'Журавли':
        await message.answer(text="Неправильно")
        await Quest.Q2_4.set()
    else:
        with open('songs/audio5.mp3', 'rb') as audio:
            await message.answer_audio(audio=audio, reply_markup=song_5)
        await Quest.next()

@dp.message_handler(state=Quest.Q2_5)
async def answer_q3_2(message: types.Message, state: FSMContext):
    if message.text != 'Три танкиста':
        await message.answer(text="Неправильно")
        await Quest.Q2_5.set()
    else:
        with open('songs/audio6.mp3', 'rb') as audio:
            await message.answer_audio(audio=audio, reply_markup=song_6)
        await Quest.next()

@dp.message_handler(state=Quest.Q2_6)
async def answer_q3_2(message: types.Message, state: FSMContext):
    if message.text != 'Священная война':
        await message.answer(text="Неправильно")
        await Quest.Q2_6.set()
    else:
        with open('songs/audio7.mp3', 'rb') as audio:
            await message.answer_audio(audio=audio, reply_markup=song_7)
        await Quest.next()

@dp.message_handler(state=Quest.Q2_7)
async def answer_q3_2(message: types.Message, state: FSMContext):
    if message.text != 'Красная армия всех сильней':
        await message.answer(text="Неправильно")
        await Quest.Q2_7.set()
    else:
        with open('songs/audio8.mp3', 'rb') as audio:
            await message.answer_audio(audio=audio, reply_markup=song_8)
        await Quest.next()

@dp.message_handler(state=Quest.Q2_8)
async def answer_q3_2(message: types.Message, state: FSMContext):
    if message.text != 'Смуглянка':
        await message.answer(text="Неправильно")
        await Quest.Q2_8.set()
    else:
        with open('songs/audio9.mp3', 'rb') as audio:
            await message.answer_audio(audio=audio, reply_markup=song_9)
        await Quest.next()

@dp.message_handler(state=Quest.Q2_9)
async def answer_q3_2(message: types.Message, state: FSMContext):
    if message.text != 'Марш преображенского полка':
        await message.answer(text="Неправильно")
        await Quest.Q2_9.set()
    else:
        await message.answer(text="Правильно!", reply_markup=nextReplica)
        await Quest.next()

@dp.message_handler(state=Quest.Q3)
async def answer_q3(message: types.Message, state: FSMContext):
    await message.answer(text=after_fourth_mission, reply_markup=ReplyKeyboardRemove())
    time.sleep(26)
    with open('images/wear.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption=after_fourth_mission1)
    time.sleep(20)
    await message.answer(text="Задание 5: тебе выдали снаряжение. Используя осязание, пойми, что ты держишь.")
    time.sleep(1)
    await message.answer(text="1)", reply_markup=question1_weapon)
    await Quest.Q3_2.set()

@dp.message_handler(state=Quest.Q3_1)
async def answer_q3_1(message: types.Message, state: FSMContext):
    with open('images/wear.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption="Задание 5: тебе выдали снаряжение. Используя осязание, пойми, что ты держишь.")
    time.sleep(1)
    await message.answer(text="1)", reply_markup=question1_weapon)
    await Quest.next()

@dp.message_handler(state=Quest.Q3_2)
async def answer_q3_2(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer1=answer)
    await message.answer(text="2)", reply_markup=question2_weapon)
    await Quest.next()

@dp.message_handler(state=Quest.Q3_3)
async def answer_q3_3(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer2=answer)
    await message.answer(text="3)", reply_markup=question3_weapon)
    await Quest.next()

@dp.message_handler(state=Quest.Q3_4)
async def answer_q3_4(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer3=answer)
    await message.answer(text="4)", reply_markup=question4_weapon)
    await Quest.next()

@dp.message_handler(state=Quest.Q3_5)
async def answer_q3_5(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer4=answer)
    await message.answer(text="5)", reply_markup=question5_weapon)
    await Quest.next()

@dp.message_handler(state=Quest.Q3_6)
async def answer_q3_6(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer5=answer)
    await message.answer(text="6)", reply_markup=question6_weapon)
    await Quest.next()

@dp.message_handler(state=Quest.Q3_7)
async def answer_q3_7(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer6=answer)
    await message.answer(text="7)", reply_markup=question7_weapon)
    await Quest.next()

@dp.message_handler(state=Quest.Q3_8)
async def answer_q3_8(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer7=answer)
    await message.answer(text="8)", reply_markup=question8_weapon)
    await Quest.next()

@dp.message_handler(state=Quest.Q3_9)
async def answer_q3_9(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer8=answer)
    await message.answer(text="9)", reply_markup=question9_weapon)
    await Quest.next()

@dp.message_handler(state=Quest.Q3_10)
async def answer_q3_10(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer9=answer)
    data = await state.get_data()
    array = []
    array_ans = ["Шапка-ушанка","Шинельное пальто","Валенки","Пояс","7,62-мм винтовка Токарева СВТ-40","Штык-нож","Патронные сумки","Сумка для противогаза","Саперная лопата"]
    for i in range(1, 10):
        array.append(data.get("answer" + str(i)))
    if array == array_ans:
        await message.answer(text="Проверим...", reply_markup=nextReplica)
        await Quest.next()
    else:
        await message.answer(text="-Опа, что-то ты взял не то. Проверь еще раз весь список и найди ошибку. Попробуй снова.", reply_markup=nextReplica)
        await Quest.Q3_1.set()


@dp.message_handler(state=Quest.Q4)
async def answer_q4(message: types.Message, state: FSMContext):
    await message.answer(text=after_fifth_mission, reply_markup=ReplyKeyboardRemove())
    time.sleep(18)
    with open('images/okopy.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption=after_fifth_mission1)
    time.sleep(12)
    await message.answer(text="Задание 6: доберись по окопам к союзным казармам.")
    time.sleep(1)
    with open('images/maze.png', 'rb') as photo:
        await message.reply_photo(photo, caption="Надо ввести без пробелов цифры находящиеся на пути к выходу из лабиринта.")
    await Quest.Q5.set()


@dp.message_handler(state=Quest.Q5)
async def answer_q5(message: types.Message, state: FSMContext):
    if message.text != '259101314162110154':
        await message.answer(text="Ах! Тупик! Надо свернуть в другую сторону.")
        await Quest.Q5.set()
    else:
        await message.answer(text=after_sixth_mission, reply_markup=ReplyKeyboardRemove())
        time.sleep(4)
        await message.answer(text=after_sixth_mission1)
        with open('images/table.jpg', 'rb') as photo:
            await message.reply_photo(photo)
        time.sleep(20)
        await message.answer(text=after_sixth_mission2)
        time.sleep(19)
        await message.answer(text="Задание 7: пойми о каких событиях говорят фронтовики и поддержи разговор.")
        time.sleep(2)
        await message.answer(text=questions_one, reply_markup=question1_answers)
        await Quest.Q5_2.set()

@dp.message_handler(state=Quest.Q5_1)
async def answer_q5_1(message: types.Message, state: FSMContext):
    await message.answer(text="Задание 7: пойми о каких событиях говорят фронтовики и поддержи разговор.", reply_markup=ReplyKeyboardRemove())
    time.sleep(1)
    await message.answer(text=questions_one, reply_markup=question1_answers)
    await Quest.next()

@dp.message_handler(state=Quest.Q5_2)
async def answer_q5_2(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer1=answer)
    await message.answer(text=questions_two, reply_markup=question2_answers)
    await Quest.next()

@dp.message_handler(state=Quest.Q5_3)
async def answer_q5_3(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer2=answer)
    await message.answer(text=questions_three, reply_markup=question3_answers)
    await Quest.next()

@dp.message_handler(state=Quest.Q5_4)
async def answer_q5_4(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer3=answer)
    await message.answer(text=questions_four, reply_markup=question4_answers)
    await Quest.next()

@dp.message_handler(state=Quest.Q5_5)
async def answer_q5_5(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer4=answer)
    await message.answer(text=questions_five, reply_markup=question5_answers)
    await Quest.next()

@dp.message_handler(state=Quest.Q5_6)
async def answer_q5_6(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer5=answer)
    await message.answer(text=questions_six, reply_markup=question6_answers)
    await Quest.next()

@dp.message_handler(state=Quest.Q5_7)
async def answer_q5_7(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer6=answer)
    await message.answer(text=questions_seven, reply_markup=question7_answers)
    await Quest.next()

@dp.message_handler(state=Quest.Q5_8)
async def answer_q5_8(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer7=answer)
    await message.answer(text=questions_eight, reply_markup=question8_answers)
    await Quest.next()

@dp.message_handler(state=Quest.Q5_9)
async def answer_q5_9(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer8=answer)
    await message.answer(text=questions_nine, reply_markup=question9_answers)
    await Quest.next()

@dp.message_handler(state=Quest.Q5_10)
async def answer_q5_10(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer9=answer)
    await message.answer(text=questions_ten, reply_markup=question10_answers)
    await Quest.next()

@dp.message_handler(state=Quest.Q5_11)
async def answer_q5_11(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer10=answer)
    data = await state.get_data()
    array = []
    array_ans = ["22 июня 1941","Рихард Зорге","Вячеслав Молотов","Брестская","Ленинградская","Московская","Иосиф Сталин","Зоя Космодемьянская","Ладожское озеро","Британия, США"]
    for i in range(1, 11):
        array.append(data.get("answer" + str(i)))
    if array == array_ans:
        await message.answer(text="Хм...", reply_markup=nextReplica)
        await Quest.next()
    else:
        await message.answer(text="-Что-то не так... Давай ещё раз. Будь внимательнее!", reply_markup=nextReplica)
        await Quest.Q5_1.set()


@dp.message_handler(state=Quest.Q6)
async def answer_q6(message: types.Message, state: FSMContext):
    workWithBase.update_base(str(message.from_user.id))
    await message.answer(text=after_seventh_mission, reply_markup=ReplyKeyboardRemove())
    time.sleep(5)
    await message.answer(text=after_seventh_mission1)
    time.sleep(23)
    with open('images/smile.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption=after_seventh_mission2)
    time.sleep(25)
    await message.answer(text=after_seventh_mission3)
    time.sleep(3)
    with open('images/end.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption=end_game, reply_markup=startButton)

    await state.reset_state(with_data=False)

@dp.message_handler(commands=['cor1'])
async def enter_test(message: types.Message):
    await message.answer(text="Редактирование", reply_markup=cor1)
    await Quest.Q0.set()

cor1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="НАШЕДЕЛОПРАВОЕ—МЫПОБЕДИЛИ")
        ],
    ],
    resize_keyboard=True
)

@dp.message_handler(commands=['cor2'])
async def enter_test(message: types.Message):
    await message.answer(text="Редактирование", reply_markup=cor2)
    await Quest.Q1.set()

cor2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1500")
        ],
    ],
    resize_keyboard=True
)

@dp.message_handler(commands=['cor3'])
async def enter_test(message: types.Message):
    await message.answer(text="Редактирование", reply_markup=nextReplica)
    await Quest.Q2.set()

cor3 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="НАШЕДЕЛОПРАВОЕ—МЫПОБЕДИЛИ")
        ],
    ],
    resize_keyboard=True
)
@dp.message_handler(commands=['cor4'])
async def enter_test(message: types.Message):
    await message.answer(text="Редактирование", reply_markup=nextReplica)
    await Quest.Q3.set()

@dp.message_handler(commands=['cor5'])
async def enter_test(message: types.Message):
    await message.answer(text="Редактирование", reply_markup=nextReplica)
    await Quest.Q4.set()

@dp.message_handler(commands=['cor6'])
async def enter_test(message: types.Message):
    await message.answer(text="Редактирование", reply_markup=cor6)
    await Quest.Q5.set()
cor6 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="259101314162110154")
        ],
    ],
    resize_keyboard=True
)
@dp.message_handler(commands=['cor7'])
async def enter_test(message: types.Message):
    await message.answer(text="Редактирование", reply_markup=nextReplica)
    await Quest.Q6.set()

@dp.message_handler(regexp='(^кот[ы]?$|котейка|котя|киса)')
async def cats(message: Message):
    with open('images/cats.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Котя тут 😺')

@dp.message_handler(regexp='(^бля[ть]?$|блядь)')
async def cats(message: Message):
    await message.answer(text="Бот зарегестрировал ненормативную лексику! Просьба прекратить.")
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Управление"),
            KeyboardButton(text="Очистить"),
        ],
        [
            KeyboardButton(text="Пользователи"),
            KeyboardButton(text="Логи"),
        ],
        [
            KeyboardButton(text="/start"),
            KeyboardButton(text="/correction")
        ],
    ],
    resize_keyboard=True
)

menuQuest = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Начать квест")
        ],
    ],
    resize_keyboard=True
)

nextReplica = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Продолжить")
        ],
    ],
    resize_keyboard=True
)
startButton = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="/start")
        ],
    ],
    resize_keyboard=True
)

question1_answers = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1 сентября 1939"),
            KeyboardButton(text="10 мая 1940"),
        ],
        [
            KeyboardButton(text="22 июня 1941"),
            KeyboardButton(text="7 ноября 1941")
        ],
    ],
    resize_keyboard=True
)
question2_answers = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Лаврентий Берия"),
            KeyboardButton(text="Рихард Зорге"),
        ],
        [
            KeyboardButton(text="Юлиус Розенберг"),
            KeyboardButton(text="Рудольф Абель")
        ],
    ],
    resize_keyboard=True
)
question3_answers = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Вячеслав Молотов"),
            KeyboardButton(text="Анастас Микоян"),
        ],
        [
            KeyboardButton(text="Никита Хрущев"),
            KeyboardButton(text="Георгий Маленков")
        ],
    ],
    resize_keyboard=True
)
question4_answers = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Брестская"),
            KeyboardButton(text="Могилевская"),
        ],
        [
            KeyboardButton(text="Бобруйская"),
            KeyboardButton(text="Гродненская")
        ],
    ],
    resize_keyboard=True
)
question5_answers = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ленинградская"),
            KeyboardButton(text="Московская"),
        ],
        [
            KeyboardButton(text="Сталинградская"),
            KeyboardButton(text="Брестская")
        ],
    ],
    resize_keyboard=True
)
question6_answers = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Смоленская"),
            KeyboardButton(text="Сталинградская"),
        ],
        [
            KeyboardButton(text="Московская"),
            KeyboardButton(text="Курская")
        ],
    ],
    resize_keyboard=True
)
question7_answers = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Владимир Ленин"),
            KeyboardButton(text="Георгий Жуков"),
        ],
        [
            KeyboardButton(text="Иосиф Сталин"),
            KeyboardButton(text="Никита Хрущев")
        ],
    ],
    resize_keyboard=True
)
question8_answers = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Зина Портнова"),
            KeyboardButton(text="Любовь Шевцова"),
        ],
        [
            KeyboardButton(text="Ульяна Громова"),
            KeyboardButton(text="Зоя Космодемьянская")
        ],
    ],
    resize_keyboard=True
)
question9_answers = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Невское озеро"),
            KeyboardButton(text="Финский залив"),
        ],
        [
            KeyboardButton(text="Онежское озеро"),
            KeyboardButton(text="Ладожское озеро")
        ],
    ],
    resize_keyboard=True
)
question10_answers = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Франция, Испания"),
            KeyboardButton(text="Британия, США"),
        ],
        [
            KeyboardButton(text="Италия, Япония"),
            KeyboardButton(text="Финляндия, Швеция")
        ],
    ],
    resize_keyboard=True
)

question1_weapon = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Шапка"),
            KeyboardButton(text="Балаклава"),
        ],
        [
            KeyboardButton(text="Шапка-ушанка"),
            KeyboardButton(text="Каска")
        ],
    ],
    resize_keyboard=True
)
question2_weapon = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Шинельное пальто"),
            KeyboardButton(text="Китель"),
        ],
        [
            KeyboardButton(text="Пиджак"),
            KeyboardButton(text="Гимнастёрка")
        ],
    ],
    resize_keyboard=True
)
question3_weapon = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Боты"),
            KeyboardButton(text="Сапоги"),
        ],
        [
            KeyboardButton(text="Валенки"),
            KeyboardButton(text="Берцы")
        ],
    ],
    resize_keyboard=True
)
question4_weapon = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Погоны"),
            KeyboardButton(text="Пояс"),
        ],
        [
            KeyboardButton(text="Сворка"),
            KeyboardButton(text="Портупея")
        ],
    ],
    resize_keyboard=True
)
question5_weapon = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="7,62-мм автомат Калашникова 74"),
        ],
        [
            KeyboardButton(text="5,45-мм автоматическая винтовка Симонова"),
        ],
        [
            KeyboardButton(text="5,45-мм винтовка Мосина"),
        ],
        [
            KeyboardButton(text="7,62-мм винтовка Токарева СВТ-40"),
        ],
    ],
    resize_keyboard=True
)
question6_weapon = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Штык-нож"),
            KeyboardButton(text="Тесак"),
        ],
        [
            KeyboardButton(text="Штык"),
            KeyboardButton(text="Нож")
        ],
    ],
    resize_keyboard=True
)
question7_weapon = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Запасные карманы"),
            KeyboardButton(text="Патронные сумки"),
        ],
        [
            KeyboardButton(text="Подсумки"),
            KeyboardButton(text="Место для библии")
        ],
    ],
    resize_keyboard=True
)
question8_weapon = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Сумка для еды"),
            KeyboardButton(text="Сумка для медикаментов"),
        ],
        [
            KeyboardButton(text="Сумка для противогаза"),
            KeyboardButton(text="Сумка для конституции")
        ],
    ],
    resize_keyboard=True
)
question9_weapon = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Лопата"),
            KeyboardButton(text="Саперная лопата"),
        ],
        [
            KeyboardButton(text="Метательная лопата"),
            KeyboardButton(text="Тяпка")
        ],
    ],
    resize_keyboard=True
)

mina_place = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1"),
            KeyboardButton(text="2"),
        ],
        [
            KeyboardButton(text="3"),
            KeyboardButton(text="4")
        ],
        [
            KeyboardButton(text="5"),
            KeyboardButton(text="6")
        ],
        [
            KeyboardButton(text="7"),
            KeyboardButton(text="8")
        ],
        [
            KeyboardButton(text="9"),
            KeyboardButton(text="10")
        ],
        [
            KeyboardButton(text="11"),
            KeyboardButton(text="12")
        ],
    ],
    resize_keyboard=True
)


song_1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Cвященная война"),
            KeyboardButton(text="День победы"),
        ],
        [
            KeyboardButton(text="На плацу"),
            KeyboardButton(text="Маршируя")
        ],
    ],
    resize_keyboard=True
)

song_2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Прощание славянки"),
            KeyboardButton(text="Темная ночь"),
        ],
        [
            KeyboardButton(text="Любимый город"),
            KeyboardButton(text="Огонёк")
        ],
    ],
    resize_keyboard=True
)

song_3 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Эх, дороги"),
            KeyboardButton(text="Синий платочек"),
        ],
        [
            KeyboardButton(text="Катюша"),
            KeyboardButton(text="На солнечной поляночке")
        ],
    ],
    resize_keyboard=True
)

song_4 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Журавли"),
            KeyboardButton(text="Эх, дороги"),
        ],
        [
            KeyboardButton(text="Три танкиста"),
            KeyboardButton(text="Темная ночь")
        ],
    ],
    resize_keyboard=True
)

song_5 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Три танкиста"),
            KeyboardButton(text="В землянке"),
        ],
        [
            KeyboardButton(text="Смуглянка"),
            KeyboardButton(text="Москвичи")
        ],
    ],
    resize_keyboard=True
)

song_6 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Красная армия всех сильней"),
            KeyboardButton(text="За того парня"),
        ],
        [
            KeyboardButton(text="Бери шинель"),
            KeyboardButton(text="Священная война")
        ],
    ],
    resize_keyboard=True
)

song_7 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Марш преображенского полка"),
            KeyboardButton(text="Красная армия всех сильней"),
        ],
        [
            KeyboardButton(text="Священная война"),
            KeyboardButton(text="В землянке")
        ],
    ],
    resize_keyboard=True
)

song_8 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Прощайте, скалистые горы"),
            KeyboardButton(text="На солнечной полянке"),
        ],
        [
            KeyboardButton(text="Смуглянка"),
            KeyboardButton(text="Синий платочек")
        ],
    ],
    resize_keyboard=True
)

song_9 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="В лесу прифронтовом"),
            KeyboardButton(text="Нам нужна одна победа"),
        ],
        [
            KeyboardButton(text="Метательная лопата"),
            KeyboardButton(text="Марш преображенского полка")
        ],
    ],
    resize_keyboard=True
)


@dp.message_handler()
async def echo(message: Message):
    print(str(message.from_user.username))
    print(str(message.from_user.id))
    print(str(message.text))
