# Twilio-API-Project
# Introduction to APIs

### Remote APIs

* [Wikipedia - SOAP](https://en.wikipedia.org/wiki/SOAP)
* [Wikipedia - Remote Procedure Call (RPC)](https://en.wikipedia.org/wiki/Remote_procedure_call)
* [SOAP and REST at Odds](https://thehistoryoftheweb.com/soap-rest-odds/)
* [SOAP vs. REST](https://stackify.com/soap-vs-rest/)
* [REST vs. RPC](https://cloud.google.com/blog/products/application-development/rest-vs-rpc-what-problems-are-you-trying-to-solve-with-your-apis)

### How the web works

* [Wikipedia - HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol)
* [Space Jam Website](http://www.spacejam.com)

### RESTful API 

* [Wikipedia - Representational State Transfer](https://en.wikipedia.org/wiki/Representational_state_transfer)


### Using an API from the command line

* [Twilio](https://www.twilio.com/referral/d4X15O)
* [Twilio Console](https://twilio.com/console?utm_source=gh-link&utm_medium=referral&utm_campaign=intro-to-apis)
* [SMS Getting Started](https://www.twilio.com/console/sms/getting-started/build?utm_source=gh-link&utm_medium=referral&utm_campaign=intro-to-apis)
* Check out the [jq tutorial](https://stedolan.github.io/jq/tutorial/) for parsing JSON on the command line


### Using Postman to explore APIs

⬇️ - Download [Postman](https://postman.com/downloads)

The Twilio Messages API URL is:

```bash
https://api.twilio.com/2010-04-01/Accounts/<Your Account SID Here>/Messages.json
```

Make sure to replace that `SID` with your Account SID which can be found in the [Twilio console](https://twilio.com/console)


### Using Helper Libraries (JavaScript)

* [Install Node.js](https://nodejs.org/en/download/)
* [Install Python 3](https://www.python.org/downloads/)
* [Install Visual Studio Code](https://code.visualstudio.com/download)
  * [macOS](https://code.visualstudio.com/docs/setup/mac)
  * [Windows](https://code.visualstudio.com/docs/setup/windows)
  * [Linux](https://code.visualstudio.com/docs/setup/linux)

To use the [Twilio Node Helper Library](https://www.twilio.com/docs/libraries/node#installation)

```bash
npm install twilio
```

### Using Helper Libraries (Python)

* [Install Python 3](https://www.python.org/downloads/)

To use the [Twilio Python Helper Library](https://www.twilio.com/docs/libraries/python)

```bash
pip install twilio
```


### Introducing the project

* [Glitch](https://glitch.com)


### Flask app

⚠️ Several students have reported that cloning sets up a default Glitch application. If this happens to you, in the Glitch app that is created choose "Tools >> Extras >> Git Import and Export >> Import from GitHub" when prompted enter "craigsdennis/intro-to-apis-node" or "craigsdennis/intro-to-apis-flask"

[Complimentr Flask GitHub repository](https://github.com/craigsdennis/intro-to-apis-flask) is located at `https://github.com/craigsdennis/intro-to-apis-flask.git`

* [Twilio docs - Create a Message with Python](https://www.twilio.com/docs/sms/api/message-resource?code-sample=code-create-a-message&code-language=Python&utm_source=gh-link&utm_medium=referral&utm_campaign=intro-to-apis)
* [Twilio docs - List all Messages with Python](https://www.twilio.com/docs/sms/api/message-resource?utm_source=gh-link&utm_medium=referral&utm_campaign=intro-to-apis&code-sample=code-read-list-all-messages&code-language=Python)

#### Flask and Envoirmental Variables

* [Flask documentation](https://flask.palletsprojects.com/)
* [Environment Variables](https://www.twilio.com/docs/usage/secure-credentials)

