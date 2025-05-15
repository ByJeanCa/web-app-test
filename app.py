from flask import Flask, request, render_template
import os
import boto3
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)

s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('AWS_REGION')
)

BUCKET_NAME = os.getenv('S3_BUCKET')

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        s3.upload_fileobj(file, BUCKET_NAME, file.filename)
        return 'Archivo subido exitosamente a S3.'
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)