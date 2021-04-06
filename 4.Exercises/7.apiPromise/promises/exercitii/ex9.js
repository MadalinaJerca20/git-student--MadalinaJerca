// 9. Get all users from https://60623f0b0133350017fd0e29.mockapi.io/users and display their names in HTML.
// I.
fetch('https://60623f0b0133350017fd0e29.mockapi.io/users')
  .then((response) => response.json())
  .then((data) => console.log(data));


// II.
async function getData() {
  const response = await fetch('https://60623f0b0133350017fd0e29.mockapi.io/users');
  const object = await response.json();
  console.log(object);
}

getData();

// III.
async function getData(url) {
  const response = await fetch(url);
  const object = await response.json();
  return(object);
}

async function main() {
  const response = await getData('https://60623f0b0133350017fd0e29.mockapi.io/users')
  console.log(response)
}

main();


// json este un concept, un mod de comunicare intre doua servere, doua programe, doua functii
// pentru ca aplicatiile sa comunice intre ele, au nevoie de un format standard a mesajelor 
// mesajul standard poarta numele de serializare
// Serialization means to convert an object into that string, and deserialization is its inverse operation (convert string -> object).
// serializarea poate fi csv, json, etc
// modul standard in javascript este json
// by default, fetch foloseste metoda get