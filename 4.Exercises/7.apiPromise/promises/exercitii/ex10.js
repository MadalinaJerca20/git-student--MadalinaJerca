// 10. Create a new user by sending a POST request to the backend server. 
//     Log the received http status code and the id of the newly created user.
//     (POST https://60623f0b0133350017fd0e29.mockapi.io/users).


const newUser = {};

async function writeData() {
  const response = await fetch(
    'https://60623f0b0133350017fd0e29.mockapi.io/users', 
    {
      method: 'POST',
      body: JSON.stringify(newUser),
    }
  );

  const object = await response.json();
  console.log(object);
}

writeData();


// avem mai multe tipuri de requesturi pe care HTTPUL le cunoste 
// POST 
// GET 
// PUT
// PATCH 
// DELETE
// OPTIONS

// HTTP-ul reprezinta un protocol de comunicare, un protocol care e implementat folosind comunicarea TCP, care e folosita de placa de retea
// la fel ca si la json, s-a gasit un standard de comunicare intre anumite servere, si anume servere pentru web
// si comunicarea asta poarta numele de http
// http respecta un set de reguli cum ar fi ca pe prima linie de mesaj sa fie aceasta metoda get/put/patch, url-ul
// apoi pe urmatoarea linie sa fie un spatiu gol si apoi
// pe a treia linie sa fie scrise cateva informatii care se numesc headere
// dupa acest header mai apare o linie in care poti specifica un continut, un mesaj
// in acest http exista aceste metode get,post, put/ patch, delete (read, create, update, delete) 