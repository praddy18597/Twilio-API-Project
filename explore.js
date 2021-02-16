const Twilio = require("twilio");

const client = new Twilio("ACc17a00d0a73936e0ac1deae70b3c4dc9", "568c7be1e1138bacd2b5dadaa85c7b9d");

"//Returns the promise value that is future messages"
client.messages.list().then(messages => console.log(`the most recent message is ${messages[0].body}`));

console.log('Gathering your message log')