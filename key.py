from aiogram.types \
    import InlineKeyboardMarkup, InlineKeyboardButton

# inline-кнопки для отображения выбора роли
inline_kb_role = InlineKeyboardMarkup(row_width=2)
inline_kb_role.add(InlineKeyboardButton('студент', callback_data='btn_student'),
                   InlineKeyboardButton('преподаватель', callback_data='btn_teacher'))

# inline-кнопки для отображения выбора вида отображения расписания
inline_btn_today = InlineKeyboardButton('на день', callback_data='btn_today')
inline_btn_week = InlineKeyboardButton('на неделю', callback_data='btn_week')
inline_btn_2weeks = InlineKeyboardButton('на 2 недели', callback_data='btn_week')
inline_btn_full = InlineKeyboardButton('на весь семестр', callback_data='btn_2_week')

inline_kb_mode = InlineKeyboardMarkup(row_width=2).add(inline_btn_today)
inline_kb_mode.add(inline_btn_week, inline_btn_2weeks)
inline_kb_mode.add(inline_btn_full)


# кнопка "назад"
inline_btn_back = InlineKeyboardButton('назад', callback_data='btn_back')
inline_k_back = InlineKeyboardMarkup().add(inline_btn_back)
