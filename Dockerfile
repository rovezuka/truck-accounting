# Используем официальный образ Python в качестве базового образа
FROM python:3.10.12
# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /mining_project
# Копируем файл requirements.txt внутрь контейнера
COPY requirements.txt ./
# Устанавливаем зависимости, описанные в файле requirements.txt
RUN pip install -r requirements.txt