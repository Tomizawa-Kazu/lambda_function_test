FROM amazon/aws-lambda-python:3.9

COPY requirements.txt lambda_function.py ./
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "lambda_function.lambda_handler" ]