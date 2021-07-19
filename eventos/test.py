import requests


def test(msg_body):

    HCTI_API_ENDPOINT = "https://hcti.io/v1/image"
    HCTI_API_USER_ID = '3aa5fdbf-f3f9-4557-b7d3-14277e4b03fa'
    HCTI_API_KEY = 'fb956df5-e50b-420e-a34d-05a90703bf84'

    content =dict(
            text= msg_body,
        )

    data = { 'html': "<div class='box'><p>'{{text}}'</p></div>",
            'css': ".box { color: white; background-color: #0f79b9; padding: 10px; font-family: Roboto }",
            'google_fonts': "Roboto" }

    image = requests.post(url = HCTI_API_ENDPOINT, data = data, auth=(HCTI_API_USER_ID, HCTI_API_KEY))

    print("Your image URL is: %s"%image.json()['url'])
    # https://hcti.io/v1/image/7ed741b8-f012-431e-8282-7eedb9910b32


test('1234')