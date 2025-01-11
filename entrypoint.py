from src.config.orm import configure_orm

if __name__ == "__main__":
    configure_orm()

from src.tg_bot.handlers.endpoints_handler import EndpointsHandler
from src.tg_bot.app.builder import TelegramApplicationBuilder
from src.tg_bot.handlers.about_handler import about_handler
from src.tg_bot.handlers.menu_handler import main_menu_handler
from src.config.settings import TG_API_KEY
from src.tg_bot.handlers.start_handler import start_handler
from src.tg_bot.handlers.text_message_hanler import text_message_handler
from src.tg_bot.const import CALLBACK_DATA


def main():
    endpoint_handler = EndpointsHandler()
    # Создаём приложение
    app_builder = TelegramApplicationBuilder(TG_API_KEY)

    # Регистрируем хендлеры
    app_builder.add_command_handler("start", start_handler)
    app_builder.add_callback_query_handler(main_menu_handler, CALLBACK_DATA.MAIN_MENU)
    app_builder.add_callback_query_handler(about_handler, CALLBACK_DATA.ABOUT_COMPANY)
    app_builder.add_message_handler(text_message_handler)
    app_builder.add_callback_query_handler(endpoint_handler.handle)

    # Запускаем бота
    print("Бот запущен!")
    app_builder.build()
    app_builder.run()

if __name__ == "__main__":
    main()