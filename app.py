import streamlit as st
import time

# Настройка страницы
st.set_page_config(page_title="Онбординг: Новичок", page_icon="🚀")
st.title("🚀 Твой первый месяц в ТГТ")
st.write("Этот помощник поможет тебе быстрее адаптироваться и не потеряться в первый месяц.")

# Создаем две вкладки
tab1, tab2 = st.tabs(["✅ Чек-лист новичка", "🤖 AI-Ассистент"])

# --- ВКЛАДКА 1: ЧЕК-ЛИСТ ---
with tab1:
    st.header("Твои первые шаги")
    st.write("Отмечай выполненные задачи, чтобы ничего не забыть:")
    
    # Чекбоксы
    doc_done = st.checkbox("📄 Подписать документы у HR")
    acc_done = st.checkbox("💻 Получить доступы (корпоративная почта, Bitrix24)")
    mate_done = st.checkbox("🤝 Встретиться с наставником")
    product_done = st.checkbox("📦 Изучить ассортимент (спорттовары и бытовая техника)")
    
    # Кнопка проверки
    if st.button("Проверить прогресс"):
        total = 4
        done = sum([doc_done, acc_done, mate_done, product_done])
        progress = done / total
        st.progress(progress)
        if done == total:
            st.balloons()
            st.success("Красавчик! Ты полностью готов к работе!")
        else:
            st.info(f"Выполнено {done} из {total} задач. Продолжай в том же духе!")

# --- ВКЛАДКА 2: AI-АССИСТЕНТ ---
with tab2:
    st.header("Задай любой вопрос")
    st.write("Я знаю ответы на частые вопросы новичков. Спроси меня, например: *'Где взять пропуск?'* или *'К кому обратиться по поводу зарплаты?'*")

    # Инициализация истории чата
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Отображение истории
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Поле ввода
    if prompt := st.chat_input("Напиши свой вопрос здесь..."):
        # Добавляем сообщение пользователя
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Мок-ответ (имитация ИИ)
        with st.chat_message("assistant"):
            with st.spinner("Думаю..."):
                time.sleep(1) # Имитация задержки
                prompt_lower = prompt.lower()
                
                # Простая логика ответов
                if "пропуск" in prompt_lower:
                    response = "Для получения пропуска обратитесь в отдел кадров (кабинет 105) к Виктории."
                elif "зарплат" in prompt_lower:
                    response = "По вопросам заработной платы и расчетных листков обращайтесь в бухгалтерию к Анне (кабинет 203)."
                elif "обед" in prompt_lower or "столов" in prompt_lower:
                    response = "Столовая находится на 2-м этаже. Обед с 13:00 до 14:00."
                elif "наставник" in prompt_lower:
                    response = "Ваш наставник закреплен за вами в Bitrix24. Проверьте список задач."
                else:
                    response = "Хороший вопрос! Я пока только учусь. Уточните его у вашего наставника или напишите в общий чат 'Новички' в Telegram."
                
                st.markdown(response)
        # Добавляем ответ в историю
        st.session_state.messages.append({"role": "assistant", "content": response})