import requests


def get_signed_url(filename, content_type):
    url = "http://127.0.0.1:5001/nova-social---dev/asia-south1/fetchSignedBucketUrl"
    payload = {
        "data": {
            'fileName': filename, 
            'contentType': content_type
            }
    }

    response = requests.post(url, json=payload)
    result = response.json()
    if response.status_code == 200:
        print(result['result']['body'], 'the body')
        signed_url = result['result']['body']['url']
        signed_fields = result['result']['body']['fields']
        return signed_url, signed_fields
    else:
        print('Failed to get signed URL. Status Code:', response.status_code)
        print('Response:', response.text)
        return None, None


def upload_image(file_path, upload_url, upload_fields):
    with open(file_path, 'rb') as file:
        data = upload_fields
        files = {'file': (file_path, file)}
        try:
            response = requests.request(
                'POST', upload_url, data=data, files=files)
            print(response, 'the response')
            print('Image uploaded successfully!')

            check_file_status(upload_fields)
        except requests.exceptions.HTTPError as errh:
            print("HTTP Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            print("Something went wrong:", err)


def check_file_status(upload_fields):
    try:
        check_url = "http://127.0.0.1:5001/nova-social---dev/asia-south1/checkFileStatus"
        payload = {"data": {'uploadFields': upload_fields}}

        response = requests.post(check_url, json=payload)
        response.raise_for_status()

        data = response.json()
        result = data['result']
        print('response', result)
        if result['exists']:
            print('File URL:', result['fileUrl'])
        else:
            print('File does not exist:', data)
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("Something went wrong:", err)


if __name__ == "__main__":
    file_path = 'trial-2.jpe'
    filename = 'trial-2.jpe'
    content_type = 'image/jpeg'
    signed_url, signed_fields = get_signed_url(filename, content_type)

    print(
        f'File: {filename}\n'
        f'Content Type: {content_type}\n'
        f'Signed URL: {signed_url}\n'
        f'Signed Fields: {signed_fields}'
    )
    if signed_url and signed_fields:
        upload_image(file_path, signed_url, signed_fields)
    else:
        print('Failed to get signed URL. Aborting image upload.')


'''
(matrix) PS C:\WORK\matrix> python main.py
{'url': 'https://storage.googleapis.com/nova-dev-assets/', 'fields': {'x-goog-meta-source': 'Nova Social - DEV', 'key': '1707218399863__trial-2.jpe', 'x-goog-date': '20240206T111959Z', 'x-goog-credential': 'firebase-adminsdk-l23rk@nova-social---dev.iam.gserviceaccount.com/20240206/auto/storage/goog4_request', 'x-goog-algorithm': 'GOOG4-RSA-SHA256', 'policy': 'eyJjb25kaXRpb25zIjpbeyJ4LWdvb2ctbWV0YS1zb3VyY2UiOiJOb3ZhIFNvY2lhbCAtIERFViJ9LHsiYnVja2V0Ijoibm92YS1kZXYtYXNzZXRzIn0seyJrZXkiOiIxNzA3MjE4Mzk5ODYzX190cmlhbC0yLmpwZSJ9LHsieC1nb29nLWRhdGUiOiIyMDI0MDIwNlQxMTE5NTlaIn0seyJ4LWdvb2ctY3JlZGVudGlhbCI6ImZpcmViYXNlLWFkbWluc2RrLWwyM3JrQG5vdmEtc29jaWFsLS0tZGV2LmlhbS5nc2VydmljZWFjY291bnQuY29tLzIwMjQwMjA2L2F1dG8vc3RvcmFnZS9nb29nNF9yZXF1ZXN0In0seyJ4LWdvb2ctYWxnb3JpdGhtIjoiR09PRzQtUlNBLVNIQTI1NiJ9XSwiZXhwaXJhdGlvbiI6IjIwMjQtMDItMDZUMTE6MzQ6NTlaIn0=', 'x-goog-signature': '9627386e6e8564bd3a3a56ba46923aff1503680d1b9cdc5c5557f7053736f655cb748648b73b922e4cd52647eee34aabb27f003d570d7bee4e3512d943004775ba487d26ec9f358c61432ab365c96e8dbb1299fd9b785e55b0dd004b0a6c41600a96fb349c70d4b0c8f56dbf4d17c30c9cd347c13ffbbead626647db70fbfe950d7baf06c664b5a442b5c54ba50102fd924b9e3a1a88577daa79ae51a49595123b23bfe038794dfdc5eda7808e8c65dd16a02347ef3242133fcd7715a7e6a645decade95edb35ab778a743d9cb4179a764532f7d08fa9bc6c1f0a00160dbb7a8c0fae7aae0c7aa00dd76af8ee1798b7200ddee0cecf3611b750676cdf53cd808'}} the body
File: trial-2.jpe
Content Type: image/jpeg
Signed URL: https://storage.googleapis.com/nova-dev-assets/
Signed Fields: {'x-goog-meta-source': 'Nova Social - DEV', 'key': '1707218399863__trial-2.jpe', 'x-goog-date': '20240206T111959Z', 'x-goog-credential': 'firebase-adminsdk-l23rk@nova-social---dev.iam.gserviceaccount.com/20240206/auto/storage/goog4_request', 'x-goog-algorithm': 'GOOG4-RSA-SHA256', 'policy': 'eyJjb25kaXRpb25zIjpbeyJ4LWdvb2ctbWV0YS1zb3VyY2UiOiJOb3ZhIFNvY2lhbCAtIERFViJ9LHsiYnVja2V0Ijoibm92YS1kZXYtYXNzZXRzIn0seyJrZXkiOiIxNzA3MjE4Mzk5ODYzX190cmlhbC0yLmpwZSJ9LHsieC1nb29nLWRhdGUiOiIyMDI0MDIwNlQxMTE5NTlaIn0seyJ4LWdvb2ctY3JlZGVudGlhbCI6ImZpcmViYXNlLWFkbWluc2RrLWwyM3JrQG5vdmEtc29jaWFsLS0tZGV2LmlhbS5nc2VydmljZWFjY291bnQuY29tLzIwMjQwMjA2L2F1dG8vc3RvcmFnZS9nb29nNF9yZXF1ZXN0In0seyJ4LWdvb2ctYWxnb3JpdGhtIjoiR09PRzQtUlNBLVNIQTI1NiJ9XSwiZXhwaXJhdGlvbiI6IjIwMjQtMDItMDZUMTE6MzQ6NTlaIn0=', 'x-goog-signature': '9627386e6e8564bd3a3a56ba46923aff1503680d1b9cdc5c5557f7053736f655cb748648b73b922e4cd52647eee34aabb27f003d570d7bee4e3512d943004775ba487d26ec9f358c61432ab365c96e8dbb1299fd9b785e55b0dd004b0a6c41600a96fb349c70d4b0c8f56dbf4d17c30c9cd347c13ffbbead626647db70fbfe950d7baf06c664b5a442b5c54ba50102fd924b9e3a1a88577daa79ae51a49595123b23bfe038794dfdc5eda7808e8c65dd16a02347ef3242133fcd7715a7e6a645decade95edb35ab778a743d9cb4179a764532f7d08fa9bc6c1f0a00160dbb7a8c0fae7aae0c7aa00dd76af8ee1798b7200ddee0cecf3611b750676cdf53cd808'}
<Response [204]> the response
Image uploaded successfully!
response {'message': 'File status checked successfully', 'exists': True, 'fileUrl': 'https://storage.googleapis.com/nova-dev-assets/1707218399863__trial-2.jpe'}
File URL: https://storage.googleapis.com/nova-dev-assets/1707218399863__trial-2.jpe
'''
