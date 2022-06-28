FROM python:alpine
COPY score/MainScores.py .
COPY Utils.py WoG/
COPY Scores.txt .
RUN pip install flask
CMD python ./MainScores.py
