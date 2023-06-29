app_title = 'Template Application'

app_desc = """
Модуль ---- 🚀

Описание модуля

Используйте markdown, он здесь работает отлично

### Подзаголовок

**не** показывается в левом меню!
"""

app_version = '0.0.1'

app_docs = '/api/v1/docs'
app_redoc = '/api/v1/redoc'
app_openapi = '/api/v1/openapi.json'

app_tags = [
    {
        "name": "Users",
        "description": "This is Users tags. Everything that's tagged Users, goes here. This section is responsible "
                       "for user authentication, operations on users and stuff like that...",
    },
    {
        "name": "Things",
        "description": "Same goes for any other tag you might wanna add...",
    },
]

redoc_config = {
    "spec": {
        "openapi": "3.0.0",
    },
    "strings": {
        "get": "Получить",
        "put": "Поместить",
        "post": "Отправить",
        "delete": "Удалить",
        "options": "Опции",
        "head": "Заголовок",
        "patch": "Заменить",
        "trace": "Трассировка",
    },
    "options": {
        "language": "ru",
        "scrollYOffset": "nav.height",
        "nativeScrollbars": True,
        "hideDownloadButton": True,
    },
    "theme": {
        "colors": {
            "primary": {
                "main": "#f01800"
            },
            "http": {
                "get": "#00cc99",
                "post": "#8a2be2",
                "put": "#ff9900",
                "delete": "#f44336",
                "options": "#9c27b0",
                "head": "#795548",
                "patch": "#00bcd4",
                "trace": "#607d8b"
            }
        },
        "typography": {
            "fontFamily": "Roboto, sans-serif",
            "fontSize": "16px",
        },
        "sidebar": {
            "backgroundColor": "#f5f5f5",
            "width": "240px"
        },
        "rightPanel": {
            "backgroundColor": "#333",
            "width": "40%",
            "fontFamily": "Roboto, sans-serif"
        },
        "codeBlock": {
            "backgroundColor": "#555"
        },
        "logo": {
            "height": "40px"
        }
    },
}
