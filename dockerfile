FROM python:slim
ENV TOKEN='bot token'
COPY . .
RUN pip install -r req.txt
CMD python bot.py
